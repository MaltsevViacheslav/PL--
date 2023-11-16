#1
def func1(i):
    a = i
    while(a):
        b = a % 10
        a //= 10
        if (b == 0 or i % b):
            return False
    return True
n = int(input("Введите число: "))
for i in range(1, n + 1):
    if (func1(i)):
        print(i)
#2
def func2(A):
    A[0], A[-1] = A[-1], A[0]
    return A

m = int(input("Длина массива равна: "))
A = list(map(int, input("Введите элементы массива: ").split(maxsplit = (m - 1))))
print("Исходный массив", A)
print("Изменённый массив", func2(A))
