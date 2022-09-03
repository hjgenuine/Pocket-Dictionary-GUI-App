from tkinter import *
from tkinter import messagebox as mb
from PIL import Image, ImageTk
from difflib import get_close_matches
import json

# For getting the defination of a Word
def get_defination(word):
    if data.get(word):
        return "\n".join(["- " + x for x in data.get(word)])

# For displaying the defination of a Word
def update_defination():
    word = e.get().lower()
    display.configure(state="normal")
    display.delete("1.0", END)
    defination = "Word not Found, please Recheck it!"
    if get_defination(word):
        defination = get_defination(word)
    else:
        similar_word = get_close_matches(word, data, 1, cutoff=0.8)
        if similar_word:
            r = mb.askyesno("Word Mismatch", "Did you mean %s?" % similar_word[0])
            if r:
                defination = get_defination(similar_word[0])
    display.insert(END, defination)
    display.configure(state="disabled")

# Loading the Data
data = json.load(open("data.json"))

# Creating the GUI
root = Tk()
root.geometry("500x500")
root.resizable(0, 0)
root.title("Pocket Dictionary")

# Background Image
bg = ImageTk.PhotoImage(Image.open("Bg.jpg"))

canvas = Canvas(root, height=500, width=500)
canvas.pack(fill="both", expand=True, padx=2, pady=2)

# Image & Title
canvas.create_image(0, 0, image=bg, anchor="nw")
canvas.create_text(250, 70, text="Pocket Dictionary", font=("Trebuchet MS", 30), fill="white")

# Input Section
canvas.create_text(145, 180, text="Word: ", font=("Trebuchet MS", 20), fill="violet")
e = Entry(root, font=("Trebuchet MS", 16))
canvas.create_window(300, 180, window=e)
b = Button(text="Search", font=("Trebuchet MS", 14), border=0, command=update_defination, activebackground="violet", activeforeground="white", padx=10, pady=0)
b.configure(bg="purple", fg="white")
canvas.create_window(230, 230, window=b)

# Output Section
canvas.create_text(250, 295, text="Output", font=("Trebuchet MS", 18), fill="violet")
display = Text(root, height=6, width=40, font=("Trebuchet MS", 14), wrap=WORD)
display.configure(state="disabled")
canvas.create_window(250, 390, window=display)

root.mainloop()
