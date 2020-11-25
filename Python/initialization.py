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

    nb_animals = int(input("Combien d'animaux vont courir ?"))
    
    while nb_animals < 2 or nb_animals > 10:
        print("Merci de choisir un nombre entre 2 et 10.")
        nb_animals = int(input("Combien d'animaux vont courir ? "))

    return nb_animals


def ask_lenght_race():
    """
        ask how many meters is the race
    """
    lenght_race = int(input("Quelle est la longueur de la course ?"))

    while lenght_race < 100 or lenght_race > 5000:
        print("Merci de choisir un nombre entre 100 et 5000.")
        lenght_race = int(input("Quelle est la longueur de la course ?"))

    return lenght_race

def show_species():
    """
        show all species characteristics
    """

    for specie in var.specie:
        for caract in var.specie[specie]:
            caract = var.specie[specie][caract]
            print(caract)
    



# check code
if __name__ == "__main__":
    # var.nb_animals = ask_nb_animals()
    # print(var.nb_animals)
    # var.lenght_race = ask_lenght_race()
    # print(var.lenght_race)
    # show_species()
    # print(var.specie['Porc-épic']['name_specie'])
        
    