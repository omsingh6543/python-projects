from statement import withdrawed_money
def withdraw():
    try:
        withdraw_money = int(input("Enter the amount you want to withdraw:"))   
        withdrawed_money.append(withdraw_money)
        print(f"{withdraw_money} amount withdrawed succesfully")
    except ValueError:
        print("Enter Valid amount")