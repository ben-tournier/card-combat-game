import json, os

SAVE_FOLDER = "data/saves"
"""
When the save game function is called python will take the player object and turn it to the dictionary
it will then make a save data dictionary to save the player dictionary as player as well as save the game object itself

then opens up the data/saves/save1.json in writing mode to add stuff 
uses the json library imported to dump the python dictionary in as JSON text instead
"""




def save_game(game):
    save_data = game.to_dict()

    with open(
        "data/saves/save1.json",
        "w"
    ) as file: 
        json.dump(
            save_data,
            file, 
            indent=4
        )