# 1)-написать lambda функцию, которая находит среднее арифметическое значение входных аргументов,
# этих входных аргументов может быть сколько угодно
arit = lambda *args: sum(args) // (len(args))
print(arit(2, 2, 11))
# 2)-написать lambda функцию которая принимает строку и возвращает лист слов, при этом каждое слово это лист его букв:
# к примеру:
str_1 = lambda a:[list(i) for i in str(a).split()]
print(str_1("sdfg dfgh fghj rfghj"))
# 3
class Owner:
    def __init__(self, name, age, city, phone_number):
        self.name = name
        self.age = age
        self.city = city
        self.phone_number = phone_number
        self.pets = []

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def add_pet(self, pet_name, pet_age, pet_type,pet_color):
        self.pets.append(Pet(pet_name, pet_age, pet_type, pet_color))

    def show_pets(self):
        for i in range(len(self.pets)):
            for key, value in self.pets[i].__dict__.items():
                print(f'{key}: {value}')
    def show_pet_type(self,type):
        for i in range(len(self.pets)):
            for key, value in self.pets[i].__dict__.items():
                if value == str(type):
                    print(f'{self.pets[i]}')


    def del_pet(self, pet_index):
        del self.pets[pet_index]

class Pet:
    def __init__(self, name, age, animal_type, color):
        self.name = name
        self.age = age
        self.animal_type = animal_type
        self.color = color

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

ower_1 = Owner("Owner_1",12 , "Lviv", "+380987341623")
ower_1.add_pet("Kesha",11, "bird", "blue")
ower_1.show_pets()
ower_1.show_pet_type('bird')
print(ower_1)
# Создаем класс Fighter,
# cоздаем два бойца(экземпляр класса)
# делам формат поединка, каждый из бойцов поочередно наносит друг другу удары забирая случайное число жизни у своего соперника
# в конце выводится победитель
#
# P.S. Случайные числа в пайтоне можно получить импортировав библиотеку random:
# from random import random
#
# random() возращяет число от 0 до 1
class Fighter:
    def __init__(self, name, age, weight, max_hit, life = 100):
        self.name = name
        self.age = age
        self.weight = weight
        self.max_hit = max_hit
        self.life = life





    def hit(self):
        hit = self.max_hit
        self.life = self.life - hit


    def block(self):
        block = self.max_hit//10

        self.life = self.life + block
        if self.life>=100:
            self.life = 100

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
fighter_1 = Fighter("Sasha",25,75,20)
fighter_2 = Fighter("Misha",21,85,22)

print(fighter_1)
print(fighter_2)
fighter_1.hit()
fighter_2.hit()
fighter_1.block()
fighter_2.block()
fighter_2.block()
fighter_1.hit()
fighter_1.hit()
fighter_1.hit()
print(fighter_1)
print(fighter_2)


