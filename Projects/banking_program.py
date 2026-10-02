# Python Banking Program

print("------Welcome to the Bank ATM Program------")

correct_pin = 6416
balance = 8000

def login():
    pin = int(input("Please enter your pin to access your bank account: "))
    if pin == correct_pin:
        print("Welcome User")
        return True
    else:
        print("Wrong pin")
        return False

def show_balance():
    print(f"Your balance is ₹{balance}")

def deposit():
    global balance
    deposit_amount = float(input("Enter amount to deposit: "))
    print(f"₹{deposit_amount} deposited successfully!")
    balance = balance+deposit_amount

def withdraw():
    global balance
    withdraw_amount = float(input("Enter amount to withdraw: "))
    if withdraw_amount<balance:
        print(f"{withdraw_amount} withdrawn successfully!")
        print(f"Remaining balance: ₹{balance-withdraw_amount}")
        balance = balance - withdraw_amount
    else:
        print("Insufficient funds!")

def main():
    if login():
         while True:
                print("1. Show Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Exit")
        
                choice = int(input("ENter your choice (1-4): "))
                if choice == 1:
                    show_balance()
                elif choice == 2:
                    deposit()
                elif choice == 3:
                    withdraw()
                elif choice == 4:
                    break
                print("***********************************")

if __name__=='__main__':
    main()