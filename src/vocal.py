#
# 4.- Definir una función isVocal () que tome como argumento un carácter y diga si es vocal, consonante o numero
#

class Vocal:
    def is_vocal(self, char):
        char_clean = char
        vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        if char_clean in vocals:
            return True
        else:
            return False

    def is_consonant(self, char):
        char_clean = char
        vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        if char_clean in vocals:
            return False
        else:
            return True

    def is_number(self, char):
        char_clean = char
        if isinstance(char_clean, int):
            return True
        else:
            return False

    def is_empty(self, char):
        if len(char) == 0:
            return True
        else:
            return False