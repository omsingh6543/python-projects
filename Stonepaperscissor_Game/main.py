from function import functions
import random

item_list = ["stone", "paper", "scissor"]

def play_game():
    print("*************Welcome to the Game*************")
    while True:
        try:
            your_choice = input(("Enter your move[stone, paper, scissor]: "))
            
            if your_choice not in item_list:
                print("Invalid input! Try again.")
                continue
            
        except:
            print("Please enter valid input")
            continue
        
        comp_choice = random.choice(item_list)
        
        print("Your choice:", your_choice)
        print("Computer choice:", comp_choice)
        
        functions(your_choice, comp_choice)
if __name__ == "__main__":
    play_game()      