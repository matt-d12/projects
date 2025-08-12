"""
File Name: dice.py
Author: Matt D.
Course: CSE 111 | BYU-Idaho
Purpose:To test out multiple functions with a simple GUI to roll dice 
against an NPC and needing to win best of 5
"""
#Imports for GUI and random for rolls
import tkinter as tk
import random
from tkinter import messagebox

class DiceRollingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Rolling Game")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#bcbcbc")
        
        #Game variables
        self.round = 0
        self.max_rounds = 5
        self.player_wins = 0
        self.npc_wins = 0
        self.game_over = False
        
        #Create frames
        self.create_header_frame()
        self.create_dice_frame()
        self.create_score_frame()
        self.create_button_frame()
        self.create_history_frame()
        
        #History box initialize
        self.round_history = []

    #Function for title 
    def create_header_frame(self):
        header_frame = tk.Frame(self.root, bg="#3498db", height=50)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="DICE ROLLING GAME", font=("Arial", 18, "bold"), bg="#3498db", fg="white")
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(self.root, text="5 Total Rounds. Good luck!", font=("Arial", 12), bg="#bcbcbc")
        subtitle_label.pack(pady=5)
    
    #Function for dice rolls 
    def create_dice_frame(self):
        self.dice_frame = tk.Frame(self.root, bg="#bcbcbc")
        self.dice_frame.pack(pady=10)
        
        # Player dice
        player_label = tk.Label(self.dice_frame, text="YOUR ROLL", font=("Arial", 12, "bold"), bg="#bcbcbc")
        player_label.grid(row=0, column=0, padx=50)
        self.player_dice_label = tk.Label(self.dice_frame, text="?", font=("Arial", 36), width=2, height=1, relief=tk.RAISED, bg="white")
        self.player_dice_label.grid(row=1, column=0, padx=50, pady=10)
        
        # NPC dice
        npc_label = tk.Label(self.dice_frame, text="NPC ROLL", font=("Arial", 12, "bold"), bg="#bcbcbc")
        npc_label.grid(row=0, column=1, padx=50)
        self.npc_dice_label = tk.Label(self.dice_frame, text="?", font=("Arial", 36), width=2, height=1, relief=tk.RAISED, bg="white")
        self.npc_dice_label.grid(row=1, column=1, padx=50, pady=10)
    
    #Function for scores
    def create_score_frame(self):
        score_frame = tk.Frame(self.root, bg="#bcbcbc")
        score_frame.pack(pady=5)
        
        # Round counter
        self.round_label = tk.Label(score_frame, text="Round: 0/5", font=("Arial", 12), bg="#bcbcbc")
        self.round_label.grid(row=0, column=0, columnspan=2, pady=5)
        
        # Score labels
        self.player_score_label = tk.Label(score_frame, text="You: 0", font=("Arial", 12), bg="#bcbcbc")
        self.player_score_label.grid(row=1, column=0, padx=30)
        self.npc_score_label = tk.Label(score_frame, text="NPC: 0", font=("Arial", 12), bg="#bcbcbc")
        self.npc_score_label.grid(row=1, column=1, padx=30)
    
    #Function for buttons
    def create_button_frame(self):
        button_frame = tk.Frame(self.root, bg="#bcbcbc")
        button_frame.pack(pady=10)
        
        self.roll_button = tk.Button(button_frame, text="Roll Dice", font=("Arial", 12), bg="#5b5b5b", fg="white", width=10, height=1, command=self.roll_dice)
        self.roll_button.grid(row=0, column=0, padx=10)
        
        self.reset_button = tk.Button(button_frame, text="New Game", font=("Arial", 12), bg="#5b5b5b", fg="white", width=10, height=1, command=self.reset_game)
        self.reset_button.grid(row=0, column=1, padx=10)
    
    #Function for history of rolls
    def create_history_frame(self):
        history_frame = tk.Frame(self.root, bg="#bcbcbc")
        history_frame.pack(pady=10, fill=tk.X)
        history_label = tk.Label(history_frame, text="Game History", font=("Arial", 10, "bold"), bg="#bcbcbc")
        history_label.pack()
        
        # Replace Text widget with Label widgets for history
        self.history_frame = tk.Frame(history_frame, bg="#1e1e1e", bd=1, relief=tk.SUNKEN, height=100)
        self.history_frame.pack(padx=20, pady=5, fill=tk.X)
        
        # Create fixed labels for history entries
        self.history_labels = []
        for i in range(4):
            label = tk.Label(self.history_frame, text="", font=("Arial", 10), bg="#1e1e1e", fg="white", anchor="w", padx=5, pady=4)
            label.pack(fill=tk.X)
            self.history_labels.append(label)
    
    #Fucntion for dice roll and comparing results
    def roll_dice(self):
        if self.game_over:
            messagebox.showinfo("Game Over", "Game is already over. Please start a new game.")
            return
            
        # Roll the dice
        player_roll = random.randint(1, 6)
        npc_roll = random.randint(1, 6)
        
        # Update dice labels
        self.player_dice_label.config(text=str(player_roll))
        self.npc_dice_label.config(text=str(npc_roll))
        
        # Determine winner of this round
        round_result = ""
        if player_roll > npc_roll:
            round_result = "You win!"
            self.player_wins += 1
            #History mesasge
            result_message = f"Round {self.round + 1}: You rolled {player_roll}, NPC rolled {npc_roll}. {round_result}"
            #Colors change labels for winner
            self.player_dice_label.config(bg="#2ecc71")
            self.npc_dice_label.config(bg="#e74c3c")
            #Update round count if there's a winner
            self.round += 1
        elif npc_roll > player_roll:
            round_result = "NPC wins!"
            self.npc_wins += 1
            result_message = f"Round {self.round + 1}: You rolled {player_roll}, NPC rolled {npc_roll}. {round_result}"
            self.player_dice_label.config(bg="#e74c3c")
            self.npc_dice_label.config(bg="#2ecc71")
            self.round += 1
        else:
            round_result = "It's a tie!"
            result_message = f"Round {self.round + 1}: Both rolled {player_roll}. {round_result}"
            #Using blue label for ties
            self.player_dice_label.config(bg="#0000ff")
            self.npc_dice_label.config(bg="#0000ff")
        
        # Update history
        self.round_history.append(result_message)
        self.update_history_display()
        
        # Update round counter and score
        self.round_label.config(text=f"Round: {self.round}/5")
        self.player_score_label.config(text=f"You: {self.player_wins}")
        self.npc_score_label.config(text=f"NPC: {self.npc_wins}")
        
        # Check if game is over
        if self.round >= self.max_rounds:
            self.game_over = True
            self.end_game()
    
    #Function to update the history box
    def update_history_display(self):
        # Clear all labels
        for label in self.history_labels:
            label.config(text="")
        
        # Display the 4 most recent history rolls
        history_to_show = self.round_history[-4:] if len(self.round_history) > 4 else self.round_history
        
        # Fill labels from bottom to top with most recent at the top
        for i, message in enumerate(reversed(history_to_show)):
            if i < len(self.history_labels):
                self.history_labels[i].config(text=message)
    
    #Function for what happens when game is over based on winner
    def end_game(self):
        winner_message = ""
        if self.player_wins > self.npc_wins:
            winner_message = f"Congratulations! You won {self.player_wins}-{self.npc_wins}!"
            self.player_score_label.config(fg="#2ecc71")
            self.npc_score_label.config(fg="#e74c3c")
        elif self.npc_wins > self.player_wins:
            winner_message = f"You lost {self.player_wins}-{self.npc_wins}. Better luck next time!"
            self.player_score_label.config(fg="#e74c3c")
            self.npc_score_label.config(fg="#2ecc71")
        else:
            winner_message = f"It's a tie {self.player_wins}-{self.npc_wins}!"
        messagebox.showinfo("Game Over", winner_message)
    
    #Function to reset game / Start new game
    def reset_game(self):
        # Reset game variables
        self.round = 0
        self.player_wins = 0
        self.npc_wins = 0
        self.game_over = False
        self.round_history = []
        
        # Reset the UI/counts
        self.round_label.config(text="Round: 0/5")
        self.player_score_label.config(text="You: 0", fg="black")
        self.npc_score_label.config(text="NPC: 0", fg="black")
        self.player_dice_label.config(text="?")
        self.npc_dice_label.config(text="?")
        
        # Clear history box
        for label in self.history_labels:
            label.config(text="")

#Start program 
if __name__ == "__main__":
    root = tk.Tk()
    game = DiceRollingGame(root)
    root.mainloop()