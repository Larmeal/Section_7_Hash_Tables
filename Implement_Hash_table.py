
class HashTable:

    def __init__(self):
        self.dict = {}
        self.keys_list = []
        self.values_list = []

    def set(self, key, value):
        self.dict[f"{key.lower()}"] = value
        return self.dict

    def get(self, key):
        self.overcome = self.dict[f"{key.lower()}"]
        return self.overcome

    def keys(self):
        for key in self.dict:
            self.keys_list.append(key)
        return self.keys_list
    
    def values(self):
        for value in self.dict:
            self.values_list.append(self.dict[value])
        return self.values_list

data_1 = HashTable()
print(data_1.set("game", 4))
print(data_1.set("day", 2))
print(data_1.keys())
print(data_1.values())
