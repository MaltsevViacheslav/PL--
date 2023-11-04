#1
n = 3
A = [[1, 4, 5], [8, 1, 1], [1, 5, 4]]
s = 0
for i in range(n):
    s += A[0][i]
b = "да, является"
for i in range(n):
    s1 = 0
    s2 = 0
    for j in range(n):
        s1 += A[i][j]
        s2 += A[j][i]
    if s1 != s or s2 != s:
        b = "нет, не является"
        break
print(b)

#2
n = 3
m = 4
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]]
for i in range(n):
    A1 = A[i][0]
    A[i][0] = A[i][m-1]
    A[i][m-1] = A1
for i in range(n):
    for j in range(m):
        print(A[i][j], end = ' ')
    print()