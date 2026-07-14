from deck_creation_and_adjustment.battle_deck import BattleDeck
import time
# This is where the users information is stored
# On top of keeping a bunch of the deck information in here it will also store hp, block, etc.


class Player:

    def __init__(self, name):
        self.name = name
        self.deck = BattleDeck()
        self.deck.fill_starting_deck()
        self.deck.shuffle_deck()
        self.hp = 25
        self.block = 0
        self.gold = 20
        self.money_pool = 0
        self.energy = 0
        self.max_energy = 3

    def combat_state(self):
        print(f"\nYou currently have {self.block} block and {self.hp} hp")

        # ------------- Hand functions -------------
    def remove_all_block(self):
        if self.block > 0:
            print("Removing all block")
        self.block = 0

    def relay_cards_in_hand(self):
        return self.deck.show_hand()

    # may eventually be extended to add in removal of all temporary effects
    def end_of_turn(self):
        print("Discarding Hand... \n")
        self.deck.discard_hand()

        # ------------- Energy functions -------------
    def fill_energy(self):
        self.energy = self.max_energy

    def energy_left(self):
        return self.energy > 0

    def current_energy(self):
        return self.energy

    def check_energy_amount(self, cost):
        return self.energy >= cost

    def charge_energy(self, amount):
        self.energy -= amount
        return self.energy

        # ------------- Combat functions -------------
    def check_card_type(self, index):
        return self.deck.get_type(index)

    def check_card_damage(self, index):
        return self.deck.card_deals_damage(index)

    def gain_block(self, amount):
        self.block += amount

    def heal(self, amount):
        self.hp += amount
        return f"{self.name} healed up to {self.hp} hp"

    def take_damage(self, enemy):
        amount_through = 0
        amount = enemy.get_damage()

        if self.block > 0:
            self.combat_state()

        if amount > self.block:
            amount_through = amount - self.block
            self.block = 0
            self.hp -= amount_through
        else:
            self.block -= amount

        print(f"{enemy} delt {amount} damage to {self.name}")

        if amount_through > 0:
            print(f"{amount_through} set {self.name}'s HP down to {self.hp}")

        if self.hp < 0:
            self.hp = 0

    def player_dead(self):
        return self.hp == 0

    # this is the function that actually playst the card in the player combat system
    def play_card(self, index, enemy):

        card_played = self.deck.get_card(index)

        if card_played is None:
            print("Invalid card choice")
            return

        energy_cost = card_played.get_energy_cost()

        if not self.check_energy_amount(energy_cost):
            print(f"Sorry {card_played.name} requires {energy_cost} energy.")
            return

        self.charge_energy(energy_cost)

        # Remove the card from the hand only AFTER paying the cost
        card_played = self.deck.play_card_from_hand(index)

        print(f"Playing {card_played.name} for {energy_cost} energy")

        actions_from_card = []

        # ---------- Cycle ----------
        if card_played.card_type == "cycle":
            self.deck.draw_card()
            actions_from_card.append("Drawing another card")

        # ---------- Damage ----------
        if enemy is not None and card_played.damage > 0:

            enemy.take_damage(card_played.damage)

            actions_from_card.append(
                f"dealing {card_played.damage} damage to {enemy}"
            )

            if not enemy.is_alive():
                actions_from_card.append(f"{enemy.name} has been killed")
                self.money_pool += enemy.value

        # ---------- Block ----------
        if card_played.block > 0:

            self.gain_block(card_played.block)

            actions_from_card.append(
                f"gaining {card_played.block} block"
            )

        for action in actions_from_card:
            print(action)    


        # ------------- Spending Functions -------------
    def cleanup_gold(self):
        self.gold += self.money_pool
        self.money_pool = 0

    def spend_gold(self, amount):
        if amount > self.gold:
            return False
        return True

    def gain_gold(self, amount):
        self.gold += amount

    def __repr__(self):
        return f"Player(HP={self.hp}, Block={self.block}, Gold={self.gold})"