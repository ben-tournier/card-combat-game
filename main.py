from game import run

# This is going to be the outermost shell for the game to work
# it will call in a lot from the game file which is where a lot of the dirty work happens

GAME_FLOW = [
    "In this game there are a couple simple loops that will allow for you to construct a deck and fight enemies with it", 
    "• You recieve a starting deck with 5 Strikes, 5 Shields, and 1 Hypnotize", 
    "• For more information about how each card works enter 'i' followed by the index of the card you want to check"
    "• Enemies will be given and it is up to you to choose which card to use against which enemy", 
    "• Please give your response in the form of a number",
    "• You may cast up to 3 cars per turn"
    "• As the game progresses the enemies will get tougher and grow in number", 
    "• Throughout the game stations will occur where you can either: \n   1) Remove a card from your deck \n   2) Add a card to your deck \n   3) Upgrade a card in your deck",
    "The rest is up to you! Best of luck \n"
]

for txt in GAME_FLOW:
    print(txt)


# This outermost shell is not currently used for much but eventually may include save files and other data 
def main():
    run()

main()