# coding: utf-8

import variables as var
from generic_specie import Generic_specie

class Specie(Generic_specie):
    """
        class for specie (with special caracteristics)
    """

    def __init__(self, number, name, tired, velocity_max, recovery_tired, skill, distance_covered=0, velocity_current=0):
        """
            contructor
        """

        Generic_specie.__init__(self, number, name, tired, velocity_max, recovery_tired, distance_covered=0, velocity_current=0)
        self.skill= skill


    def __str__(self):
        """
            Overload the print method
        """

        return f"N°{self.number} :: {self.name} - skill :: {self.skill} - Vitesse max :: {self.velocity_max}"



    #! staticmethod
    # !def generate_animals(number_animals):
    #  !   """
    #   !      generate as many animals as chosen
    #    ! """
    #    ! for index in range(number_animals):
    #  !       print(index)


    @staticmethod
    def print_message():
        print("\nLes animaux sont les meilleurs !\n")


# check code
if __name__ == "__main__":
    # Specie.print_message()

    # var.animals = [Specie(specie) for specie in var.specie]
    # print(var.animals)

    specie_1 = Specie(1, "nom", 10, 50, 10, "SKILL")
    print(specie_1)