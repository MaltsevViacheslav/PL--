#1
a = [1, 2, 3, 4, 4, 5, 5, 6, 7]
b = [i for i in set(a) if a.count(i) > 1]
if len(b) == 0:
    print("Повторяющихся элементов нет")
else:
    print(b)

#2
a = [1, 2, 3, 4, 5, 10, 11, 12, 14, 20, 21, 22, 23, 24, 25]
print("Первоначальный массив", a)
print("Преобразованный массив", [0 if i < 10 else 1 if i > 20 else i for i in a])