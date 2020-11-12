# coding: utf-8

class Animal:
    """
        class for animal
    """

    def __init__(self, number, name, tired, elocity_max, velocity_current, recovery_tired, distance_covered, skill):
        """
            contructor
        """

        self.number = number
        self.name = name 
        self.tired = tired
        self.velocity_max = elocity_max
        self.velocity_current = velocity_current
        self.recovery_tired = recovery_tired
        self.distance_covered = distance_covered
        self.skill= skill

    @staticmethod
    def print_message():
        print("\nLes animaux sont les meilleurs !\n")


# check code
if __name__ == "__main__":
    Animal.print_message()