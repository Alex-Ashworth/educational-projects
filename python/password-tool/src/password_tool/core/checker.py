from password_tool.utils import is_symbol, check_length, check_capital, check_lower, check_number, check_symbol
from password_tool.config import pass_len, pass_cap, pass_low, pass_num, pass_sym
from getpass import getpass

# ensure password meets complexity requirements
def check_pass(password: str) -> bool:
    if not check_length(password):
        print(f"\nYour password is too short. Please try again using a password longer than {pass_len} characters. ")
        return False

    if not check_capital(password):
        print(f"\nYour password is missing at least {pass_cap} capital letter. Please try again. ")
        return False

    if not check_lower(password):
        print(f"\nYour password is missing at least {pass_low} lowercase letter. Please try again. ")
        return False

    if not check_number(password):
        print(f"\nYour password is missing at least {pass_num} number. Please try again. ")
        return False

    if not check_symbol(password):
        print(f"\nYour password is missing at least {pass_sym} symbol. Please try again. ")
        return False
    else:
        print("\nPassword Accepted. Password meets all complexity requirements. ")
        return True
    
def run():
    def intro():
        print(f"\nPlease enter a password that is {pass_len} characters in length, includes at least {pass_cap} capital letter, at least {pass_low} lowercase letter, at least {pass_num} number, and at least {pass_sym} symbol. ($@!%&..)")
    intro()
    PASS = getpass("\nEnter your password: ")
    
    while not check_pass(password=PASS):
        intro()
        PASS = getpass("\nEnter your password: ")
    return True