#1
from random import randint
size = int(input("Введите размер матрицы: "))
min = 1 
max = 9 
k = int(input("Введите номер строки: "))
A = [] 
print("Начальная матрица:")
for i in range(size): 
    b = []
    for j in range(size):
        b.append(int(randint(min, max))) 
        print(b[j], end=' ') 
    A.append(b)
    print()

def funcm(A, k): 
    dg = A[k-1][k-1]
    for j in range(len(A[k-1])):
        A[k-1][j] /= dg
    return A

print("Изменённая матрица:")
i = funcm(A, k)
for i in range(size): 
    for j in range(size):
        print(A[i][j], end=' ')
    print()

#2
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in m:
    print(i)
print()
n = 3
tm = [] 
for i in range(n):
    tm.append([0] * n) 
for i in range(n):
    for j in range(n):
        tm[j][i] = m[i][j] 
for i in range(len(tm)):
    print(tm[i])
