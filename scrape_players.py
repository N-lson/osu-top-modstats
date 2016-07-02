from time import sleep
import csv
import re
import sys

import requests
from bs4 import BeautifulSoup


def scrape(num_players):
    url = "https://osu.ppy.sh/p/pp/"
    players = {}

    # Handle invalid input
    if num_players%50 != 0:
        print("num_players must be divisible by 50")
        return None

    max_page = num_players//50 + 1

    for i in range(1, max_page):
        print("Currently processing page {}".format(i))
        payload = {"m": 0, "page": i}
        r = requests.get(url, params=payload)
        page = BeautifulSoup(r.text, "lxml")
        for player in page.findAll("a", {"href":re.compile("^(\/u\/)[0-9]+$")}):
            # Remove '/u/' from url to obtain user id
            user_id = player.attrs["href"][3:]
            user_name = player.get_text()
            players[user_name] = user_id
            print(user_name, user_id)
        sleep(1)

    return players


def write_csv(players):
    with open("players.csv", "w", newline="") as f:
        w = csv.writer(f)
        for user_name, user_id in players.items():
            w.writerow([user_name, user_id])


if __name__ == "__main__":
    players = scrape(int(sys.argv[1]))
    if players is not None:
        write_csv(players)