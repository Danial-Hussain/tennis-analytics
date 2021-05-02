"""
headshots.py:
Scraper to collect player headshots.
"""

__author__ = "Ali Hussain"
__version__ = "1.0"

# Import libraries
import requests as rq
from bs4 import BeautifulSoup
import json

# Get the URL
URL = 'http://www.espn.com/tennis/players'
page = rq.get(URL)

# Create BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Find all links
players = soup.find_all("a", href = True)

# Hold player name and image link
data = {}

# Get the player and headshot link
for player in players:
	name = player.text
	try:
		player_id  = player['href'].partition("id/")[2].partition("/")[0]
		link = f"https://a.espncdn.com/combiner/i?img=/i/headshots/tennis/players/full/{player_id}.png"
		data[name] = link
	except:
		print("Not a player link")

# Save the dictionary as a json file
with open("headshots.json", 'w') as outfile:
	json.dump(data, outfile)