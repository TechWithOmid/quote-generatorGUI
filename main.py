from tkinter import *
import random
import requests

root = Tk()

# ====== TODO ======
# fix generate button


# ================= Variables =====================
color = '#ededed'
generated_quote = StringVar()
generated_quote.set('click generate button')
url = 'https://type.fit/api/quotes'
url = requests.get(url).json()
quote_author = StringVar()


# ================= Functions =====================
def gen_quote():
    global generated_quote
    quotes = random.choice(url)
    generated_quote.set(quotes["text"])
    quote_author.set(quotes["author"])


# ================= Settings =====================
root.geometry('500x300')
root.resizable(height=False, width=False)
root.title('Quote Generator')
root.config(bg=color)

# ================= Button&Entry =====================
frameQuote = Frame(root, width=500, height=150, bg=color)
frameQuote.pack(side=TOP)

frameGen = Frame(root, width=500, height=150, bg=color)
frameGen.pack(side=TOP)

quote_label = Label(frameQuote, bg=color, textvariable=generated_quote, justify=LEFT, wraplength=300)
quote_label.pack(pady=10)

author_label = Label(frameQuote, bg=color, textvariable=quote_author, justify=LEFT)
author_label.pack(pady=10)

generateBtn = Button(frameGen, text='Generate', bg='#fc2e00', command=gen_quote, pady=5, padx=5)
generateBtn.pack(pady=25)

root.mainloop()
