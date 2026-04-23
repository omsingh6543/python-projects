from available_balance import avail_bal
from deposit_money import deposit
from withdraw_money import withdraw
from display_balance import display

def library():
    
    while True:
        print("\n1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Display Account")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        
        if choice == 1:
            deposit()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            display()
        elif choice == 4:
            print("Thank you")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    library()
        