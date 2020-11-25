# coding: utf-8

class Generic_specie:
    """
        generic class for specie (same caracteristics between all the species)
    """

    def __init__(self, number, name, tired, velocity_max, recovery_tired, distance_covered=0, velocity_current=0):
        """
            contructor
        """

        self.number = number
        self.name = name 
        self.tired = tired
        self.velocity_max = velocity_max
        self.velocity_current = velocity_current
        self.recovery_tired = recovery_tired
        self.distance_covered = distance_covered


    def relax(self):
        """
            animal relaxs
        """
        pass


    def move(self):
        """
            animal moves
        """
        pass

    #! staticmethod
    # !def generate_animals(number_animals):
    #  !   """
    #   !      generate as many animals as chosen
    #    ! """
    #    ! for index in range(number_animals):
    #  !       print(index)


    def __str__(self):
        """
            Overload the print method
        """

        return f"N°{self.number} :: {self.name} - Fatigue :: {self.tired} - Vitesse max :: {self.velocity_max}"



# check code
if __name__ == "__main__":
    specie_1 = Generic_specie(1, "nom", 10, 50, 10)
    # print(specie_1)
    # Generic_specie.generate_animals(6)
    print(specie_1)
