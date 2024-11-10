import tkinter as tk
import random


class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tebak Angka")
        
        self.number_to_guess = random.randint(1, 100) 
        self.attempts = 0 
        self.max_attempts = 10 

        self.instruction_label = tk.Label(root, text="Tebak angka antara 1 dan 100!", font=("Arial", 14))
        self.instruction_label.pack()

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack()

        self.guess_button = tk.Button(root, text="Tebak", font=("Arial", 14), command=self.check_guess)
        self.guess_button.pack()

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack()

        self.attempts_label = tk.Label(root, text=f"Tebakan tersisa: {self.max_attempts}", font=("Arial", 14))
        self.attempts_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())  
        except ValueError:
            self.result_label.config(text="Masukkan angka yang valid!")
            return

        self.attempts += 1  
        remaining_attempts = self.max_attempts - self.attempts 

        if guess < self.number_to_guess:
            self.result_label.config(text="Tebakan terlalu rendah!")
        elif guess > self.number_to_guess:
            self.result_label.config(text="Tebakan terlalu tinggi!")
        else:
            self.result_label.config(text=f"Selamat! Anda menebak dengan benar dalam {self.attempts} percobaan!")
            self.guess_button.config(state="disabled")  


        self.attempts_label.config(text=f"Tebakan tersisa: {remaining_attempts}")

        if remaining_attempts <= 0 and guess != self.number_to_guess:
            self.result_label.config(text="Game Over! Anda kehabisan tebakan.")
            self.guess_button.config(state="disabled") 

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
