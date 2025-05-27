import os
import time

isSameBank = True

# File Handling
def read_pin():
    with open("pin.txt", "r") as file:
        return file.read().strip()
def write_pin(pin):
    with open("pin.txt", "w") as file:
        file.write(pin)
def read_balance():
    with open("balance.txt", "r")    as file:
        return int(file.read().strip())
def write_balance(balance):
    with open("balance.txt", "w") as file:
        file.write(balance)
def valid_amount(amount):
    if amount % 100 == 0:
        return True
    else:
        return False
def user_name():
    with open("user.txt", "r") as file:
        return file.read().strip()
def bank_name():
    global isSameBank
    if isSameBank:
        with open("bank.txt", "w") as file:
            file.write("BDO")
            return "BDO"
    else:
        # If the bank is not BDO, read the bank name from the file
        with open("bank.txt", "r") as file:
            return file.read().strip()

# User Interface Functions
def header():
    bank = bank_name()
    print("[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]")
    print(bank.center(60, " "))
    print("[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]")
    print("----------------------------------------------------------------\n")
def footer():
    print("----------------------------------------------------------------")
    print("[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]")
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def pause():
    if os.name == 'nt':
        os.system('pause')
    else:
        input("Press to enter continue...")

# Registration and Login
def card_registration():
    while True:
        clear()
        header()
        print("Welcome to".center(60, " "))
        print()
        print("BANKO DE ORO".center(60, " "))
        print("""
                      Continue with BDO?
            Please select [N] if you want to transact
           with other bank or [Y] to continue with BDO.
        """)
        print("[Y] Yes    [N] No".center(60, " "))
        choice = input("                        Choice: ").strip().upper()
        if choice == "Y":
            print("\n                     You have selected BDO. \n       "
                  "       Please proceed with your transaction.")
            print()
            input('''                 Please insert your card and
                   press [ENTER] to continue.''')
            break
        elif choice == "N":
            global isSameBank
            isSameBank = False
            clear()
            other_bank_reg()
            clear()
            bank = bank_name()
            header()
            print(f"Welcome to {bank}".center(60, " "))

            print("""
            Note that this is an off-us transaction. 
                 For every off us transactions,
                 a fee will be deducted, 2 pesos
            for checking balance, 18 for withdrawal.
                         """)
            input('''               Please insert your card and
                press [ENTER] to continue.''')
            break
        else:
            print("Invalid Choice.")

    clear()
    header()
    print("\n\n")
    print("Card inserted.".center(60 , " "))
    print("Starting Session... ".center(60 , " "))
    print("\n\n")
    footer()
    time.sleep(2)
    return
def other_bank_reg():
    while True:
        clear()
        header()
        print("You have selected other bank.".center(60, " "))
        print("        Please select the following bank to proceed: \n"
              "             [1] Landbank\n"
              "             [2] BPI\n"
              "             [3] DBP\n"
              "             [4] Back to Menu ")
        choice = input("                    Choice : ")
        if choice == "1":
            with open("bank.txt", "w") as file:
                file.write("Landbank")
                return
        elif choice == "2":
            with open("bank.txt", "w") as file:
                file.write("BPI")
                return
        elif choice == "3":
            with open("bank.txt", "w") as file:
                file.write("DBP")
                return
        elif choice == "4":
            card_registration()
        else:
            print("Invalid choice.".center(60, " "))
            print("Please choose from the options given.".center(60, " "))
            footer()
            pause()
def register():
    clear()
    header()
    print("REGISTER\n".center(60, " "))

    with open("user.txt", "w") as file:
        username = input("             Enter Name: ").title()
        file.write(username)

    while True:
        new_pin = input("             Set your 6-digit PIN: ").strip()
        if len(new_pin) != 6 or not new_pin.isdigit():
            print("Invalid PIN format. Please try again.\n".center(60, " "))

        else:
            write_pin(new_pin)
            write_balance(str(10000))
            print()
            print("PIN Saved!\n".center(60, " "))
            footer()
            pause()
            clear()
            log_in()
def log_in():
    clear()
    header()
    with open("pin.txt", "a") as file:
        file.write("")
    print("LOG IN\n".center(60, " "))
    if not read_pin():
        print("NO USER FOUND. ".center(60, " "))
        print("Please register first.".center(60, " "))
        pause()
        register()
    print("Please log in to continue.".center(60, " "))
    print()
    max_attempts = 3
    for attempt in range(max_attempts):
        entered_pin = input("                   Enter your PIN: ")
        if entered_pin == read_pin():
            clear()
            header()
            print("\n\n")
            print("ACCESS GRANTED\n".center(60, " "))
            print("\n\n")
            footer()
            pause()
            menu()
        else:
            clear()
            header()
            print("LOG IN\n".center(60, " "))
            print(f"Incorrect PIN. Attempts left: {max_attempts - attempt - 1}".center(60, " "))
            print()
    print("Too many failed attempts. Exiting.".center(60, " "))
    print()
    footer()
    exit()

# Transaction Functions
def withdraw():
    while True:
        try:
            clear()
            balance = read_balance()
            header()
            print("WITHDRAW\n".center(60, " "))
            print(f"Your current balance is ₱{balance:.2f}\n".center(60, " "))
            amount = int(input("                   Enter amount | ₱"))
            if amount <= 0:
                print("\nInvalid Amount. Please enter a positive value.".center(60, " "))
                footer()
                pause()
                break
            if not valid_amount(amount):
                print()
                print("Invalid amount. The machine only accepts multiples of 100.".center(60, " "))
                footer()
                pause()
                break
            if not isSameBank:
                total_amount = amount + 18.00
            else:
                total_amount = amount
            if total_amount > balance:
                print()
                print("Insufficient funds.".center(60, " "))

                if not isSameBank:
                    print("(Including ₱18.00 transaction fee)".center(60, " "))
                footer()
                pause()
                break
            if not isSameBank:
                print()
                print("₱18.00 transaction fee will be deducted.".center(60, " "))
            balance -= total_amount
            write_balance(str(int(balance)))
            print()
            print(f"You withdrew ₱{amount:.2f} from your account.".center(60, " "))
            if not isSameBank:
                print(f"Transaction fee: ₱18.00".center(60, " "))
            print()
            print(f"Your current balance is ₱{balance:.2f}".center(60, " "))
            footer()
            pause()
            return
        except ValueError:
            print()
            print("Please enter a valid number.".center(60, " "))
            footer()
            pause()
            break
def deposit():
    try:
        clear()
        balance = read_balance()
        header()
        print("DEPOSIT\n".center(60, " "))
        print(f"Your current balance is ₱{balance:.2f}\n".center(60, " "))
        amount = int(input("                   Enter amount | ₱"))
        print()
        if amount < 1:
            print("Invalid deposit amount.".center(60, " "))
            print()
            pause()
            return
        else:
            balance += amount
            write_balance(str(int(balance)))
            print(f"You deposited ₱{amount:.2f} to your account.".center(60, " "))
            print(f"Your updated balance is ₱{balance:.2f}\n".center(60, " "))
            footer()
        pause()
    except ValueError:
        print("\n")
        print("Please enter a valid number.".center(60, " "))
        print()
        pause()
        return
def check_balance():
    global isSameBank
    clear()
    balance = read_balance()
    if not isSameBank:
        balance -= 2.00
        write_balance(str(int(balance)))
    header()
    print("\n\n")
    print(f" Your Balance is ₱ {balance} \n".center(60, " "))
    print("\n\n")
    footer()
    pause()
def change_pin():
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        clear()
        header()
        print("CHANGE PIN\n".center(60, " "))
        current_pin = input("             Enter current PIN: ")
        if current_pin != read_pin():
            attempts += 1
            remaining = max_attempts - attempts
            print(f"Authentication failed. {remaining} attempts remaining.".center(60, " "))
            pause()
            if attempts >= max_attempts:
                print("Too many failed attempts. Returning to main menu.".center(60, " "))
                pause()
                return
            continue
        while True:
            clear()
            header()
            print("CHANGE PIN\n".center(60, " "))
            new_pin = input("             Enter new 6-digit PIN: ").strip()
            if new_pin == current_pin:
                print()
                print("New PIN must be different from current PIN.".center(60, " "))
                print()
                footer()
                pause()
                continue
            if len(new_pin) != 6 or not new_pin.isdigit():
                print()
                print("Invalid PIN format. Must be 6 digits.".center(60, " "))
                print()
                footer()
                pause()
                continue
            confirm_pin = input("             Confirm new PIN: ").strip()
            if new_pin != confirm_pin:
                print()
                print("PINs do not match. Please try again.".center(60, " "))
                print()
                footer()
                pause()
                continue
            write_pin(new_pin)
            print("\nPIN changed successfully!".center(60, " "))
            footer()
            pause()
            return

# ATM Main Function
def atm():
    card_registration()
    while True:
        clear()
        header()
        bank = bank_name()
        print(f"Welcome to {bank}".upper().center(60, " "))
        print()
        print("Are you a new user?".center(60, " "))
        print("[Y] Yes       [N] No".center(60, " "))
        print()
        user_type = input("                         Choice: ").upper()

        if user_type == "Y":
            register()
            break
        elif user_type == "N":
            log_in()
            break
        else:
            print("Invalid input. Please try again.".center(60, " "))
            pause()

# ATM Menu Function
def menu():
    while True:
        clear()
        header()
        username = user_name()
        print(f" Welcome {username}! PLease select transaction. \n".center(60, " "))
        print("         [1] Check Balance")
        print("         [2] Withdraw Amount")
        print("         [3] Deposit Amount")
        print("         [4] Change PIN")
        print("         [5] Exit\n")
        footer()
        choice = input("    Choice :  ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            deposit()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            clear()
            header()
            print("\n\n")
            print("Thank you for using the ATM.".center(60, " "))
            print("\n\n")
            footer()
            pause()
            exit()
        else:
            print("Invalid choice.")
            pause()

atm()