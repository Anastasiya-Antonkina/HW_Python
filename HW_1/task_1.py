#Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) 

a = input("Введите трехзначное число ")
a = int(a)
b = a % 10
a = a // 10
c = a % 10
a = a // 10

print ("Сумма цифр равна: ", a + b + c) 
