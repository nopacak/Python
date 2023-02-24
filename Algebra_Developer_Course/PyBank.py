# BANK ACCOUNT SIMULATION

import datetime
import os
import random

#------------------------------
# GLOBAL VARIABLES
#------------------------------

choice = -1

# Company information

company_name = ""
company_address = ""
postal_code = ""
city = ""
tax_id = ""
manager_name = ""

# Account information
# Account number format: BA-YEAR-MONTH-ID (5 DIGIT ID)

currency = ""
account_no = ""
balance = 0.00

# Transaction information

transaction_id = ""
transactions = {}
total_deposit = 0.00
total_withdrawal = 0.00

#------------------------------
# FUNCTIONS
#------------------------------

def clear() -> None:
    """clears the console screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def title_print() -> None:
    """Prints out the application title
    """
    print("*" * 65)
    print("PyBANK ALGEBRA\n".center(65))


def main_menu() -> int:
    """Prints main menu and returns user's choice

    Returns:
        int: User's choice (1, 2, 3, 4, ,5 or 0)
    """
    clear()
    choice = -1
    global account_no
    title_print()
    print("MAIN MENU\n\n".center(65))
    if account_no == "":
        print("1. Create New Account")
    else:
        print("1. Update Account")
    print("2. Account Balance")
    print("3. Transaction History")
    print("4. Deposit")
    print("5. Withdrawal")
    print("0. Exit")

    print("_" * 65)

    if account_no == "":
        while choice != 1 and choice != 0:
            print("Account doesn't exist. Please create new account, thank you!")
            print("_" * 65)
            choice = int(input("Your Menu Selection:\t"))
    else:
        print("Please select the number in front of one of the menu options, thank you!")
        print("_" * 65)
        choice = int(input("Your Menu Selection:\t"))

    return choice


def generate_account_number() -> str:
    """Return account number.

    Returns:
        str: Account number in 'BA-YYYY-MM-00001' format
    """
    global account_no

    # ensure two digit for month
    acc_date = datetime.datetime.now().strftime("-%Y-%m-")

    # ensure 5 digit for id
    acc_id = str(random.randrange(1, 10*5)).zfill(5)

    account_no = "BA" + acc_date + acc_id

    return account_no


def open_account() -> str:
    """Prints create account menu and prompts user for data input

    Returns:
        str: Account details
    """

    global choice
    global account_no
    global company_name
    global company_address
    global postal_code
    global city
    global tax_id
    global manager_name
    global currency
    save = ""

    generate_account_number()

    while company_name == "" or company_address == "" or postal_code == "" or city == "" or tax_id == "" or manager_name == "" or currency == "" or save == "":
        clear()
        title_print()
        print("CREATE ACCOUNT\n".center(65))    
        print("Account owner details\n".center(65))  
        print(f"\n{'Company Name:':<30}{company_name:>20}", 
              f"\n{'Company Address:':<30}{company_address:>20}",
              f"\n{'Postal Code:':<30}{postal_code:>20}",
              f"\n{'City:':<30}{city:>20}", 
              f"\n{'Tax ID:':<30}{tax_id:>20}",
              f"\n{'Account Manager:':<30}{manager_name:>20}\n")

        if company_name == "":
            company_name = str(input("Please enter company name:\t"))
        elif company_address == "":
            company_address = str(input("Please enter company address:\t"))
        elif postal_code == "":
            postal_code = str(input("Please enter postal code:\t"))
        elif city == "":
            city = str(input("Please enter city:\t"))
        elif tax_id == "":
            tax_id = str(input("Please enter company TAX ID (must have 13 digits):\t"))
            if len(tax_id) != 13 or str.isdigit(tax_id) == False:
                tax_id = ""
        elif manager_name == "":
            manager_name = str(input("Please enter account manager name:\t"))
        elif currency == "" or currency not in {"HRK", "EUR"}:
            currency = str(input("Please enter account currency (HRK or EUR):\t").upper())
        else:
            save = str(input("Save data? (y/n)").lower())
            if save == "y":
                clear()
                title_print()
                print("CREATE ACCOUNT\n".center(65))
                print(f"Account data for company: {company_name} are successfully saved in our database!")
                input("Press any key to return to the main menu \t")
                choice = main_menu()
            else:
                account_no = ""
                company_name = ""
                company_address = ""
                postal_code = ""
                city = ""
                tax_id = ""
                manager_name = ""
                currency = ""
                choice = main_menu()


def update_account() -> str:
    """Prints out update account menu and prompts user for input

    Returns:
        str: Updated account details (if any)
    """

    global choice
    global account_no
    global company_name
    global company_address
    global postal_code
    global city
    global tax_id
    global manager_name
    global currency
    update_choice = -1

    while update_choice != 0:

        clear()
        title_print()
        print("UPDATE ACCOUNT\n".center(65))    
        print("Account owner details\n".center(65))  
        print(f"\n{'1. Company Name:':<30}{company_name:>20}", 
              f"\n{'2. Company Address:':<30}{company_address:>20}",
              f"\n{'3. Postal Code:':<30}{postal_code:>20}",
              f"\n{'4. City:':<30}{city:>20}", 
              f"\n{'5. Tax ID:':<30}{tax_id:>20}",
              f"\n{'6. Account Manager:':<30}{manager_name:>20}\n")
        update_choice = int(input("Please select data to be updated (1 to 6) or press 0 to go back to main menu:\t"))
        if update_choice == 1:
            company_name = str(input("Please enter new company name:\t"))
        elif update_choice == 2:
            company_address = str(input("Please enter new company address:\t"))
        elif update_choice == 3:
            postal_code = str(input("Please enter new postal code:\t"))
        elif update_choice == 4:
            city = str(input("Please enter new city:\t"))
        elif update_choice == 5:
            tax_id = str(input("Please enter new company TAX ID (must have 13 digits):\t"))
            if len(tax_id) != 13 or str.isdigit(tax_id) == False:
                tax_id = ""
        elif update_choice == 6:
            manager_name = str(input("Please enter new account manager name:\t"))
        elif update_choice == 0:
            choice = main_menu()


def display_account_balance() -> None:
    """Prints out account balance
    """

    global choice
    global account_no
    global balance
    global currency
    
    clear()
    title_print()
    print("CURRENT ACCOUNT BALANCE\n\n".center(65))
    print(f"Account Number:\t{account_no}")
    print(f"Date and Time:\t{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
    print(f"Current Account Balance:\t{balance:.2f} {currency}")
    print("_" * 65)
    input("Press any key to return to the main menu \t")
    choice = main_menu()



def deposit() -> dict:
    """Prints out deposit page and prompts for user input

    Returns:
        dict: appended transactions dictionary
    """

    global transaction_id
    global transactions
    global balance 
    global currency
    global choice
    global total_deposit
    deposit_amount = ""
    save = ""

    while save == "":

        clear()
        title_print()
        print("CURRENT ACCOUNT BALANCE\n\n".center(65))
        print(f"Account Number:\t{account_no}")
        print(f"Current Account Balance:\t{balance:.2f} {currency}\n")

        deposit_amount = float(input("Please write the amount you wish to deposit to your account.\nNOTE! Please use decimal point (.), not a comma (,)\n\t"))
        balance = balance + deposit_amount
        total_deposit = total_deposit + deposit_amount
        transaction_id = str(random.randrange(1, 10*8)).zfill(8)
        transactions[transaction_id] = [deposit_amount, datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')]

        save = str(input("Complete deposit transaction? (y/n)").lower())
        if save == "y":
            clear()
            title_print()
            print("DEPOSIT\n".center(65))
            print(f"Your deposit of {total_deposit:.2f} has been saved!")
            input("Press any key to return to the main menu \t")
            choice = main_menu()
            total_deposit = 0.00
        else:
            deposit()

    return transactions



def withdraw() -> dict:
    """Prints out withdrawal page and prompts for user input

    Returns:
        dict: appended transactions dictionary
    """

    global transaction_id
    global transactions
    global balance 
    global currency
    global total_withdrawal
    global choice
    withdrawal_amount = ""
    save = ""

    while save == "":
        clear()
        title_print()
        print("CURRENT ACCOUNT BALANCE\n\n".center(65))
        print(f"Account Number:\t{account_no}")
        print(f"Current Account Balance:\t{balance:.2f} {currency}\n")

        withdrawal_amount = float(input("Please write the amount you wish to withdraw from your account.\nNOTE! Please use decimal point (.), not a comma (,)\n\t"))
        balance = balance - withdrawal_amount
        total_withdrawal = total_withdrawal + withdrawal_amount
        transaction_id = str(random.randrange(1, 10*8)).zfill(8)
        transactions[transaction_id] = ["-" + str(withdrawal_amount), datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')]

        save = str(input("Complete withdrawal transaction? (y/n)").lower())
        if save == "y":
            clear()
            title_print()
            print("WITHDRAWAL\n".center(65))
            print(f"Your withdrawal of {total_withdrawal:.2f} has been saved!")
            input("Press any key to return to the main menu \t")
            choice = main_menu()
            total_withdrawal = 0.00
        else:
            withdraw()

    return transactions



def display_transaction_history() -> None:
    """Prints out transactions dictionary
    """

    global transactions
    global balance 
    global currency
    global choice

    clear()
    title_print()
    print("CURRENT ACCOUNT BALANCE\n\n".center(65))
    print(f"Account Number:\t{account_no}".center(62))
    print(f"Current Account Balance:\t{balance:.2f} {currency}\n\n".center(65))
    print("Transaction ID\t\tAmount\t\tTimestamp")

    for key, value in transactions.items():
        print(f"\n  {key}", end = "\t\t")
        for element in value:
            print(f"{element}", end = "\t\t")

    input("\n\nPress any key to return to the main menu \t")
    choice = main_menu()

#------------------------------
# MAIN PROGRAM
#------------------------------

choice = main_menu()

while choice != 0:
    if choice == 1 and account_no == "":
        open_account()
        pass
    elif choice == 1 and account_no != "":
        update_account()
        pass
    elif choice == 2:
        display_account_balance()
        pass
    elif choice == 3:
        display_transaction_history()
        pass
    elif choice == 4:
        deposit()
        pass
    elif choice == 5:
        withdraw()
        pass
