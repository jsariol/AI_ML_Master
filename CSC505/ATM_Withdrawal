def atm_process(pin_correct=True, balance=100.0):
    attempts = 0
    max_attempts = 3
    print("ATM Ready. Insert your card...")
    print("Card inserted. Please enter your PIN.")

    while attempts < max_attempts:
        pin_input = input("Enter PIN: (simulate 'correct' or 'incorrect'): ").strip().lower()
        if pin_input == "correct" or (pin_correct and pin_input != "incorrect"):
            print("PIN accepted. Access granted.")
            break
        else:
            attempts += 1
            print(f"Incorrect PIN. Attempts remaining: {max_attempts - attempts}")
            if attempts >= max_attempts:
                print("Too many failed attempts. Card retained. Access denied.")
                return

    print("Checking account balance...")
    if balance == 0:
        print("Account balance is zero. Account closed.")
        return
    else:
        print(f"Current balance: ${balance:.2f}")
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print(f"${withdraw:.2f} dispensed. Remaining balance: ${balance:.2f}")
        else:
            print("Insufficient funds. Transaction cancelled.")
    print("Please take your card. Session complete.")

if __name__ == "__main__":
    atm_process()
