

class Convert_number():
    """
        class to get number (arabic or roman) from the user
    """

    equal_roman_arabic_number = {
        'M' : 1000,
        'CM':  900,
        'D' :  500,
        'CD':  400,
        'C' :  100,
        'XC':   90,
        'L' :   50,
        'XL':   40,
        'X' :   10,
        'IX':    9,
        'V' :    5,
        'IV':    4,
        'I' :    1
    }


    @staticmethod
    def arabic_to_roman(arabic_number):
        """
            convert arabic number to roman number
        """

        print("\nConvertisseur de nombre arabe en nombre romain")
        print("----------------------------------------------")

        roman_number = ""

        for roman_nb, arabic_nb in (Convert_number.equal_roman_arabic_number.items()):
            while arabic_number >= arabic_nb:
                arabic_number -= arabic_nb
                roman_number += roman_nb

        return roman_number


    @staticmethod
    def roman_to_arabic(roman_number):
        """
            convert roman number to arabic number
        """
        
        print("\nConvertisseur de nombre romain en nombre arabe")
        print("----------------------------------------------")
        
        arabic_number = 0

        while roman_number != "":
            for roman_nb, arabic_nb in (Convert_number.equal_roman_arabic_number.items()):
                if roman_number.startswith(roman_nb):
                    arabic_number += arabic_nb
                    roman_number = roman_number[len(roman_nb):]
        
        return arabic_number




# test point
if __name__ == "__main__":
    print(Convert_number.arabic_to_roman(3))
    
    print(Convert_number.roman_to_arabic("XVI"))