import random
import time
import tkinter

def yeet():
    troll_fen = tkinter.Tk()
    troll_fen.title('LOL')
    troll_fen.geometry('560x320')
    troll_fen.minsize(560, 320)
    troll_fen.maxsize(560, 320)
    troll_fen.config(background='#333230')
    troll_txt = tkinter.Label(troll_fen, text='Your computer got destroyed and I\'m very happy', fg='#FFFFFF',
                      font=("Pusia", 10), bg='#333230')
    troll_txt.pack()
    troll_btn = tkinter.Button(text='Shit', font=("Pusia", 15), bg='#F0F0F0', fg='#000000', command=yeet2)
    troll_btn.pack(padx=7, pady=5)
    troll_fen.mainloop()


def yeet2():
    troll_fen2 = tkinter.Tk()
    troll_fen2.title('Still using this computer ?')
    troll_fen2.geometry('560x320')
    troll_fen2.minsize(560, 320)
    troll_fen2.maxsize(560, 320)
    troll_fen2.config(background='#333230')
    height = 300
    width = 200
    troll_txt2 = tkinter.Label(troll_fen2, text='Your computer got destroyed and I\'m very happy', fg='#FFFFFF',
                       font=("Pusia", 10), bg='#333230')
    troll_txt2.pack()
    troll_btn2 = tkinter.Button(text='Shit', font=("Pusia", 15), bg='#F0F0F0', fg='#000000')
    troll_btn2.pack(padx=7, pady=5)
    troll_can2 = tkinter.Canvas(troll_fen2, width=width, height=height, bg='#333230', bd=0, highlightthickness=0)
    troll_can2.pack()
    troll_fen2.mainloop()


a = True

while a:
    wait_sec = random.uniform(0.02, 0.7)
    time.sleep(int(wait_sec))
    yeet()
    yeet2()
