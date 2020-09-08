# Створити клас rectangle
# 1) об'єкт приймає два параметри - дві сторони х у
# 2) описати методи арифметичні
#   + сума площин двок об'єктів
#   - різниця площин
# 3) логічні оператори:
#   == повертає true якщо рівні по площині
#   != якщо не рівні
#   >, < відповідно
# 4) len() - сума сторін
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.area = a*b
    def __add__(self, other):
        return self.area + other.area
    def __sub__(self, other):
        return self.area - other.area
    def __lt__(self, other):
        return self.area < other.area
    def __eq__(self, other):
        return self.area == other.area
    def __lt__(self, other):
        return self.area < other.area
    def __gt__(self, other):
        return self.area > other.area
    def __le__(self, other):
        return self.area <= other.area
    def __ge__(self, other):
        return self.area >= other.area
    def __ne__(self, other):
        return self.area != other.area
    def __eq__(self, other):
        return self.area == other.area
    def __len__(self):
        return self.a + self.b

rectangle_1 = Rectangle(5,9)
rectangle_2 = Rectangle(7,15)
print(rectangle_1 + rectangle_2)
print(rectangle_2 - rectangle_1)
print(rectangle_2 >= rectangle_1)
print(rectangle_2 <= rectangle_1)
print(rectangle_2 == rectangle_1)
print(rectangle_2 != rectangle_1)
print(len(rectangle_1))
# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text
list=[]
class Letter:
    def __init__(self):
        self.__count = 0
        self.__text = str(' ')
    def set_text(self,value):
        self.__count +=1
        self.__text = str(value)
    def get_text(self):
        return self.__text
    def del_text(self):
        self.__count -=1
        del self.__text
    def print_count(self):
        print(f'{self.__count}')
    def text_add_to_list(self,l=[]):
        return l.append(self.__text)
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
text_1 = Letter()
text_1.set_text('text_1')
print(text_1.get_text())
text_1.print_count()
text_1.text_add_to_list(list)
print(list)
# 1) написати програму для запису відомостей про пасажирські перевезення
# 2) перевезення відбувається трьома способами, літаком, машиною, поїздом,
# 3) дані які треба буде зберігати:
#   - вартість квитка(літак, поїзд)
#   - кількість пасажирів(машина)
#   - час в дорозі(всі)
#   - час реєстрації(літак)
#   - клас:перший,другий(літак)
#   - вартість пального(машина)
#   - км(машина)
#   - місце: купе,св(поїзд)
# 4) методи:
#   - розрахунок вартості доїзду(машина)
#   - загальний час перельоту(літак)
#   - порівняти час в дорозі між двома будь якими транспортними засобами(двома об'єктами) - наприклад"літак на 5 годин швидше за поїзд"
#   - вивести всі дані про перевезення(поїзд)
class Trip:
    def __init__(self, price, time, name_passenger):
        self.price = price
        self.time = time
        self.name_passenger = name_passenger
        self.__data = {"name":name_passenger, "time":time, "price":price}
    def get_data(self):
        return self.__data
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
class Plane(Trip):
    def __init__(self, price, time, name_passenger, time_registration):
        super().__init__(price, time, name_passenger)
        self.time_registation = time_registration

