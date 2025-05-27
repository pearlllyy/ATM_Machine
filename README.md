
# ATM Machine Simulator

This project is for our CC203: Computer Programming 2 course, this simulates an Automated Teller Machine (ATM) system that allows users to perform common banking operations through a command-line interface.


## Guidelines
**Instructions:**
- should have an initial balance of 10,000
- should consider a new or current user
- should consider different banks (Landbank, BPI, DBP, and BDO)
- if the user has a different bank, will charge P18.00 for each "withdraw"
- if the user has a different bank, will charge P2.00 for each 'check balance'
- will only dispense an amount of P1000, P500, P100
- will display 'insufficient fund' if 'current balance' is less than 'withdraw amount'
- will display 'invalid amount' if 'withdraw amount' is not valid.
  - negative or zero withdraw and deposit amount
  - amount to be dispensed is not divisible by the dispense amount
- will store and retrieve PIN on a 'pin.txt' file.
- will store and retrieve 'current balance' on 'balance.txt' file

**The program,**
- should ask if the user is an existing user or a new user.
- should ask to save a NEW PIN (6 characters) if the user is a new user.
- should ask for a PIN (6 characters)
- will have five(5) features.
  - Check Balance
  - Withdraw Fund(s)
  - Deposit Fund(s)
  - Change PIN
  - Exit
## Overview

The ATM Simulator is a Python application that replicates the functionality of a real ATM. It provides a text-based interface for users to perform banking operations such as checking balance, withdrawing money, depositing money, and changing their PIN.
## Features

- **Card Registration**: Users can select their bank (BDO or other banks)  
- **User Registration**: New users can create an account with a username and PIN  
- **Secure Login**: PIN-based authentication with a maximum of three attempts  
- **Transaction Types**:
  - **Balance Inquiry**: Check account balance  
  - **Withdrawal**: Withdraw money in multiples of 100  
  - **Deposit**: Add money to account  
  - **PIN Change**: Update account PIN with verification  

- **Bank Interoperability**: Supports both same-bank (on-us) and other-bank (off-us) transactions  
- **Transaction Fees**:
  - Off-us balance inquiry: ₱2.00 fee  
  - Off-us withdrawal: ₱18.00 fee  

## Technical Implementation

The system uses text files to store user data:

- `pin.txt`: Stores the user's PIN  
- `balance.txt`: Stores the account balance  
- `user.txt`: Stores the username  
- `bank.txt`: Stores the bank name  

## How to Use

1. **Start the application**: Run `python ATM.py`  
2. **Card Registration**: Select your bank (BDO or other)  
3. **User Registration/Login**: Register as a new user or log in with your PIN  
4. **Main Menu**: Choose from the available transaction options:
   - Check Balance  
   - Withdraw Amount  
   - Deposit Amount  
   - Change PIN  
   - Exit  
5. **Complete Transactions**: Follow the on-screen prompts to complete your chosen transaction  

## Requirements

- Python 3.x  
- Operating System: Windows, macOS, or Linux  

## Code Structure

The code is organized into several functional sections:

- File handling functions (read/write operations)  
- User interface functions (display formatting)  
- Registration and login functions  
- Transaction processing functions (withdraw, deposit, etc.)  
- Main ATM control flow  

## Future Improvements

Potential enhancements for future versions:

- Transaction history logging  
- Multiple user accounts  
- Enhanced security features  
- Graphical user interface  
- Database integration instead of file storage  

## License

This project is for educational purposes only.

## Author

This ATM simulator was created as a demonstration of programming concepts including file Input/Output, user authentication, and transaction processing in Python.
