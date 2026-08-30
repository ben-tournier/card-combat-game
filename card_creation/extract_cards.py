from pathlib import Path
from copy import deepcopy
import json

from card_creation.card import Card

# This function is used to upgrade cards throughout the game as you progress
def build_card(card_data, cardid):
    return Card(
        name=card_data["name"],
        card_type=card_data["type"],
        card_id=cardid,
        gold_cost=card_data["gold"],
        damage=card_data.get("damage", 0),
        block=card_data.get("block", 0),
        cost=card_data["cost"]
    )

# Here the card information is loaded from the json file and loaded to where it was called
def load_cards():
    file_path = Path(__file__).parent / "card_info.json"

    with open(file_path, "r") as f:
        data = json.load(f)

    cards = {}

    for entry in data["cards"]:
        card_id = entry["cardid"]

        cards[card_id] = {
            "basic": build_card(entry["basic"], card_id),
            "upgraded": build_card(entry["upgraded"], card_id)
        }

    return cards

# this will reextract the cards later when going through a save file with variety of versions
def get_card_by_name(name):
    cards = load_cards()

    for card_pair in cards.values():

        if card_pair["basic"].name == name: 
            return deepcopy(card_pair["basic"])

        if card_pair["upgraded"].name == name: 
            return deepcopy(card_pair["upgraded"])

    return None