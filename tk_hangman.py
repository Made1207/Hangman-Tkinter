import random
import string
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from words import words

root = tk.Tk()
root.geometry('500x500')

score = []

def get_valid_word(words):
    word = random.choice(words)
    if '-' in word or ' ' in word:
        word = random.choice(words)
    if len(list(word)) > 8:
        word = random.choice(words)

    return word.upper()

word = get_valid_word(words)
word_letters = []
alphabet = list(string.ascii_uppercase)
used_letters = []
lives = [1, 2, 3, 4, 5, 6, 7]

def hangman():
    if len(word_letters) == 0:
        for i in range(len(word)):
            word_letters.append('_')
    for widget in root.winfo_children():
        widget.destroy()
    def take_guess():
        guess = entry.get().upper()
        if guess in alphabet:
            if guess in used_letters:
                hangman()
            else:
                word_letters.clear()
                used_letters.append(guess.upper())
                word_letters.clear()
                for letter in word:
                    if letter in used_letters:
                        word_letters.append(letter)
                    else:
                        word_letters.append('_')
                if guess not in word:
                    lives.remove(lives[len(lives) - 1])
        hangman()

    hang0 = Image.open('Hangman/hang0.png')
    hang1 = Image.open('Hangman/hang1.png')
    hang2 = Image.open('Hangman/hang2.png')
    hang3 = Image.open('Hangman/hang3.png')
    hang4 = Image.open('Hangman/hang4.png')
    hang5 = Image.open('Hangman/hang5.png')
    hang6 = Image.open('Hangman/hang6.png')
    hang7 = Image.open('Hangman/stickman celebrating.png')

    h0 = hang0.resize((180, 300), Image.ANTIALIAS)
    h1 = hang1.resize((180, 300), Image.ANTIALIAS)
    h2 = hang2.resize((180, 300), Image.ANTIALIAS)
    h3 = hang3.resize((180, 300), Image.ANTIALIAS)
    h4 = hang4.resize((180, 300), Image.ANTIALIAS)
    h5 = hang5.resize((180, 300), Image.ANTIALIAS)
    h6 = hang6.resize((180, 300), Image.ANTIALIAS)
    h7 = hang7.resize((180, 300), Image.ANTIALIAS)

    ha0 = ImageTk.PhotoImage(h0)
    ha1 = ImageTk.PhotoImage(h1)
    ha2 = ImageTk.PhotoImage(h2)
    ha3 = ImageTk.PhotoImage(h3)
    ha4 = ImageTk.PhotoImage(h4)
    ha5 = ImageTk.PhotoImage(h5)
    ha6 = ImageTk.PhotoImage(h6)
    ha7 = ImageTk.PhotoImage(h7)

    if len(lives) == 7:
        img = tk.Label(root, image = ha0)
        img.image = ha0
        img.pack()
    elif len(lives) == 6:
        img = tk.Label(root, image = ha1)
        img.image = ha1
        img.pack()
    elif len(lives) == 5:
        img = tk.Label(root, image = ha2)
        img.image = ha2
        img.pack()
    elif len(lives) == 4:
        img = tk.Label(root, image = ha3)
        img.image = ha3
        img.pack()
    elif len(lives) == 3:
        img = tk.Label(root, image = ha4)
        img.image = ha4
        img.pack()
    elif len(lives) == 2:
        img = tk.Label(root, image = ha5)
        img.image = ha5
        img.pack()
    elif len(lives) == 1:
        img = tk.Label(root, image = ha6)
        img.image = ha6
        img.pack()
    label = tk.Label(root, text = ', '.join(word_letters))
    label.pack(padx = 130)
    entry = tk.Entry(root)
    entry.pack(padx = 130)
    button = tk.Button(root, text = 'Guess', command = take_guess, bg = '#263D42')
    button.pack(padx = 130)
    label = tk.Label(root, text = 'Used Letters:')
    label.pack(padx = 130)
    label = tk.Label(root, text = used_letters)
    label.pack(padx = 130)
    if len(lives) - 1 == 0:
        for widget in root.winfo_children():
            widget.destroy()
        img = tk.Label(root, image = ha6)
        img.image = ha6
        img.pack()
        fontStyle1 = tkFont.Font(size = 50)
        fontStyle2 = tkFont.Font(size = 30)
        label = tk.Label(root, text = 'You Lost!', font = fontStyle1, padx = 90)
        label.pack()
        result = ['The', 'word', 'was', word]
        label = tk.Label(root, text = ' '.join(result), font = fontStyle2, padx = 90)
        label.pack()
    if '_' not in word_letters:
        for widget in root.winfo_children():
            widget.destroy()
        img = tk.Label(root, image = ha7)
        img.image = ha7
        img.pack()
        fontStyle1 = tkFont.Font(size = 50)
        fontStyle2 = tkFont.Font(size = 30)
        label = tk.Label(root, text = 'You Guessed Right!', font = fontStyle1, padx = 90)
        label.pack()
        result = ['The', 'word', 'was', word]
        label = tk.Label(root, text = ' '.join(result), font = fontStyle2, padx = 90)
        label.pack()

hangman()
root.mainloop()