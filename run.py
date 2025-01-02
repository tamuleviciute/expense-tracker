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
    print("Format: Date (YYYY-MM-DD), Category, Amount, Description, Payment Method")
    print("Example: 2024-12-23, Food, 34.15, Grocery shopping, Credit card\n")

    while True:
        user_input = input("Enter your expense details: ")
        expense_data = user_input.split(", ")

        if validate_expense_input(expense_data):
            print("\nYour input has been validated\n")
            return expense_data
        
        else: 
            print("Please try entering expense details again\n")

get_expense_data()



