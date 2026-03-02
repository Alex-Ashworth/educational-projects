from ..utils import is_symbol, chk_length, chk_capital, chk_number, chk_symbol
from ..config import pass_len, pass_cap, pass_num, pass_sym
from getpass import getpass

def chk_pass(password: str) -> bool:
    if not chk_length(password):
        print(f"\nYour password is too short. Please try again using a password longer than {pass_sym} characters. ")
        return False

    if not chk_capital(password):
        print(f"\nYour password is missing at least {pass_sym} capital letter. Please try again. ")
        return False

    if not chk_number(password):
        print(f"\nYour password is missing at least {pass_sym} number. Please try again. ")
        return False

    if not chk_symbol(password):
        print(f"\nYour password is missing at least {pass_sym} symbol. Please try again. ")
        return False
    else:
        print("\nPassword Accepted. Password meets all complexity requirements. ")
        return True
    
def run():
    def intro():
        print(f"\nPlease enter a password that is {pass_len} characters in length, includes at least {pass_cap} capital letter, at least {pass_num} number, and at least {pass_sym} symbol. ($@!%&..)")
    intro()
    PASS = getpass("\nEnter your password: ")
    
    while not chk_pass(password=PASS):
        intro()
        PASS = getpass("\nEnter your password: ")
    return True