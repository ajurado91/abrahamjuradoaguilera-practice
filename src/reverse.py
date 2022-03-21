#
# 5.- Definir una función inversa() que reciba una cadena y retorne la inversión por ejemplo “AT16 Python”
# y retorne “nohtyP 61TA”
#

class Reverse:
    def to_invert(self, string):
        reverse_string = ""
        for char in string:
            reverse_string = char + reverse_string
        return reverse_string

    def is_only_char(self, string):
        clean_string = string.strip()
        if len(clean_string) == 1:
            return True
        else:
            return False

    def is_empty(self, string):
        clean_string = string.strip()
        if len(clean_string) == 0:
            return True
        else:
            return False