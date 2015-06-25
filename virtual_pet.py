import random
import sys
import time

COLORS = ['purple', 'red', 'blue', 'orange']

class Animal(object):

    start = time.time()
    now = time.time()
    health = 10
    experience = 0
    happy = 10
    attack = 0
    sound = "gurbl"

    def minute(self):
        self.health -= 1
        self.happy -= 1
        self.attack += 1
        self.experience += 1
        if self.will_attack():
            print "You're pet has mauled you!"
            print "Game Over"
            sys.exit()

    def speak(self):
        return self.sound().upper()

    def will_attack(self):
        roll = random.randint(1, self.attack)
        if self.type == 'snake' or self.type == 'aligator':
            roll += 2
        elif self.type == 'bear':
            roll += 1
        return roll > 5

    def get_pet(self):
        pet_choice = raw_input("Choose baby pet ([S]nake, [A]ligator, [B]ear): ").lower()
        print pet_choice
        if pet_choice in 'sab':
            if pet_choice == 's':
                return 'snake'
            elif pet_choice == 'a':
                return 'aligator'
            else:
                return 'bear'
        else:
            self.get_pet()

    def __init__(self):
        self.name = raw_input("Name: ")
        self.color = random.choice(COLORS)
        self.type = self.get_pet()


class Snake(Animal):
    attack = 1
    sound = "hisssss"


class Bear(Animal):
    attack = 2
    sound = "growl"


class Aligator(Animal):
    attack = 3
    sound = "snap"

def menu():
    choice = raw_input("Choose action ([F]eed, [P]lay, [W]alk or [I]gnore): ").lower()
    if choice in "fpwi":
        pass
    else:
        return self.menu()

def main():
    new_pet = Animal()
    while new_pet.health > 0:
        new_pet.now = time.time()
        if new_pet.now - new_pet.start >= 10.0:
            new_pet.minute()
            print "\n" * 20
            print "{} is still {}. It's health is {}, experience is {}, happiness is {} and attack is {}.".format(new_pet.name, new_pet.color, new_pet.health, new_pet.experience, new_pet.happy, new_pet.attack)
            new_pet.start = time.time()
        else:
            menu()


if __name__ == '__main__':
    main()

