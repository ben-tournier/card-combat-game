
from pathlib import Path
import json 

from card_creation.card import Card

#
def load_cards():

    file_path = Path(__file__).parent / "card_info.json"

    with open(file_path, 'r') as f:
        data = json.load(f)

    cards = []

    for card in data["basic_cards"]: 
        new_card = Card(
            name=card["name"], 
            card_type=card["type"],
            damage=card.get("damage", 0),
            block=card.get("block", 0),
            cost=card["cost"]

            )
        cards.append(new_card)
        
    return cards