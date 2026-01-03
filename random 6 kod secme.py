import random
import string

def generate_code(length=6):
    if length < 2:
        raise ValueError("Hatali kod")
    letters = string.ascii_letters
    digits = string.digits

    
    code_chars = []
    code_chars.append(random.choice(letters))
    code_chars.append(random.choice(digits))

    
    all_chars = letters + digits
    for _ in range(length - 2):
        code_chars.append(random.choice(all_chars))

    
    random.shuffle(code_chars)
    return ''.join(code_chars)


print(generate_code())  