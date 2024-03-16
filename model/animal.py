class Animal:

    def __init__(self, kind, name, size, weight, age):
        self.kind = kind
        self.name = name
        self.size = size
        self.weight = weight
        self.age = age


    def print_animal(self):
        print(f'pet kind: {self.kind}, name: {self.name}, size: {self.size}, weight: {self.weight}, age: {self.age}')