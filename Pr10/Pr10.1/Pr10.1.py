file1 = open("Мальцев В. М._УБ-32_vvod1.txt")
file2 = open("Мальцев В. М._УБ-32_vivod1.txt", "w", encoding= "utf-8")

tm = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
m = []
for i in file1:
    list = []
    for j in i.strip().split():
        list.append(int(j))
    m.append(list)
file2.write("Начальная матрица:\n")
file2.write(str(m))

for i in range(3):
    for j in range(3):
        tm[j][i] = m[i][j]
file2.write("\nИзменённая матрица:\n")
file2.write(str(tm))
file1.close()
file2.close()