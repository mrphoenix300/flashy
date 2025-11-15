from tkinter import *
import pandas

FONT1 = ("Arial", 60, "bold")
FONT2 = ("Arial", 40, "italic")
BACKGROUND_COLOR = "#B1DDC6"


try:
    words = pandas.read_csv("words_to_learn")
    words_to_learn = {"French": words["French"].to_list(), "English": words["English"].to_list()}
    print(len(words_to_learn["French"]))
    print(len(words_to_learn["English"]))
except FileNotFoundError:
    words = pandas.read_csv("./data/french_words.csv")
    words_to_learn = {"French": words["French"].to_list(), "English": words["English"].to_list()}
    print(len(words_to_learn["French"]))
    print(len(words_to_learn["English"]))


current_word = {"French": f"{words_to_learn['French'][0]}", "English": f"{words_to_learn['English'][0]}"}
unknown_words = {"French": [], "English": []}
index = 1


def next_word():
    global index,words_to_learn

    if index < len(words_to_learn["French"]):
        current_word["French"] = words_to_learn["French"][index]
        current_word["English"] = words_to_learn["English"][index]
        index += 1
    else:
        index = 0



def french_card():
    canvas.itemconfig(card, image=front_card)
    canvas.itemconfig(card, state="normal")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=f"{current_word['French']}", fill="black")
    print(current_word)



def english_card():
    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(card, state="normal")
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=f"{current_word['English']}", fill="white")
    print(current_word)

def save_progress():
    df = pandas.DataFrame(unknown_words)
    df.to_csv("words_to_learn", mode="w", index=False)

def keep_progress():
    global unknown_words
    unknown_words["French"].append(current_word["French"])
    unknown_words["English"].append(current_word["English"])
    save_progress()

def update_progress():
    global unknown_words
    if current_word["French"] in unknown_words["French"]:
        unknown_words["French"].pop(index - 1)
        unknown_words["English"].pop(index - 1)
        save_progress()

def refresh(action):
    global switch
    window.after_cancel(switch)
    if action == "wrong":
        keep_progress()
    elif action == "right":
        update_progress()
    next_word()
    french_card()
    switch = window.after(3000, english_card)


window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR)
window.config(pady=50, padx=50)

front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526)
card = canvas.create_image(400, 263, image=front_card)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, font=FONT2, text="French")
word = canvas.create_text(400, 263, font=FONT1, text=f"{current_word['French']}")
switch = window.after(3000, english_card)
canvas.grid(column=0, row=0, columnspan=2)

img1 = PhotoImage(file="./images/right.png")
right_button = Button(image=img1, command=lambda: refresh("right"))
right_button.config(highlightthickness=0)
right_button.grid(column=1, row=1)

img2 = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=img2, command=lambda: refresh("wrong"))
wrong_button.config(highlightthickness=0)
wrong_button.grid(column=0, row=1)


window.mainloop()
