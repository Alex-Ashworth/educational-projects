from .config import pass_len, pass_cap, pass_num, pass_sym

def is_symbol(char: str) -> bool:
    return not char.isalnum() and not char.isspace()

def chk_length(password: str) -> bool:
    if len(password) >= pass_len:
        return True

def chk_capital(password: str) -> bool:
    tally = []
    for char in password:
        if char.isupper():
            tally.append(char)
    if len(tally) >= pass_cap:
        return True

def chk_number(password: str) -> bool:
    tally = []
    for char in password:
        if char.isdigit():
            tally.append(char)
    if len(tally) >= pass_num:
        return True

def chk_symbol(password: str) -> bool:
    tally = []
    for char in password:
        if is_symbol(char):
            tally.append(char)
    if len(tally) >= pass_sym:
        return True
