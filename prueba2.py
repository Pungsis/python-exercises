class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):
    def perro(self):
        return self.items_list


amigos = MappingSubclass("perro")

print(amigos.update([amigos]))
