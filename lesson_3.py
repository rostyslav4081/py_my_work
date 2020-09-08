# - створити функцію яка виводить ліст
def list_maker(*args):
    return  [ i for i in args]
print(list_maker(12, "fghj", 567, "ghjk,"))
# - створити функцію яка приймає три числа та виводить та повертає найменьше.
def min_abc(a=1,b=2,c=3):
    return min(a,b,c)
print(min_abc(3,5,1))
def max_abc(a=3,b=5,c=9):
    return max(a,b,c)
print(max_abc())
def min_max(*args):
    print(max([ i for i in args]))
    return min([ i for i in args])
print(min_max(6,6,9,0,7,29))
def min_l(list_int):
    return min(list_int)
print(min_l([1, 4, -4, 8]))
def max_l(list_int):
    return max(list_int)
print(max_l([1,2,7,0,8,8123,5678]))
def sum_itemList(list):
    sum=0
    for i in list:
        sum+=i
    return sum
print(sum_itemList([1,2,7,0,8,8123,5678]))
def list_ar(list):
     return  sum_itemList(list)//len(list)


print(list_ar([2,2,6,10 ]))
def l_st(list_1,list_2):
    list_3=[]
    if len(list_1)==len(list_2):
        for i in list_1:
            for j in list_2:
                list_3.append(i+j)

    return list_3[::(len(list_1)+1)]



print(l_st([1, 2, 3, 5, 6,-6], [-1, 2, 5, 9, 0, 6]))
def dec(func):
    def wrap():
        print("_____")
        print(str(func()).replace("_"," "))
        print("________")
    return wrap
@dec
def pr(): return ( 'Hello_boss_!!!')
pr()
# Практична:
#
# Імітуємо роботу банкомату
# Є рахунок та дії над ним
# 1. Етап логінації - ввести логін + пароль
# 2 Меню :  (кожен пункт меню це функція)
# 1) Подивитись стан рахунку : виводить стан рахунку
# 2) Зняти кошти (ввести кількість коштів, + дивитись над тим щоб не залазити в борг)
# 3) покласти кошти (ви вводите скільки коштів потрібно покласти)
# 4) вихід

data = [["login_1","pass_1",100],["login_2","pass_2",200]]
login = input("Ведіть свійй логін:")
password = input("Ведіть свій пароль:")
balance = 0
def balance(d):
    for i in d:
        return i[2]
def put(money):
    for i in data:
        i[2]=i[2] + money
        print("Тепер у Вас на балансі:",i[2])
        return i[2]
def take(money):
    for i in data:
        if  login and  password in i:
            if i[2]<money:
                print("Замало на рахунку:")
            else:
                if i[2]>0:
                    i[2]=i[2] - money
                    return i[2]
                else :
                    print("Спробуйте зняти меншу суму:")

def login(l,p):
    for i in data:
        if l and p in i:
            print("Особу підтверджено:")
            while True:
                print("1.Подивитися стан рахунку:")
                print("2.Зняти кошти:")
                print("3.Покласти кошти на рахунок")
                print("4.Вихід з мінібанкомату_терміналу):")
                a = int(input("Зробіть свій вибір:"))
                if a == 1:
                    print("Ваш баланс:", balance(data))
                elif a == 2:
                    t = int(input("Ведіть суму зняття:"))
                    take(t)
                elif a == 3:
                     p =int(input("Ведіть суму,щоб покласти на рахунок:"))
                     put(p)
                elif a == 4:
                     print("Чекаємо на Вас знетерпінням:")
                     exit()



        else:
            print("Спробуйте ще раз залогінитися:")
            return
login(login,password)



