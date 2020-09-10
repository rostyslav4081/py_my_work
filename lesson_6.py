# 1) є дві функції
k = bool
def add_to_list(list,item):
    if type(list) == type([]):
        list.append(item)
        k = True
        print(k)
        return len(list)
    else:
        list = create_list()
        list.append(item)
        k = False
        print(k)
        return len(list)

def create_list():
    list =[]
    return list

# 1) треба прямо в функції add_to_list дописати код який буде обробляти помилку якщо передали не ліст і буде запускати іншу функцію
# 2) якщо ніякої помилки не було в глобальну змінну записати True в іншому випадку False
l = []
print(add_to_list(k, 12))
print(add_to_list(l,32))
# Пишемо програму для реїстрації юзерів і їх тел номерів. (Тобто телефонну книгу) Данні які потрібно записувати: - ім'я
# - прізвище
# - тип контакту(напр.дом.ном.тел.або роб.)
# - ном.телефона(може бути декілька)
# Створити меню:
# - створити нового юзера
# - список юзерів
# - видалити юзера
# - змінити телефон
# - вивести всю тел.книгу
# -Записати в файл 10 користувачів
# - Вивести всіх користувачів - вивести користувача з конкретним номером
# - вивести всіх користувачів номер яких містить код 073
class User:
    def __init__(self, name = '---', home_phone = '---', phone = '---', work_phone = '---'):
        self.name = name
        self.home_phone = home_phone
        self.phone = phone
        self.work_phone = work_phone
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
    def find_con(self,phone):
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            file.close()
        for line in lines:
            if phone in line:
                print(line)

    def find_kod(self, kod):
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            file.close()
        for line in lines:
            if kod in line:
                print(line)
    def write_to_file(self):
        with open('users.txt', 'a') as file:
            text = f'Name:{self.name} Home_phone:{self.home_phone} Phone:{self.phone} Work_phone:{self.work_phone}'
            file.writelines(text+'\n')
            file.close()
    def add_phone(self,old_phone,phone):
        global old_line
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            file.close()
        for line in lines:
            if old_phone in line:
                old_line = line
                with open('users.txt', 'a') as wf:
                    wf.writelines(line.replace(f'{self.phone}',phone))
                    self.phone = phone
                    wf.close()
        f = open("users.txt", "r+")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != f'{old_line}':
                f.write(i)
        f.truncate()
        f.close()

    def add_home_phone(self, old_home_phone, phone):
        global old_line
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            file.close()
        for line in lines:
            if 'Home_phone:'+ old_home_phone in line:
                old_line = line
                with open('users.txt', 'a') as wf:
                    wf.writelines(line.replace(f'{self.home_phone}', phone))
                    self.home_phone = phone
                    wf.close()
        f = open("users.txt", "r+")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != f'{old_line}':
                f.write(i)
        f.truncate()
        f.close()
    def add_work_phone(self,old_work_phone,phone):
        global old_line
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            file.close()
        for line in lines:
            if 'Work_phone:' + old_work_phone in line:
                old_line = line
                with open('users.txt', 'a') as wf:
                    wf.writelines(line.replace(f'{self.work_phone}',phone))
                    self.work_phone = phone
                    wf.close()
        f = open("users.txt", "r+")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != f'{old_line}':
                f.write(i)
        f.truncate()
        f.close()
    def del_user(self,name):
        file = open('users.txt', 'r+')
        text = f'Name:{name}'
        d = file.readlines()
        file.seek(0)
        for i in d:
            if i != text:
                file.write(i)
        file.truncate()
        file.close()


user_1 = User('Nona','28760876', '380959875685')
user_1.write_to_file()
print(user_1)
user_1.add_work_phone('---','909874532')
print(user_1)
user_2 = User('Bob', '2628546', '3809847564')
user_2.write_to_file()
user_2.add_phone('3809847564','380976417328')
user_2.add_work_phone('---','0735787856')
user_3 = User('Max','---','0737654843')
user_3.write_to_file()
user_4 = User('Dasha','2396543')
user_4.write_to_file()
user_5 = User('Masha','---','070678543')
user_5.write_to_file()
user_6 = User('Nadia','---','---','0985674321')
user_6.write_to_file()
user_7 = User('Misha','---')
user_7.write_to_file()
user_8 = User('Daryna')
user_8.write_to_file()
user_9 = User('Galyna')
user_9.write_to_file()
user_10 = User('Olex','2624532','097564078')
user_10.write_to_file()
User().del_user('Misha')
find_user = User()
find_user.find_con('070678543')
find_user.find_kod('073')
f = open('users.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()

