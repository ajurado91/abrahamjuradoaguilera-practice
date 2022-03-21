#
# 10 Definir una función que cuente la cantidad de caracteres que tiene una cadena
#

class Long:
    def long_string(self, string):
        if string.isspace():
            return True
        if string == "":
            return 0
        else:
            return len(string)
