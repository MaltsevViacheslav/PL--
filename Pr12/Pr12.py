# Microsoft Visual Studio Code: microsoft/vscode
import tkinter as tk
import requests
import json

window = tk.Tk()
window.title("GitHub")
window.geometry("280x100")
window.config(bg = "#87CEFA")

vvod = tk.Entry(window, width=30)
vvod.grid(column=0, row=0)

def clicked():
    reposname = vvod.get()
    url = f"https://api.github.com/repos/{reposname}"
    data = requests.get(url).json()

    result = {
        "company": data.get("company"),
        "created_at": data.get("created_at"),
        "email": data.get("email"),
        "id": data.get("id"),
        "name": data.get("name"),
        "url": data.get("url")
    }
    with open("GitHub", "w") as file:
        json.dump(result, file, indent=1)


vivod = tk.Button(window, text = "G", command=clicked)
vivod.grid(column=1, row=0, padx = 10)

window.mainloop()


