from tkinter import *
import random

# ------------------------ ROOT ------------------------ #
FONT = "Comic Sans MS"
BACKGROUND = "#371B58"
FOREGROUND = "#3EC70B"

root = Tk()
root.geometry = "200x400"
root.title("Dre's Magic 8-Ball")
root.configure(background=BACKGROUND, highlightcolor=FOREGROUND, highlightthickness=4, padx=20, pady=20)

# ----------------------- ANSWERS ----------------------- #

answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.",
           "As I see it, yes.", "Most likely.", "Outlook good.", "Signs point to yes.", "Abso-fucking-lutely!",
           "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
           "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.",
           "Outlook not so good.", "Very doubtful."]

# --------------------- FUNCTIONS ----------------------- #


def respond():
    answer.delete(1.0, END)
    response = random.choice(answers)
    answer.insert(END, response)


def clear():
    question_entry.delete(0, END)
    answer.delete(1.0, END)


# ----------------------- LABELS ------------------------ #

header_label = Label(text="Dre's Magic 8-Ball", font=(FONT, 26))
header_label.config(bg=BACKGROUND, fg=FOREGROUND)
question_label = Label(text="Ask a question below", font=(FONT, 16))
question_label.config(bg=BACKGROUND, fg=FOREGROUND)

# ----------------------- BUTTONS ----------------------- #

answer_button = Button(text="Get Answer", font=(FONT, 16, "bold"), command=respond)
answer_button.config(bg=FOREGROUND, fg=BACKGROUND, activebackground="#FFCE45")
clear_button = Button(text="Clear", font=(FONT, 16, "bold"), command=clear)
clear_button.config(bg=FOREGROUND, fg=BACKGROUND, activebackground="#FFCE45")

# ------------------------ ENTRY ------------------------- #

question_entry = Entry(width=50, font=(FONT, 16))

# ------------------------ TEXTBOX ----------------------- #

answer = Text(width=50, height=2, font=(FONT, 16))


# ------------------------- PACK ------------------------- #
header_label.pack()
question_label.pack()
question_entry.pack(pady=10)
answer_button.pack()
answer.pack(pady=10)
clear_button.pack()


root.mainloop()