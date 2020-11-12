#coding: utf-8


# import modules
import random

# additional codes
import variables as var

def print_title_rule():
    """
        print the title
        print the game rule
    """

    print("\nLa course des animaux")
    print("---------------------")
    print("")
    print("L'objectif est de faire courir des animaux appartenant à différentes espèces, chaque espèce ayant des caractéristiques et des compétences spécificques.\n")

def ask_nb_animals():
    """
        ask how many animals are going to race
    """

    nb_animals = int(input("Combien d'animaux vont courir ? "))

    return nb_animals


# check code
if __name__ == "__main__":
    var.nb_animals = ask_nb_animals()
    print(var.nb_animals)
    