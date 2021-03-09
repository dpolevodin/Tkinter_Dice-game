import tkinter as tk
from functools import partial
from tkinter import Entry
from tkinter import messagebox 
import random
import time

window = tk.Tk()
window.title("Игра: Кости")

"""Переменные для игры"""
user_score = 0
admin_score = 0

""" Функция броска кубика"""
def click_roll():
    global user_score
    global admin_score
    roll_user = random.randint(1,6)
    roll_admin = random.randint(1,6)
    time.sleep(1)
    if roll_user > roll_admin:
        user_score += 1
    if roll_user < roll_admin:
        admin_score += 1
    if roll_user == roll_admin:
        messagebox.showinfo('Так тоже бывает...', 'У нас ничья в этой партии!')
    txt.delete(0, 'end')
    txt.insert(0, 'У тебя на кубике выпало - {}, мой результат - {}'.format(roll_user, roll_admin)) 
    label2.configure(text='Общий счет игры: Пользователь - {}, Админ - {}'.format(user_score, admin_score))

""" настройка виджетов """
txt = Entry(window,width=60)  
label = tk.Label(text='Бросаем кубик по очереди. Выигрывает тот, у кого выпадет большее число от 1 до 6')
label2 = tk.Label()
button = tk.Button(
    text='Бросить',
    width=10,
    height=2,
    font=('Calibri', 11, 'bold'),
    bg='white',
    fg='black',
    command=partial(click_roll))

""" создаем геометрию """
label.grid()
button.grid()
txt.grid()
label2.grid()

window.mainloop()
