balance = 1000

def add_money():
    balance
    balance = balance + 500
    print("Balance after adding money:", balance)
    print(f"Inside Function: {balance}")
add_money()
print(f"Outside Function: {balance}")