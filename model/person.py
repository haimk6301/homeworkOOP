from model.animal import Animal


class Person:

    def __init__(self, name, surname, age, gender, mail, owned_animals=[]):
        self.__name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.mail = mail
        self.owned_animals = owned_animals
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def print_person(self):
        print(f'name: {self.__name}, size: {self.surname},'
              f' weight: {self.age}, age: {self.gender}, nickname: {self.mail},owned animals {self.owned_animals}')

    def add_animal(self, animal):
        if animal is not self.owned_animals:
            self.owned_animals.append(animal)
            print(f'new animal has been added to {self.name} owned pets')
        else:
            print(f'this animal already exists in {self.name} owned pets')

    def remove_animal(self, animal_kind):
        if animal_kind in self.owned_animals:
            self.owned_animals.remove(animal_kind)
            print(f'animal has been removed from {self.name} owned pets')
        else:
            print(f'this animal does not exists in {self.name} owned pets')


