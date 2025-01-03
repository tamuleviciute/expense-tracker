import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Expense Tracker")

all = SHEET.worksheet("All")

data = all.get_all_values()

print(data)

def get_expense_data():
    """
    Get expense data from the user.
    Validate input and re-prompt until valid data is provided.
    """
    print("Welcome to the Expense Tracker!")
    print("Please provide the following details about your expense.")
    print("Format: Date (YYYY-MM-DD), Category, Amount, Description, Payment Method.")
    print("Example: 2024-12-23, Food, 34.15, Grocery shopping, Credit card\n.")

    while True:
        user_input = input("Enter your expense details: ")
        expense_data = user_input.split(", ")

        if validate_expense_input(expense_data):
            print("\nYour input has been validated\n")
            return expense_data
        
        else: 
            print("Please try entering expense details again\n")

def validate_expense_input(data):
    """
    Validate the users expense input.
    Check that the input contains exactly 5 fields.
    Validate the date format.
    Ensure the amount is a positive number.
    """
    if len(data) != 5:
        print("Error: Please provide exactly 5 fields (Date, Category, Amount, Description, Payment Method).")
        return False
    
    try: 
        from datetime import datetime
        datetime.strptime(data[0], "%Y-%m-%d")
    

        amount = float(data[2]) 
        if amount <= 0:
            print("Error: Amount must be a positive number.")
            return False


    except ValueError as e: 
        print(f"Error: {e}")
        return False

    return True


get_expense_data()



