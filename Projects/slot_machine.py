# Python Slot Machine Program
import random

symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

def spin_row():
    print("Spinning...")
    return [random.choice(symbols) for _ in range(0,3)]

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0]=="🍒":
            return bet *3
        elif row[0]=="🍉":
            return bet *4
        elif row[0]=="🍋":
            return bet *5
        elif row[0]=="🔔":
            return bet *10
        elif row[0]=="⭐":
            return bet *20
    return 0

def main():
    print("******************************************")
    print("*************** SLOT MACHINE *************")
    print("******************************************")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    balance = 100
    while balance>0:
        print(f"Current Balnce: ${balance}")
        bet = input("Place your bet: $ ")
        if not bet.isdigit():
            print("Invalid input! Please enter a valid numeric amount.") 
            continue

        bet = int(bet)

        if bet>balance:
            print("Insufficient funds!")
            continue

        if bet <=0:
            print("Please enter an amount greater than 0.")
            continue
        
        print("Bet accepted successfully!")
        print(f"Your bet: ${bet}")
        balance = balance - bet
        print(f"Your balance: ${balance}")

        row = spin_row()
        print_row(row)        
        payout = get_payout(row,bet)
        if payout >0:
            print(f"You won ${payout}")
        else:
            print("Sorry, You lost this round")

        balance += payout

        play_again = input("Do you want to spin again?:(Y/N): ")
        if play_again.upper() !='Y':
            break
    print(f"Game over! Your final balance ${balance}")

if __name__ == "__main__":
    main() 