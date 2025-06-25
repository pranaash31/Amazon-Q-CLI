#!/usr/bin/env python3
"""
CyberMind: Codebreaker Challenge
A cyberpunk-themed Mastermind game where players crack 4-digit security codes
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
from typing import List, Tuple

class CyberMindGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🔐 CyberMind: Codebreaker Challenge")
        self.root.geometry("600x700")
        self.root.configure(bg='#0a0a0a')
        self.root.resizable(False, False)
        
        # Game state
        self.secret_code = self.generate_secret_code()
        self.attempts = []
        self.max_attempts = 10
        self.game_over = False
        
        # Colors for cyber theme
        self.colors = {
            'bg': '#0a0a0a',
            'panel': '#1a1a2e',
            'accent': '#16213e',
            'success': '#00ff41',
            'warning': '#ffaa00',
            'error': '#ff0040',
            'text': '#00ff41',
            'secondary': '#888888'
        }
        
        self.setup_ui()
        
    def generate_secret_code(self) -> List[int]:
        """Generate a random 4-digit code with digits 0-9"""
        return [random.randint(0, 9) for _ in range(4)]
    
    def setup_ui(self):
        """Setup the main user interface"""
        # Title
        title_frame = tk.Frame(self.root, bg=self.colors['bg'])
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="🔐 CYBERMIND: CODEBREAKER",
            font=('Courier New', 20, 'bold'),
            fg=self.colors['success'],
            bg=self.colors['bg']
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="CRACK THE 4-DIGIT SECURITY CODE",
            font=('Courier New', 12),
            fg=self.colors['secondary'],
            bg=self.colors['bg']
        )
        subtitle_label.pack()
        
        # Input section
        input_frame = tk.Frame(self.root, bg=self.colors['panel'], relief='raised', bd=2)
        input_frame.pack(pady=20, padx=20, fill='x')
        
        tk.Label(
            input_frame,
            text="ENTER CODE:",
            font=('Courier New', 12, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['panel']
        ).pack(pady=10)
        
        # Code input fields
        self.code_frame = tk.Frame(input_frame, bg=self.colors['panel'])
        self.code_frame.pack(pady=10)
        
        self.code_entries = []
        for i in range(4):
            entry = tk.Entry(
                self.code_frame,
                width=3,
                font=('Courier New', 16, 'bold'),
                justify='center',
                bg=self.colors['accent'],
                fg=self.colors['text'],
                insertbackground=self.colors['text'],
                relief='flat',
                bd=2
            )
            entry.pack(side='left', padx=5)
            entry.bind('<KeyPress>', self.on_key_press)
            entry.bind('<KeyRelease>', self.auto_advance)
            self.code_entries.append(entry)
        
        # Submit button
        self.submit_btn = tk.Button(
            input_frame,
            text="🚀 HACK CODE",
            font=('Courier New', 12, 'bold'),
            bg=self.colors['success'],
            fg=self.colors['bg'],
            relief='flat',
            padx=20,
            pady=5,
            command=self.submit_guess
        )
        self.submit_btn.pack(pady=15)
        
        # Attempts display
        self.attempts_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.attempts_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        tk.Label(
            self.attempts_frame,
            text="HACK ATTEMPTS:",
            font=('Courier New', 14, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['bg']
        ).pack(anchor='w')
        
        # Scrollable attempts list
        self.attempts_canvas = tk.Canvas(
            self.attempts_frame,
            bg=self.colors['panel'],
            height=300,
            highlightthickness=0
        )
        self.attempts_scrollbar = ttk.Scrollbar(
            self.attempts_frame,
            orient="vertical",
            command=self.attempts_canvas.yview
        )
        self.attempts_canvas.configure(yscrollcommand=self.attempts_scrollbar.set)
        
        self.attempts_canvas.pack(side="left", fill="both", expand=True)
        self.attempts_scrollbar.pack(side="right", fill="y")
        
        self.attempts_inner_frame = tk.Frame(self.attempts_canvas, bg=self.colors['panel'])
        self.attempts_canvas.create_window((0, 0), window=self.attempts_inner_frame, anchor="nw")
        
        # Status bar
        self.status_frame = tk.Frame(self.root, bg=self.colors['accent'], relief='sunken', bd=1)
        self.status_frame.pack(side='bottom', fill='x')
        
        self.status_label = tk.Label(
            self.status_frame,
            text=f"Attempts remaining: {self.max_attempts}",
            font=('Courier New', 10),
            fg=self.colors['text'],
            bg=self.colors['accent']
        )
        self.status_label.pack(pady=5)
        
        # New game button
        self.new_game_btn = tk.Button(
            self.status_frame,
            text="🔄 NEW GAME",
            font=('Courier New', 10),
            bg=self.colors['warning'],
            fg=self.colors['bg'],
            relief='flat',
            command=self.new_game
        )
        self.new_game_btn.pack(side='right', padx=10, pady=2)
        
        # Focus on first entry
        self.code_entries[0].focus()
    
    def on_key_press(self, event):
        """Handle key press events"""
        if event.keysym == 'Return':
            self.submit_guess()
        elif event.keysym == 'BackSpace':
            return True
        elif not event.char.isdigit():
            return "break"  # Prevent non-digit input
    
    def auto_advance(self, event):
        """Auto-advance to next field when digit is entered"""
        widget = event.widget
        if len(widget.get()) == 1 and widget.get().isdigit():
            # Find current entry index
            current_index = self.code_entries.index(widget)
            if current_index < 3:
                self.code_entries[current_index + 1].focus()
    
    def submit_guess(self):
        """Process the player's guess"""
        if self.game_over:
            return
        
        # Get the guess
        guess = []
        for entry in self.code_entries:
            if not entry.get().isdigit():
                messagebox.showerror("Invalid Input", "Please enter 4 digits (0-9)")
                return
            guess.append(int(entry.get()))
        
        if len([g for g in guess if str(g).isdigit()]) != 4:
            messagebox.showerror("Invalid Input", "Please enter exactly 4 digits")
            return
        
        # Analyze the guess
        feedback = self.analyze_guess(guess)
        self.attempts.append((guess.copy(), feedback))
        
        # Display the attempt
        self.display_attempt(guess, feedback)
        
        # Check win condition
        if feedback['correct_position'] == 4:
            self.game_won()
            return
        
        # Check lose condition
        if len(self.attempts) >= self.max_attempts:
            self.game_lost()
            return
        
        # Update status
        remaining = self.max_attempts - len(self.attempts)
        self.status_label.config(text=f"Attempts remaining: {remaining}")
        
        # Clear entries for next guess
        for entry in self.code_entries:
            entry.delete(0, tk.END)
        self.code_entries[0].focus()
    
    def analyze_guess(self, guess: List[int]) -> dict:
        """Analyze the guess and return feedback"""
        correct_position = 0
        correct_digit = 0
        
        secret_copy = self.secret_code.copy()
        guess_copy = guess.copy()
        
        # First pass: check for correct position
        for i in range(4):
            if guess[i] == self.secret_code[i]:
                correct_position += 1
                secret_copy[i] = -1  # Mark as used
                guess_copy[i] = -2   # Mark as used
        
        # Second pass: check for correct digit, wrong position
        for i in range(4):
            if guess_copy[i] != -2:  # Not already matched
                if guess_copy[i] in secret_copy:
                    correct_digit += 1
                    secret_copy[secret_copy.index(guess_copy[i])] = -1
        
        return {
            'correct_position': correct_position,
            'correct_digit': correct_digit,
            'incorrect': 4 - correct_position - correct_digit
        }
    
    def display_attempt(self, guess: List[int], feedback: dict):
        """Display an attempt in the attempts list"""
        attempt_frame = tk.Frame(self.attempts_inner_frame, bg=self.colors['accent'], relief='raised', bd=1)
        attempt_frame.pack(fill='x', pady=2, padx=5)
        
        # Attempt number
        attempt_num = len(self.attempts)
        tk.Label(
            attempt_frame,
            text=f"#{attempt_num:02d}",
            font=('Courier New', 10, 'bold'),
            fg=self.colors['secondary'],
            bg=self.colors['accent'],
            width=4
        ).pack(side='left', padx=5)
        
        # Guess display
        guess_frame = tk.Frame(attempt_frame, bg=self.colors['accent'])
        guess_frame.pack(side='left', padx=10)
        
        for digit in guess:
            tk.Label(
                guess_frame,
                text=str(digit),
                font=('Courier New', 12, 'bold'),
                fg=self.colors['text'],
                bg=self.colors['panel'],
                width=2,
                relief='sunken',
                bd=1
            ).pack(side='left', padx=1)
        
        # Feedback display
        feedback_frame = tk.Frame(attempt_frame, bg=self.colors['accent'])
        feedback_frame.pack(side='right', padx=10)
        
        # Correct position (green circles)
        for _ in range(feedback['correct_position']):
            tk.Label(
                feedback_frame,
                text="●",
                font=('Courier New', 12),
                fg=self.colors['success'],
                bg=self.colors['accent']
            ).pack(side='left')
        
        # Correct digit (yellow circles)
        for _ in range(feedback['correct_digit']):
            tk.Label(
                feedback_frame,
                text="●",
                font=('Courier New', 12),
                fg=self.colors['warning'],
                bg=self.colors['accent']
            ).pack(side='left')
        
        # Incorrect (red circles)
        for _ in range(feedback['incorrect']):
            tk.Label(
                feedback_frame,
                text="●",
                font=('Courier New', 12),
                fg=self.colors['error'],
                bg=self.colors['accent']
            ).pack(side='left')
        
        # Update scroll region
        self.attempts_inner_frame.update_idletasks()
        self.attempts_canvas.configure(scrollregion=self.attempts_canvas.bbox("all"))
        self.attempts_canvas.yview_moveto(1.0)  # Scroll to bottom
    
    def game_won(self):
        """Handle game won state"""
        self.game_over = True
        self.submit_btn.config(state='disabled')
        for entry in self.code_entries:
            entry.config(state='disabled')
        
        self.status_label.config(
            text=f"🎉 ACCESS GRANTED! Code cracked in {len(self.attempts)} attempts!",
            fg=self.colors['success']
        )
        
        messagebox.showinfo(
            "Access Granted!",
            f"🎉 Congratulations, hacker!\n\nYou cracked the security code in {len(self.attempts)} attempts!\n\nThe code was: {' '.join(map(str, self.secret_code))}"
        )
    
    def game_lost(self):
        """Handle game lost state"""
        self.game_over = True
        self.submit_btn.config(state='disabled')
        for entry in self.code_entries:
            entry.config(state='disabled')
        
        self.status_label.config(
            text=f"🚨 ACCESS DENIED! Security system locked.",
            fg=self.colors['error']
        )
        
        messagebox.showinfo(
            "Access Denied!",
            f"🚨 Security breach detected!\n\nYou've exceeded the maximum attempts.\n\nThe secret code was: {' '.join(map(str, self.secret_code))}"
        )
    
    def new_game(self):
        """Start a new game"""
        self.secret_code = self.generate_secret_code()
        self.attempts = []
        self.game_over = False
        
        # Clear attempts display
        for widget in self.attempts_inner_frame.winfo_children():
            widget.destroy()
        
        # Reset UI
        self.submit_btn.config(state='normal')
        for entry in self.code_entries:
            entry.config(state='normal')
            entry.delete(0, tk.END)
        
        self.status_label.config(
            text=f"Attempts remaining: {self.max_attempts}",
            fg=self.colors['text']
        )
        
        self.code_entries[0].focus()
    
    def run(self):
        """Start the game"""
        self.root.mainloop()

if __name__ == "__main__":
    game = CyberMindGame()
    game.run()
