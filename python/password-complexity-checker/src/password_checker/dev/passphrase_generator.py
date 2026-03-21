import secrets
from pathlib import Path
from password_checker.config import phrase_len

WORD_PATH = Path(__file__).resolve().parent / "wordlist.txt"

with open(WORD_PATH, "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]
    digits = '0123456789'
    phrase = ''
    for i in range(phrase_len):
        x = ''.join([secrets.choice(words), secrets.choice(digits), '-'])
        phrase += x
    phrase = phrase[:-1]
    print(phrase)
    

# TODO parse string and add symbols, etc