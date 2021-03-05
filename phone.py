from tkinter import *
from tkinter import scrolledtext
from functools import partial
from tkinter import Tk, W, E


    
window = Tk()
window.title("Наберите номер телефона")
window.geometry('250x250')
#txt = scrolledtext.ScrolledText(window,width=20,height=1)
txt = Entry(window,width=20)  

def clicked(n):
#    txt.delete(1.0, END)
    txt.insert(INSERT, n)


#Кнопка
btn1 = Button(window, text="1", command=partial(clicked, 1))
btn2 = Button(window, text="2", command=partial(clicked, 2))
btn3 = Button(window, text="3", command=partial(clicked, 3))
btn4 = Button(window, text="4", command=partial(clicked, 4))
btn5 = Button(window, text="5", command=partial(clicked, 5))
btn6 = Button(window, text="6", command=partial(clicked, 6))
btn7 = Button(window, text="7", command=partial(clicked, 7))
btn8 = Button(window, text="8", command=partial(clicked, 8))
btn9 = Button(window, text="9", command=partial(clicked, 9))
btn10 = Button(window, text="", command=partial(clicked, ''))
btn11 = Button(window, text="0", command=partial(clicked, 0))
btn12 = Button(window, text="#", command=partial(clicked, '#'))

txt.grid(column= 0, row=0)
btn1.grid(column=1, row=2)
btn2.grid(column=2, row=2)
btn3.grid(column=3, row=2)
btn4.grid(column=1, row=3)
btn5.grid(column=2, row=3)
btn6.grid(column=3, row=3)
btn7.grid(column=1, row=4)
btn8.grid(column=2, row=4)
btn9.grid(column=3, row=4)
btn10.grid(column=1, row=5)
btn11.grid(column=2, row=5)
btn12.grid(column=3, row=5)

window.mainloop()
