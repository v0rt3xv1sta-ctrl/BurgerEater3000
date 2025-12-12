# Burger Eater 3000
# Copyright (C) 2025 Jasper Gulka
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.


import tkinter as tk
import time
import threading

bur = 0
has_bot = False

window = tk.Tk()

window.title("Burger Eater 3000")

cout = tk.Label(window, text=f"Burger:{bur}")
cout.pack(pady=20)

def eat():
    global bur
    bur += 1

    cout.config(text=f"Burger:{bur}")

def bot_worker():
    global bur
    while has_bot:
        time.sleep(1)
        bur += 1
        cout.config(text=f"Burger:{bur}")

def getbot1():
    global bur, has_bot
    if bur >= 20:
        has_bot = True
        threading.Thread(target=bot_worker, daemon=True).start()
        bur -= 20
        cout.config(text=f"Burger:{bur}")
    else:
        cout.config(text="you dont have enough for this")


but = tk.Button(window, text="Eat Burger", command=eat)
but.pack(pady=20)

bot = tk.Button(window, text="unlock bot (20 Burgers)", command=getbot1)
bot.pack(pady=20)

window.mainloop()
