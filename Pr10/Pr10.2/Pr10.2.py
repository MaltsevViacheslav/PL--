file1 = open("Мальцев В. М._УБ-32_vvod2.txt")
file2 = open("Мальцев В. М._УБ-32_vivod2.txt", "w", encoding= "utf-8")
A = []
for i in file1:
    list= []
    for j in i.strip().split():
        list.append(int(j))
    A.append(list)
n = 3
s = 0
for j in range(n):
    s += A[0][j]
for i in range(n):
    s1 = 0
    s2 = 0
    for j in range(n):
        s1 += A[i][j]
        s2 += A[i][j]
if s1 != s or s2 != s:
    file2.write("Нет, не является")
else:
    file2.write("Да, является")
file1.close()
file2.close()
