from time import sleep
import csv
import sys
import json
import operator

import requests

from api_key import API_KEY


all_mods = {
    "NF": 1 << 0,
    "EZ": 1 << 1,
    # NoVideo
    "HD": 1 << 3,
    "HR": 1 << 4,
    "SD": 1 << 5,
    "DT": 1 << 6,
    # Relax
    "HT": 1 << 8,
    "NC": (1 << 9) + (1 << 6),
    "FL": 1 << 10,
    # Auto
    "SO": 1 << 12,
    # Autopilot
    "PF": 1 << 14
}

mod_frequencies = {}
map_frequencies = {}

def read_csv():
    players = {}
    with open("players.csv", "r") as f:
        r = csv.reader(f)
        for row in r:
            user_name = row[0]
            user_id = row[1]
            players[user_name] = user_id

    return players


def add_map(map):
    for data in map:
        map_name = "{} - {} [{}] ({})".format(data["artist"], data["title"], data["version"], data["creator"])

    map_frequencies.setdefault(map_name, 0)
    map_frequencies[map_name] += 1

    return map_name


def add_mod(mods):
    mod_combination = ""
    while mods > 0:
        for mod, value in all_mods.items():
            if mods >= value and mods/2 < value:
                mod_combination += mod
                mods -= value

    if mod_combination == "":
        mod_combination = "Nomod"

    mod_frequencies.setdefault(mod_combination, 0)
    mod_frequencies[mod_combination] += 1

    return mod_combination


if __name__ == "__main__":
    players = read_csv()
    url_best = "https://osu.ppy.sh/api/get_user_best"
    url_map = "https://osu.ppy.sh/api/get_beatmaps"

    for i, user_name in enumerate(players):
        print("Obtaining scores for {} [Progress: {}/{}]".format(user_name, i+1, len(players)))
        payload = {"k": API_KEY, "u": user_name, "m": 0, "limit": 10, "type": "string"}
        r = requests.get(url_best, params=payload)
        scores = json.loads(r.text)

        for score in scores:
            beatmap = score["beatmap_id"]
            payload = {"k": API_KEY, "b": beatmap, "limit": 1}
            r = requests.get(url_map, params=payload)
            map = json.loads(r.text)
            current_map = add_map(map)

            mods = int(score["enabled_mods"])
            current_mods = add_mod(mods)
            print(current_map, current_mods)
            sleep(0.5)

        sleep(1)

    ordered_maps = sorted(map_frequencies.items(), key=operator.itemgetter(1), reverse=True)
    ordered_mods = sorted(mod_frequencies.items(), key=operator.itemgetter(1), reverse=True)

    with open("map_frequencies.csv", "w", newline="") as f:
        w = csv.writer(f)
        for map_name, frequency in map_frequencies.items():
            w.writerow([map_name, frequency])

    with open("mod_frequencies.csv", "w", newline="") as f:
        w = csv.writer(f)
        for mod_combination, frequency in mod_frequencies.items():
            w.writerow([mod_combination, frequency])