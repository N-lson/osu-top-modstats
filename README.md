# osu-top-modstats

Statistics for high ranked players' top performances - displays the most frequent maps, as well as mod combinations

# Usage

* `python scrape_players.py [NUM_PLAYERS]` to obtain a current list of top players, where num_players is a multiple of 50

# Other

To compile the ui files (already done), cd to root folder, then run:
* `pyrrc5.exe .\icons\icons.qrc -o icons_rc.py` to compile resources
* `pyuic5.bat program.ui -o program_ui.py` to compile program.ui