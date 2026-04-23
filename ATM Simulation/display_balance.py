from statement import deposited_money, withdrawed_money
from available_balance import avail_bal
def display():
    print("Money deposited till now:")
    for bal in deposited_money:
        print(bal)
    print("Money withdrawed till now:")
    for bal in withdrawed_money:
        print(bal)
    balance = avail_bal()
    print(f"{balance} amount is in your account")