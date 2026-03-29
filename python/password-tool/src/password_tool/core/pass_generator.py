from password_tool.config import pass_len, pass_cap, pass_low, pass_num, pass_sym
import secrets
import string

# join random characters while meeting password requirements
def generate_password(min_len=pass_len, min_low=pass_low, min_cap=pass_cap, min_num=pass_num, min_sym=pass_sym):
    if pass_len < min_cap + min_low + min_num + min_sym:
        raise ValueError("Length too small for the constraints.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*" 
    all_chars = lower + upper + digits + symbols

    password = ''.join(secrets.choice(all_chars) for i in range(min_len))
    return password

generate_password()