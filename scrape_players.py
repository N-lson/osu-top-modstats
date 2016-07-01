from time import sleep
from collections import OrderedDict
import csv
import re
import sys

import requests
from bs4 import BeautifulSoup


def scrape(num_players):
    url = "https://osu.ppy.sh/p/pp/"
    players = OrderedDict()

    # Handle invalid input
    if num_players%50 != 0:
        num_players = 50

    max_page = num_players//50

    for i in range(1, max_page+1):
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


if __name__ == "__main__":
    players = scrape(int(sys.argv[1]))