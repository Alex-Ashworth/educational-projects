import secrets
from pathlib import Path
from password_tool.config import phrase_len, separator


# T
WORD_PATH = Path(__file__).resolve().parent.parent / "data" / "wordlist.txt"
def generate_passphrase():
    with open(WORD_PATH, "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]
        digits = '0123456789'
        phrase = ''
        for i in range(phrase_len):
            x = ''.join([secrets.choice(words), secrets.choice(digits), separator])
            phrase += x
        phrase = phrase[:-1]
        print(phrase)
    
generate_passphrase()