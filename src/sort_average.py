#
# 7.- Definir una función que dado un array de números me retorne el mayor, el menor y el promedio (usar clase
# para el resultado)
#

class Sort:
    def max_value(self, value):
        max = value[0]
        for number in value:
            if number > max:
                max = number
        return max

    def min_value(self, value):
        min = value[0]
        for number in value:
            if number > min:
                min = number
        return min

    def average_value(self, value):
        return sum(value)/float(len(value))

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

    def is_empty(self, value):
        if len(value) == 0:
            return True
        else:
            return False
