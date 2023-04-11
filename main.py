import turtle
import csv
import pandas
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
window=Tk()
window.title("French Flash")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
canvas=Canvas(width=700,height=500)
card_fr=PhotoImage(file="images/card_front.png")
card_bk=PhotoImage(file="images/card_back.png")
page_bg=canvas.create_image(350,250,image=card_fr)
lang=canvas.create_text(350,150,text="",font=("Ariel",40,"italic"))
word=canvas.create_text(350,250,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
og_data={}
current_card={}
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data=pandas.read_csv("data/french_words.csv")
    df=og_data.to_dict(orient="records")
else:
    df=data.to_dict(orient="records")


def is_known():
    df.remove(current_card)
    print(len(df))
    data=pandas.DataFrame(df)
    data.to_csv("data/words_to_learn.csv",index=False)

    next_card()
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(df)
    canvas.itemconfig(lang,text="French",fill="Black")
    canvas.itemconfig(word,text=current_card["French"],fill="Black")
    canvas.itemconfig(page_bg,image=card_fr)
    flip_timer=window.after(3000, func=Flip_card)
def Flip_card():
    canvas.itemconfig(lang,text="English",fill="White")
    canvas.itemconfig(word,text=current_card["English"],fill="White")
    canvas.itemconfig(page_bg,image=card_bk)
flip_timer=window.after(3000, func=Flip_card)
correct=PhotoImage(file="images/right.png")
Correct=Button(image=correct,highlightthickness=0,command=is_known)
Correct.grid(row=1,column=1)
Wrong=PhotoImage(file="images/wrong.png")
wrong=Button(image=Wrong,highlightthickness=0,command=next_card)
wrong.grid(row=1,column=0)
next_card()









window.mainloop()