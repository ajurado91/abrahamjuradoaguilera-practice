#
# 8.- Definir una función que tome una lista de nombres de países y que devuelva el país mas largo es decir
# con mayor números de caracteres.
#

class Countries:
    def sort(self, countries):
        count = 0
        position = 0
        iterate = 0
        for num in countries:
            if len(num) > count:
                count = len(num)
                position = iterate
            iterate = iterate + 1
        return (countries[position])

    def only_one(self, countries):
        if len(countries) == 1:
            return True
        else:
            return False

    def is_empty(self, countries):
        if len(countries) == 0:
            return True
        else:
            return False
