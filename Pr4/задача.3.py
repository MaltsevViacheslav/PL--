a = int(input("Введите число: "))
b = int(input("Введите число: "))
if a>b:
    for i in range(a - (a+1) % 2, b-1, -2):
        print(i)
else:
    print("Числа не соответствуют условию")