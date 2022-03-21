#
# 6.- Definir una función que determine si un texto ingresado es palíndromo
#

class Palindrome:
    def check(self, string):
        clean_string = string.strip()
        start = 0
        end = len(clean_string) - 1
        while clean_string[start] == clean_string[end]:
            if start >= end:
                return True
            start += 1
            end -= 1
        return False

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

