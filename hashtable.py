class hash:
    def __init__(self):
        self.table = [None] * 23

    def get_hash(self, key):
        # my_hash = (my_hash + ord(letter) * 13) % len(7)
        h = 0
        i = 1
        j = len(key)
        a = 7
        b = 11
        for char in key:
            h += (h * a + ord(char) * b * i)
            i += 1
        index = h % 23
        return index

    def add(self, key, edad):
        index = self.get_hash(key)
        if self.table[index] is None:
            self.table[index] = edad
            return True
        else:
            print("Colision...")
            return False
    def search(self,key):
        index = self.get_hash(key)
        if self.table[index] is None:
            print("No existe el Elemento ingresado")
            return False
        else:
            print(f"La edad de {key} es de : {self.table[index]}")
            return self.table[index]
    def remove(self,key):
        index = self.get_hash(key)
        if self.table is None:
            print("No hay elemento para borrar")
        else:
            print("Eliminando elemento...")
            self.table[index] = None


h = hash()

print(h.get_hash("mario"))
print(h.get_hash("mauricio"))
print(h.get_hash("fernanda"))
print(h.get_hash("gael"))
print(h.get_hash("rafael"))
print(h.get_hash("julian"))
print(h.get_hash("samantha"))
print(h.get_hash("leag"))
print(h.get_hash("oiram"))
print(h.get_hash("adnanref"))
print(h.get_hash("leafar"))
print(h.get_hash("nailuj"))
print(h.get_hash("oiciruam"))
print(h.get_hash("ahtnamas"))

print(h.add("mauricio", 19))
h.search("mauricio")
h.remove("mauricio")
h.search("mauricio")

