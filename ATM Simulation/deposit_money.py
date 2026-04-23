from statement import deposited_money
def deposit():
    try:
        deposit_money = int(input("Enter the amount you want to deposit:"))   
        deposited_money.append(deposit_money)
        print(f"{deposit_money} amount deposited succesfully")
    except ValueError:
        print("Enter Valid amount")
        