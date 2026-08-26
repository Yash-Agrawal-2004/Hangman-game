import tkinter as tk
import random
from collections import Counter
from PIL import Image, ImageTk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
root = tk.Tk()
root.title("Hangman Game")

# Fullscreen
root.state("zoomed")

# Dark theme
root.configure(bg="#000000")

# Press ESC to leave fullscreen
root.bind("<Escape>",
          lambda e: root.state("normal"))

main_frame = tk.Frame(root, bg="#000000")
main_frame.pack(fill="both",expand=True,padx=20,pady=20)



List1 ='schooling teaching training tutoring tuition development preparation instructional educative informational informative instructive illuminating enlightening comprehensive'
words = List1.split()
word = random.choice(words)

guessed_letters = ""
chances = 6

screen_width = root.winfo_screenwidth()

word_font_size = max(20, screen_width // 50)


hint_label = tk.Label(
    main_frame,
    text="Hint: Word is related to Education",fg="white",
    font=("Segoe UI", max(6, screen_width // 150))
)


word_label = tk.Label(
    main_frame,
    text="_ " * len(word),fg="white",
    font=("Impact", word_font_size)
)


chance_label = tk.Label(
    main_frame,fg="#C11007",
    text=f"Chances Left: {chances}",
    font=("Impact", max(12, screen_width // 100))
)
chance_label.config(fg="#C11007")

message_label = tk.Label(
    main_frame,
    text="",
    font=("Impact", max(12, screen_width // 100))
)


entry = ctk.CTkEntry(
    main_frame,
    width=250,
    height=40,
    corner_radius=20,
    font=("Impact", max(12, screen_width // 100))
)


def restart_game():
    global word, guessed_letters, chances

    # Select new word
    word = random.choice(words)

    # Reset variables
    guessed_letters = ""
    chances = 6

    # Reset UI
    word_label.config(text="_ " * len(word))
    chance_label.config(text=f"Chances Left: {chances}",fg="#C11007")
    message_label.config(text="")
    entry.delete(0, tk.END)

    # Reset hangman image
    canvas.itemconfigure(head_id, state="hidden")
    canvas.itemconfigure(head1_id, state="hidden")
    canvas.itemconfigure(body_id, state="hidden")
    canvas.itemconfigure(left_arm_id, state="hidden")
    canvas.itemconfigure(right_arm_id, state="hidden")
    canvas.itemconfigure(left_leg_id, state="hidden")
    canvas.itemconfigure(right_leg_id, state="hidden")

    # Restore button
    guess_btn.configure(text="Guess", command=check_guess)


def check_guess():
    global guessed_letters, chances

    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if len(guess) != 1 or not guess.isalpha():
        message_label.config(text="Enter one alphabet only",fg="#C11007")
        return

    if guess in guessed_letters:
        message_label.config(text="Already guessed!",fg="#C11007")
        return

    guessed_letters += guess

    if guess not in word:
        chances -= 1

        if chances == 5:
            canvas.itemconfigure(head_id, state="normal")
            canvas.itemconfigure(head1_id, state="normal")

        elif chances == 4:
            canvas.itemconfigure(body_id, state="normal")

        elif chances == 3:
            canvas.itemconfigure(left_arm_id, state="normal")

        elif chances == 2:
            canvas.itemconfigure(right_arm_id, state="normal")

        elif chances == 1:
            canvas.itemconfigure(left_leg_id, state="normal")

        elif chances == 0:
            canvas.itemconfigure(right_leg_id, state="normal")

    display_word = ""

    for char in word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "

    word_label.config(text=display_word)
    chance_label.config(text=f"Chances Left: {chances}",fg="#C11007")

    if all(char in guessed_letters for char in word):
        message_label.config(text="🎉 Congratulations! You Won!",fg="#32CD32")
        guess_btn.configure(text="Replay", command=restart_game)

    elif chances == 0:
        message_label.config(
            text=f"❌ You Lost! Word was '{word}'"
        )
        guess_btn.configure(text="Replay", command=restart_game)

guess_btn = ctk.CTkButton(
    main_frame,
    text="Guess",
    width=150,
    height=40,
    corner_radius=20,text_color="#000000",
    fg_color="#32CD32",
    hover_color="#28a428",command=check_guess,font=("Impact", max(12, screen_width // 80))
)

canvas = tk.Canvas(
    main_frame,
    width=400,
    height=500,
    bg="#000000",
    highlightthickness=0
)


gallows = tk.PhotoImage(file="../assets/hangman0.png")
head = tk.PhotoImage(file="../assets/hangman1.png")
head1 = tk.PhotoImage(file="../assets/hangman11.png")
body = tk.PhotoImage(file="../assets/hangman2.png")
left_arm = tk.PhotoImage(file="../assets/hangman4.png")
right_arm = tk.PhotoImage(file="../assets/hangman3.png")
left_leg = tk.PhotoImage(file="../assets/hangman5.png")
right_leg = tk.PhotoImage(file="../assets/hangman6.png")

head = Image.open("../assets/hangman1.png")
head = head.resize((190, 90))
head = ImageTk.PhotoImage(head)

head1 = Image.open("../assets/hangman11.png")
head1 = head1.resize((30, 15))
head1 = ImageTk.PhotoImage(head1)

body = Image.open("../assets/hangman2.png")
body = body.resize((230, 230))
body = ImageTk.PhotoImage(body)

left_arm= Image.open("../assets/hangman4.png")
left_arm = left_arm.resize((175, 180))
left_arm = ImageTk.PhotoImage(left_arm)

right_arm = Image.open("../assets/hangman3.png")
right_arm = right_arm.resize((180, 180))
right_arm = ImageTk.PhotoImage(right_arm)

left_leg = Image.open("../assets/hangman5.png")
left_leg = left_leg.resize((200, 270))
left_leg = ImageTk.PhotoImage(left_leg)

right_leg = Image.open("../assets/hangman6.png")
right_leg = right_leg.resize((180, 256))
right_leg = ImageTk.PhotoImage(right_leg)

canvas.create_image(
    200, 250,
    image=gallows
)

head_id = canvas.create_image(
    303, 165,
    image=head,
    state="hidden"
)

head1_id = canvas.create_image(
    303, 122,
    image=head1,
    state="hidden"
)

body_id = canvas.create_image(
    306, 250,
    image=body,
    state="hidden"
)

left_arm_id = canvas.create_image(
    270, 235,
    image=left_arm,
    state="hidden"
)

right_arm_id = canvas.create_image(
    341, 255,
    image=right_arm,
    state="hidden"
)

left_leg_id = canvas.create_image(
    289, 366,
    image=left_leg,
    state="hidden"
)

right_leg_id = canvas.create_image(
    328, 375,
    image=right_leg,
    state="hidden"
)


hint_label.pack(pady=15)
word_label.pack(pady=15)
chance_label.pack(pady=15)
entry.pack(pady=15, ipadx=20)
message_label.pack(pady=15)
guess_btn.pack(pady=15)
canvas.pack()

for widget in [hint_label, chance_label, message_label, word_label]:
    widget.configure(bg="#000000")

root.bind("<Return>", lambda event: check_guess())


root.mainloop()
