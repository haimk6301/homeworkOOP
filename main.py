from turtle import pd
from model.animal import Animal
from model.employee import Employee
from model.person import Person
from model.rectangle import Rectangle



if __name__ == '__main__':
    person_1 = Person('Haim', 'Kalderon', 61, 'Male', 'hhk@gmail.com', ['dog', 'cat', 'bird'])
    person_2 = Person('Orna', 'Lalo', 51, 'Female', 'orna@gmail.com')
    person_3 = Person('Meir', 'Dali', 56, 'Male', 'meir@gmail.com')
    print(type(person_1))
    print()
    print(type(person_2))
    print()
    print(type(person_3))
    setattr(person_1, 'name', 'Yona')
    print()
    print(getattr(person_1, 'name'))
    person_2.age = 31
    print()
    print(person_2.age)
    animal = Animal('dog', 'milo', 'small','6.3 kg', 14)
    print()
    animal.print_animal()
    person_1.print_person()
    print()
    dog = Animal('dog','chicko', 'medium', 14.5, 7)
    rabit = Animal('rabit','roger','small',3,1 )
    person_2.add_animal(dog)
    print()
    person_1.remove_animal(rabit)
    print()
    person_1.add_animal(rabit)
    print()
    rectangle = Rectangle(4,5)
    area = rectangle.get_area()
    print(f'The area of the rectangle is', area)
    print()
    employee_1 = Employee('Haim', 1990, 14000, 'Nitsana 6')
    employee_2 = Employee('Roni', 1998, 12500, 'Shmaya 7')
    employee_3 = Employee('Ilana', 2002, 16000, 'Hertsel 15')
    print(f' Employee Details Table')
    print(f'\tName \tYear of joining \tSalary \tAddress')
    employee_1.print_employee_table()
    employee_2.print_employee_table()
    employee_3.print_employee_table()
