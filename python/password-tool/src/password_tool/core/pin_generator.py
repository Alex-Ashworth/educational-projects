import secrets
from password_tool.config import pin_len

def generate_pin(pin_len = pin_len):
    digits = '0123456789'
    pin = ''.join(secrets.choice(digits) for i in range(pin_len))
    print(pin)

generate_pin()