# coding:utf-8

from number import Convert_number

class Converter():

    @staticmethod
    def ask_which_converter():

        print("\n----------------------------------------------------------------------")
        print("   Convertisseur de chiffre arabe en chiffre romain, et inversement.")
        print("----------------------------------------------------------------------")
        print()

        converter_choice = (input("Tape 'R' si tu veux obtenir un nombre romain (à partir d'un nombre arabe)\n ou 'A' si tu veux obtenir un nombre arabe (à partir d'un nombre romain) : ")).upper()

    
        if converter_choice == "R":
            arabic = int(input("Entre un nombre arabe supérieur à 0 : "))
            print(f"{arabic} en nombre arabe devient {Convert_number.arabic_to_roman(arabic)} en nombre romain.\n")
        elif converter_choice == "A" :
            roman = input("Entre un nombre romain : ")
            print(f'{roman} en nombre romain devient {Convert_number.roman_to_arabic(roman)} en nombre arabe.\n')
            print()


# test point
if __name__ == "__main__":
    Converter.ask_which_converter() 