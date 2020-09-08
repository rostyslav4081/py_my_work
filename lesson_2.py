input_str =str_3 =str(input("Input new string:"))
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
new_str=''
for i in input_str:
    if i in ('1','2','3','4','5','6','7','8','9','0'):
       new_str+=f'{i},'
print(new_str .rstrip(','))
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
for i in range(len(input_str)):
    if input_str[i] not in ('1','2','3','4','5','6','7','8','9','0'):
       input_str=input_str.replace(f'{input_str[i]}', ' ')
new_str_1=''
for i in input_str.split():
    new_str_1+=f'{i},'
print(new_str_1 .rstrip(','))
# 3)прога, що виводить кількість кожного символа з введеної строки,
# наприклад:
# st = 'as 23 fdfdg544' #введена строка
#
# 'a' -> 1  #вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
# """
str_3_1=''
for i in str_3:
    if i not in str_3_1:
        str_3_1+=f'{i}'
        if i in str_3_1:
            print(f"'{i}' -> {str_3.count(f'{i}')}")
greeting = 'Hello, world'
print([i for i in greeting.upper()])
print([i*i for i in range(0,50) if i%2==1])
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
num=''
for i in range(len(numbers)):
    if numbers[i]<=4:
        num+=' LT '
    else:
        num+=' GT '
print(num.split())
list1 = [1, 2, 3, 4, 5]
list2 = [-1, 7, 10, -5, -2]
print([(i,-i) for i in list1 for k in list2 if i==-k])
# Нужно проверить, все ли числа в листе уникальны.
# лист нужно сделать со строки полученной с помощью input()
# пример "1, 2, 3, 4, 5" -> [1,2,3,4,5]
# [1, 2, 3, 4, 5] -> True
# [1, 2, 3, 4, 3] -> False
# ввести строчку с input() и вывести самое длинное и повторяющееся слово
# пример:
#"python the best of the best programming language, because is python"
#Вывод: python
l_1=[]
k=str(input("Enter value:"))
for i in k:
    if i in  ('1','2','3','4','5','6','7','8','9','0') :
        l_1.append(int(i))
l_1_0=set(l_1)
if len(l_1)==len(l_1_0):
    print(l_1, " -> True")
else:
    print(l_1, " -> False")
s=str(input("Enter string:"))
l_s=[]
for i in s.split():
    if s.count(i)>1:
        l_s.append(i)
print(max([i for i in l_s], key=len))

