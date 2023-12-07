file1 = open("Мальцев В. М._УБ-32_vvod3.txt")
file2 = open("Мальцев В. М._УБ-32_vivod3.txt", "w", encoding= "utf-8")
n = 3
m = 4
A = []
for i in file1:
    elem = []
    for j in i.strip().split():
        elem.append(int(j))
    A.append(elem)
for i in range(n):
    A1 = A[i][0]
    A[i][0] = A[i][m-1]
    A[i][m-1] = A1
file2.write(str(A))
file1.close()
file2.close()


