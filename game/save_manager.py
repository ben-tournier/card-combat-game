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


"""
will open up the file with the save in it to read and stores it as variable file 
then simply returns all of the save data to the call
"""

def load_game():

    with open(
        "data/saves/save1.json",
        "r"
    ) as file:

        data = json.load(file)

    from game.game import Game

    return Game.from_dict(data)