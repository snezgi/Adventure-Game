import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(enemy):
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + enemy + " is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("To your right is a dark cave. ")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.")


def fight(items, enemy):
    # Things that happen when the player fights
    if "dagger" in items:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the" + enemy + ".")
        print_pause("You have been defeated!")
        print_pause("Would you like to play again? (y/n)")
        again = input()
        while again != 'y' and again != 'n':
            print_pause("(Please enter y or n.)")
            again = input("y  play again\n"
                          "n  exit game \n")
        if again == 'y':
            play_game()
        elif again == 'n':
            print_pause("Goodbye!")
    else:
        print_pause("As the " + enemy + " moves to attack,"
                    " you unsheath your new sword."
                    "The Sword of Ogoroth shines brightly in your hand"
                    " as you brace yourself for the attack. ")
        print_pause("But the " + enemy + " takes one look at "
                    "your shiny new toy and runs away!")
        print_pause("You have rid the town of the" + enemy + ". "
                    "You are victorious!")
        print_pause("Would you like to play again? (y/n)")
        again = input()
        while again != 'y' and again != 'n':
            print_pause("(Please enter y or n.)")
            again = input("y  play again\n"
                          "n  exit game \n")
        if again == 'y':
            play_game()
        elif again == 'n':
            print_pause("Goodbye!")


def cave(items, enemy):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")

    if "sword" in items:
        print_pause("You already found the sword here, "
                    "so there is nothing "
                    "more to do here now.")
    else:
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    " and take the sword with you.")
        items.append("sword")
        items.remove("dagger")
    print_pause("You walk back out to the field.")
    field(items, enemy)


def house(items, enemy):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens"
                " and out steps a " + enemy + ". "
                "Eep! This is the " + enemy + "'s house!")
    print_pause("The " + enemy + " attacks you!")
    if "dagger" in items:
        print_pause("You feel under-prepared for this, "
                    "with your tiny dagger.")
    print_pause("Would you like to (1) fight or (2) run away?")
    print_pause("(Please enter 1 or 2.)")
    fightorflight = input("1. FIGHT!\n"
                          "2. RUN AWAY!\n")
    while fightorflight != '1' and fightorflight != '2':
        print_pause("(Please enter 1 or 2.)")
        fightorflight = input("1. FIGHT!\n"
                              "2. RUN AWAY!\n")
    if fightorflight == '1':
        fight(items, enemy)
    elif fightorflight == '2':
        print_pause("You run back into the field."
                    " Luckily, you don't seem to have been followed.")
        field(items, enemy)


def field(items, enemy):
    print_pause("Enter 1 to knock on the door of the house. "
                "Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    print_pause("(Please enter 1 or 2.)")
    doororcave = input("1. knock on the door\n"
                       "2. wonder into the cave\n")
    while doororcave != '1' and doororcave != '2':
        print_pause("(Please enter 1 or 2.)")
        doororcave = input("1. knock on the door\n"
                           "2. wonder into the cave\n")
    if doororcave == '1':
        house(items, enemy)
    elif doororcave == '2':
        cave(items, enemy)


def play_game():
    items = ["dagger"]
    enemies = ["pirate", "troll", "dragon", "evil witch"]
    enemy = random.choice(enemies)
    intro(enemy)
    field(items, enemy)


play_game()
