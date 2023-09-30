n = int(input("Введите число: "))
a, b, c = 0, 0, 1
while c<n:
    b, c = c, b + c
s = a + b + c
print(s)