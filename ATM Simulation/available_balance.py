from statement import withdrawed_money, deposited_money

def avail_bal():
    total_deposited_money = 0
    for bal in deposited_money:
        total_deposited_money += bal
    total_withdrawed_money = 0
    for bal in withdrawed_money:
        total_withdrawed_money += bal 
    balance = total_deposited_money - total_withdrawed_money
    return balance