from time import sleep
import csv
import json
import sys
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


def read_csv():
    players = {}
    with open("players.csv", "r") as f:
        r = csv.reader(f)
        for row in r:
            user_name = row[0]
            user_id = row[1]
            players[user_name] = user_id

    return players


def convert_ids(beatmap_ids):
    url = "https://osu.ppy.sh/api/get_beatmaps"
    map_frequencies = {}
    for i, id in enumerate(beatmap_ids):
        success = False
        while not success:
            try:
                payload = {"k": API_KEY, "b": id, "limit": 1}
                r = requests.get(url, params=payload)
                r.raise_for_status()
                map = json.loads(r.text)
                success = True
            except Exception as e:
                print("Beatmap {} | Error: {}".format(id, e), file=sys.stderr)

        for data in map:
            map_name = "{} - {} [{}] ({})".format(data["artist"], data["title"], data["version"], data["creator"])
            print("[{}/{}] | {} | Freq: {}".format(i, len(beatmap_ids), map_name, beatmap_ids[id]))
            map_frequencies[map_name] = beatmap_ids[id]

        sleep(0.9)

    return map_frequencies


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


def add_map_id(beatmap_id):
    beatmap_ids.setdefault(beatmap_id, 0)
    beatmap_ids[beatmap_id] += 1


def get_scores(players):
    url = "https://osu.ppy.sh/api/get_user_best"

    for i, user_name in enumerate(players):
        print("Obtaining scores for {} [Progress: {}/{}]".format(user_name, i + 1, len(players)))
        payload = {"k": API_KEY, "u": user_name, "m": 0, "limit": 10, "type": "string"}
        r = requests.get(url, params=payload)
        scores = json.loads(r.text)

        for score in scores:
            beatmap_id = score["beatmap_id"]

            mods = int(score["enabled_mods"])
            add_mod(mods)
            add_map_id(beatmap_id)

        sleep(0.8)

if __name__ == "__main__":
    players = read_csv()

    mod_frequencies = {}
    beatmap_ids = {}

    get_scores(players)

    map_frequencies = convert_ids(beatmap_ids)

    ordered_maps = sorted(map_frequencies.items(), key=operator.itemgetter(1), reverse=True)
    ordered_mods = sorted(mod_frequencies.items(), key=operator.itemgetter(1), reverse=True)

    with open("map_frequencies.csv", "w", newline="") as f:
        w = csv.writer(f)
        for map_name, frequency in ordered_maps:
            w.writerow([map_name, frequency])

    with open("mod_frequencies.csv", "w", newline="") as f:
        w = csv.writer(f)
        for mod_combination, frequency in ordered_mods:
            w.writerow([mod_combination, frequency])