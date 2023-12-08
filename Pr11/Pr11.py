import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

window = tk.Tk()
window.title("Мальцев Вячеслав Максимович")
window.geometry("645x415")
window.config(bg = "#87CEFA")

nb = ttk.Notebook(window)
nb.pack()
tab1 = ttk.Frame(nb)
nb.add(tab1, text="Калькулятор")

number1 = tk.Entry(tab1, width = 8)
number1.grid(column=0, row=0, padx=10, pady=10)

action = Combobox(tab1, width = 8)
action["values"] = ("+", "-", "*", "/")
action.current(0)
action.grid(column=1, row=0, padx = 5, pady = 10)

number2 = tk.Entry(tab1, width = 8)
number2.grid(column=2, row=0, padx = 5, pady = 10)

result = tk.Entry(tab1, width = 8)
result.grid(column=4, row=0, padx = 5, pady = 10)
def clicked1():
    num1 = int(number1.get())
    num2 = int(number2.get())
    act = action.get()
    if act == "+":
        result1 = num1 + num2
    elif act == "-":
        result1 = num1 - num2
    elif act == "*":
        result1 = num1 * num2
    elif act == "/":
        result1 = num1 / num2
    result.delete(0, tk.END)
    result.insert(0, str(result1))

ravno = tk.Button(tab1, text = "=", command=clicked1)
ravno.grid(column=3, row=0)


tab2 = ttk.Frame(nb)
nb.add(tab2, text="Выбор")
ch1 = tk.IntVar()
ch2 = tk.IntVar()
ch3 = tk.IntVar()
chec1 = tk.Checkbutton(tab2, text="Первый", variable=ch1)
chec2 = tk.Checkbutton(tab2, text="Второй", variable=ch2)
chec3 = tk.Checkbutton(tab2, text="Третий", variable=ch3)
chec1.grid(column=0, row=0, padx=5, pady=10)
chec2.grid(column=1, row=0, padx=5, pady=10)
chec3.grid(column=2, row=0, padx=5, pady=10)

def clicked2():
    result2 = []
    if ch1.get() == 1:
       result2.append("первый")
    elif ch2.get() == 1:
        result2.append("второй")
    elif ch3.get() == 1:
        result2.append("третий")
    messagebox.showinfo("Итог", "Вы выбрали " + "".join(result2) + " вариант")
choise = tk.Button(tab2, text="Нажми!!", command=clicked2)
choise.grid(column=3, row=0)

tab3 = ttk.Frame(nb)
nb.add(tab3, text="Текст")

mn = tk.Menu(window)
window.config(menu=mn)

def clicked3():
    road = filedialog.askopenfilename()
    f = open(road, "r", encoding="UTF-8")
    txt.insert(tk.END, f.read())

f = tk.Menu(mn)
mn.add_cascade(label="Файл", menu=f)
f.add_command(label="Выберите файл", command=clicked3)

txt = tk.Text(tab3, wrap="word")
txt.grid()

window.mainloop()
