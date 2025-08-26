#Command-Line RPG Game


import random
import pickle

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = []

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

    def deal_damage(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)
        return damage

class Game:
    def __init__(self):
        self.player = None
        self.locations = {
            "forest": ["enemy", "item", "nothing"],
            "cave": ["enemy", "item"],
            "village": ["rest", "item"]
        }

    def start(self):
        name = input("Enter your hero's name: ")
        self.player = Character(name, 100, 20, 5)
        print(f"Welcome, {self.player.name}! Adventure begins...\n")
        self.main_loop()

    def explore(self):
        location = random.choice(list(self.locations.keys()))
        event = random.choice(self.locations[location])
        print(f"You entered the {location} and encountered {event}!")

        if event == "enemy":
            enemy = Character("Goblin", 50, 10, 2)
            self.combat(enemy)
        elif event == "item":
            item = random.choice(["Sword", "Shield", "Potion"])
            self.player.inventory.append(item)
            print(f"You found a {item}!")
        elif event == "rest":
            self.player.health = 100
            print("You rested and restored your health.")
        else:
            print("Nothing happened...")

    def combat(self, enemy):
        print(f"A wild {enemy.name} appears!")
        while self.player.is_alive() and enemy.is_alive():
            action = input("Do you want to (a)ttack or (r)un? ").lower()
            if action == "a":
                dmg = self.player.deal_damage(enemy)
                print(f"You dealt {dmg} damage to {enemy.name}!")
                if enemy.is_alive():
                    dmg = enemy.deal_damage(self.player)
                    print(f"{enemy.name} dealt {dmg} damage to you!")
            elif action == "r":
                print("You ran away!")
                return
        if self.player.is_alive():
            print(f"You defeated {enemy.name}!")
        else:
            print("You were defeated... Game Over.")
            exit()

    def save_game(self):
        with open("savegame.pkl", "wb") as f:
            pickle.dump(self.player, f)
        print("Game saved!")

    def load_game(self):
        try:
            with open("savegame.pkl", "rb") as f:
                self.player = pickle.load(f)
            print(f"Game loaded! Welcome back, {self.player.name}.")
        except FileNotFoundError:
            print("No saved game found.")

    def main_loop(self):
        while self.player.is_alive():
            choice = input("\nWhat do you want to do? (e)xplore, (s)ave, (l)oad, (q)uit: ").lower()
            if choice == "e":
                self.explore()
            elif choice == "s":
                self.save_game()
            elif choice == "l":
                self.load_game()
            elif choice == "q":
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    game = Game()
    game.start()
