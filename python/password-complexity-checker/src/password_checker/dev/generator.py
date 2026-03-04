from ..config import pass_len, pass_cap, pass_low, pass_num, pass_sym
import secrets
import string

def generate_password(min_length=pass_len, min_cap=pass_cap, min_num=pass_num, min_sym=pass_sym):
    if length < pass_cap + pass_low + pass_num + pass_sym:
        raise ValueError("Length too small for the constraints")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@$%^&*()_+-=[]{}.,?~`;:" 
    all_chars = lower + upper + digits + symbols

    chars = [
        secrets.choice(lower)
    ]

