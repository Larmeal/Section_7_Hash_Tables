list = "Hello"
code = []
convert = []

class Convert:

    def __init__(self):
        self.convert_int = []
        self.convert_str = []

    def int(self, letter):
        for i in letter:
            self.convert_int.append(ord(i))
        return self.convert_int
    
    def str(self, number):
        for i in number:
            self.convert_str.append(chr(i))
        
        self.merge(self.convert_str)
        return self.word

    def merge(self, convert_str):
        self.word = "".join(convert_str)
        return self.word

game = [103, 97, 109, 101]
print(Convert().int("game"))
print(Convert().str(game))
