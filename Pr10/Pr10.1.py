#Часть1
from random import randint
file1 = open("Мальцев В. М._УБ-32_vvod.txt")
size = int(next(file1))
min = 1
max = 9
k = int(next(file1))
A = []
file2 = open("Мальцев В. М._УБ-32_vivod.txt", "w", encoding= "utf-8")
for i in range(size):
    b = []
    for j in range(size):
        b.append(int(randint(min, max)))
    A.append(b)
file2.write("Часть 1\nНачальная матрица:\n")
file2.write(str(A))
def funcm(A, k):
    dg = A[k-1][k-1]
    for j in range(len(A[k-1])):
        A[k-1][j] /= dg
    return A

i = funcm(A, k)
file2.write("\nИзменённая матрица:\n")
file2.write(str(A))

#Часть2
n = int(next(file1))
m = str(next(file1))
tm = []
file2.write("\nЧасть 2\n")
file2.write(m)
m = m.split(';')
m = [i.split() for i in m]
for i in range(n):
    tm.append([0] * n)
for i in range(n):
    for j in range(n):
        tm[j][i] = m[i][j]
file2.write("\nИзменённая матрица:\n")
file2.write(str(tm))