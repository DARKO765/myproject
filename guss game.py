import tkinter as tk
import random

# إعداد اللعبة
secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

# ألوان
bg_color = "#1e1e2f"
btn_color = "#4CAF50"
text_color = "#ffffff"
accent = "#ff9800"

# نافذة
root = tk.Tk()
root.title("🎮 Guess The Number")
root.geometry("350x400")
root.config(bg=bg_color)

# عنوان
title = tk.Label(root, text="🎯 Guess The Number", font=("Arial", 18, "bold"),
                 bg=bg_color, fg=accent)
title.pack(pady=10)

# تعليمات
info = tk.Label(root, text="Choose a number between 1 and 100",
                font=("Arial", 11), bg=bg_color, fg=text_color)
info.pack()

# إدخال
entry = tk.Entry(root, font=("Arial", 16), justify="center")
entry.pack(pady=10)

# نتيجة
result = tk.Label(root, text="", font=("Arial", 12, "bold"),
                  bg=bg_color, fg=text_color)
result.pack(pady=10)

# محاولات
attempts_label = tk.Label(root, text=f"Attempts: {attempts}/{max_attempts}",
                          font=("Arial", 10), bg=bg_color, fg=accent)
attempts_label.pack()

# دالة التحقق
def check():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1

        if guess < secret:
            result.config(text="📉 Too Low!", fg="#03A9F4")
        elif guess > secret:
            result.config(text="📈 Too High!", fg="#E91E63")
        else:
            result.config(text="🎉 YOU WIN!", fg="#4CAF50")

        attempts_label.config(text=f"Attempts: {attempts}/{max_attempts}")

        if attempts >= max_attempts and guess != secret:
            result.config(text=f"💀 You Lost! Number was {secret}", fg="red")

    except:
        result.config(text="❌ Enter valid number", fg="red")

# إعادة اللعبة
def reset():
    global secret, attempts
    secret = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result.config(text="")
    attempts_label.config(text=f"Attempts: {attempts}/{max_attempts}")

# أزرار
guess_btn = tk.Button(root, text="🎯 Guess", font=("Arial", 12, "bold"),
                      bg=btn_color, fg="white", width=15, command=check)
guess_btn.pack(pady=10)

reset_btn = tk.Button(root, text="🔄 Restart", font=("Arial", 12),
                      bg="#f44336", fg="white", width=15, command=reset)
reset_btn.pack()

# تشغيل
root.mainloop()