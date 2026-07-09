from pathlib import Path
import json

from card_creation.card import Card

# This function is used to upgrade cards throughout the game as you progress
def build_card(card_data, cardid):
    return Card(
        name=card_data["name"],
        card_type=card_data["type"],
        card_id=cardid,
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