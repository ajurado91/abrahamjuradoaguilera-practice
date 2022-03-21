#
# 3 Definir una función max () que tome como argumentos tres números y devuelva le mayor de ellos
#

class Max:
    def max_value(self, value):
        max = value[0]
        for number in value:
            if number > max:
                max = number
        return max

    def equal_value(self, value):
        equal = value[0]
        counter = 0
        for number in value:
            if number == equal:
                counter += 1
        if counter == len(value):
            return True
        else:
            return False

    def nan_value(self, value):
        counter = 0
        for number in value:
            if isinstance(number, str):
                counter += 1
        if counter > 0:
            return True
        else:
            return False
