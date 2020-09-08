while True:
    list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print("1.Знайти min у лісті:")
    print("2.Видалити всі одинакові значення")
    print("3.Замінити кожен 4_ий елемент на (X)")
    print("4.Вивести елемент ліста значення ,якого найблище до середнього арифметичного значення ліста")
    print("5.Вивести на екран пустий квадрат з зірочками")
    print("6.Вивести табличку множення:")
    print("7.Вийти з програми) кінець роботи)")
    a = int(input("Зробіть свій вибір:"))
    if a == 1:
        print("Мінімальне значення:", min(list))
    elif a == 2:
        new_list = []
        for i in list:
            if i not in new_list:
                new_list.append(i)
        print("Без однакових значень:",new_list)
    elif a == 3:
        for i in range(len(list)):
            if list.index(list[i])%4==0 :
                list[i] = "X"
        print("Кожен 4_ий елемент (X):",list)
    elif a == 4:
        sum = 0
        for i in list:
            sum+=i
        print("Сума чисел ліста:",sum)
        ar=sum/len(list)
        print("Cереднє арифметичне:",ar)
        print("Найблищий елемент ліста до середнього арифметичного:",min(list, key=lambda x: abs(ar - x)))
    elif a == 5:
        n=int(input("Задай довжину квадрату:"))
        for i in range(n):
            for j in range(n):
                if(i==0 or j==0 or i==n-1 or j==n-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif a == 6:
        for i in range(1, 10):
            for j in range(1, 10):
                print("%4d" % (i * j), end='')
            print()
    elif a == 7:
        exit()
    elif a not in range(1,8):
        print("Помилка)Спробуйте від 1 до 7 вказати число)")



