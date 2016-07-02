from time import sleep
import csv
import sys
import json

import requests

from api_key import API_KEY


def read_csv():
    players = {}
    with open("players.csv", "r") as f:
        r = csv.reader(f)
        for row in r:
            user_name = row[0]
            user_id = row[1]
            players[user_name] = user_id

    return players


if __name__ == "__main__":
    players = read_csv()
    url = "https://osu.ppy.sh/api/get_user_best"

    for i, user_name in enumerate(players):
        print("Obtaining scores for {} [Progress: {}/{}]".format(user_name, i+1, len(players)))
        payload = {"k": API_KEY, "u": user_name, "m": 0, "limit": 10, "type": "string"}
        r = requests.get(url, params=payload)
        scores = json.loads(r.text)

        with open("scores.csv", "a", newline="") as f:
            w = csv.writer(f)
            for score in scores:
                beatmap = score["beatmap_id"]
                mods = score["enabled_mods"]
                w.writerow([user_name, beatmap, mods])

        sleep(1)