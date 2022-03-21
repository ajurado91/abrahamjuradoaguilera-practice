#
# 9.- Definir un método que ingresado un numero devuelva su binario
#

class Binary:
    def convert(self, decimal):
        if decimal <= 0:
            return "0"
        binary = ""
        while decimal > 0:
            remainder = int(decimal % 2)
            decimal = int(decimal / 2)
            binary = str(remainder) + binary
        return binary

    def nan_binary(self, value):
        counter = 0
        for number in value:
            if isinstance(number, str):
                counter += 1
        if counter > 0:
            return True
        else:
            return False

    def is_empty(self, value):
        if len(value) == 0:
            return True
        else:
            return False
