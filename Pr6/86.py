#1
a = [2, 10, 48, 56, 79, 186]
a1 = 0
a2 = 1
for i in a:
    a1 += i
    a2 *= i
print("Сумма элементов  = ", a1)
print("Произведение элементов  = ", a2)

#2
b = [0, 2, -8, 3.44, 10, 108, 0]
b1 = sum(b)
b2 = sum(b) / len(b)
for i in range(len(b)):
    if b [i] == 0:
       b [i] = b2
print(b)