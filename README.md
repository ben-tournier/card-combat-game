# Card Combat Game

A turn-based card combat game built in Python. The project was created as a programming project to practice **object-oriented programming, data structures, JSON data management, game-state management, and modular program design**.

The game features a deck-building style combat system where the player draws cards, spends energy to play them, defeats enemies, earns rewards, and progresses through increasingly difficult encounters.

## Features

* Turn-based card combat
* Player and enemy combatants
* JSON-based card data
* Object-oriented card, deck, player, and enemy classes
* Draw pile, hand, and discard pile system
* Five-card starting hand
* Energy-based card costs
* Card rewards and deck progression
* Elite encounters every 5 rounds
* Boss encounters every 10 rounds
* Game-state saving and loading
* Modular project structure

## How the Game Works

The player begins with a starting deck and enters combat against enemies.

Each combat revolves around managing:

* **Cards** – Used to attack, defend, or produce other effects
* **Energy** – Limits how many cards can be played during a turn
* **Hand** – Cards currently available to the player
* **Draw pile** – Cards available to be drawn
* **Discard pile** – Cards that have already been played
* **Health** – Determines whether the player or enemy remains in combat

As the player progresses, encounters become more challenging and rewards allow the player to improve their deck.

## Combat System

The game uses a turn-based combat structure.

A typical combat loop involves:

1. Drawing cards
2. Receiving available energy
3. Playing cards from the hand
4. Applying card effects
5. Ending the player's turn
6. Allowing the enemy to act
7. Repeating until the combat ends

Cards have different costs and effects, requiring the player to decide how to spend their available energy.

## Deck System

The game uses a dedicated battle deck system to manage cards during combat.

The `BattleDeck` maintains three primary collections:

```text
Draw Pile
    ↓
   Hand
    ↓
Discard Pile
```

The player's starting hand contains **5 cards**, and the battle deck is populated from the player's available cards.

Cards are loaded from JSON data and copied when necessary so that combat can modify individual card objects without unintentionally modifying the original card definitions.

## Card Data

Card information is stored separately from the game's Python logic using JSON.

This allows cards to be added or modified without having to hard-code every card directly into the game.

A card can contain information such as:

* Name
* Cost
* Damage
* Defense
* Effect information
* Other gameplay properties

Separating the data from the game logic also makes the project easier to expand.

## Progression

The game includes encounter-based progression.

### Regular Encounters

Normal encounters provide the standard progression through the game.

### Elite Encounters

Every **5 rounds**, the player encounters an elite enemy.

Elite encounters provide greater difficulty and improved rewards.

### Boss Encounters

Every **10 rounds**, the player encounters a boss.

Boss encounters serve as major progression milestones and are intended to provide a significant increase in difficulty.

## Energy System

Cards require energy to play.

At the beginning of a turn, the player receives available energy and must decide how to spend it.

For example:

```text
Available Energy: 3

Attack Card: 1 Energy
Defense Card: 1 Energy
Powerful Attack: 2 Energy

Possible combination:
1 + 2 = 3 Energy
```

This creates a resource-management component to combat rather than allowing the player to play every card in their hand.

## Saving and Loading

The project includes a `save_manager.py` module for managing persistent game state.

Game information is stored in JSON so that a game can be saved and loaded between sessions.

The save system is designed to preserve relevant information such as the player's current game state and progression.

This system also provides practice working with:

* JSON serialization
* JSON deserialization
* File handling
* Persistent program state

## Project Structure

The project is organized into separate modules so that different parts of the game have their own responsibilities.

```text
Card Combat Game/
│
├── data/
│   └── cards.json
│
├── src/
│   ├── main.py
│   ├── deck.py
│   ├── player.py
│   ├── enemy.py
│   └── save_manager.py
│
├── saves/
│   └── save data
│
└── README.md
```

*The exact filenames and folders may vary as the project continues to develop.*

## Object-Oriented Design

The project uses classes to represent major game objects.

Examples include:

### Player

Represents the player and manages information such as health, cards, energy, and progression.

### Enemy

Represents opponents encountered during combat.

### Deck / BattleDeck

Manages card collections and the movement of cards between the draw pile, hand, and discard pile.

### Cards

Represent individual playable cards and their associated properties.

Using classes allows each object to manage its own data and behavior instead of placing all game logic inside one large program.

## Technologies

* **Python**
* **JSON**
* Object-Oriented Programming
* File I/O
* Data structures
* Git / GitHub

## What I Learned

This project was primarily developed as a way to gain practical programming experience.

Major concepts practiced include:

* Classes and objects
* Encapsulation
* Functions and modular programming
* Lists and other data structures
* Deep copying objects
* JSON data management
* Reading and writing files
* Managing game state
* Designing interacting classes
* Debugging larger Python programs
* Using Git and GitHub for version control

## Future Improvements

Possible future additions include:

* More cards and enemy types
* Additional card effects
* Status effects
* More varied enemy behaviors
* Multiple character classes
* More complex deck-building mechanics
* Expanded reward choices
* Improved user interface
* More advanced save-state management
* Additional bosses and elite encounters

## Project Status

**In Development**

The core combat, deck, progression, reward, and save systems have been implemented, while additional gameplay mechanics and content can continue to be added.
