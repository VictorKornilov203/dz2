
import random
import string

def generate_passwords(length, use_digits=False, use_uppercase=False, use_symbols=False):
    symbols = list(string.ascii_lowercase + string.digits)
    if use_uppercase:
        symbols += list(string.ascii_uppercase)
        
    if use_digits:
        symbols += list(string.digits)
        
    if use_symbols:
        symbols += list(string.punctuation)
        
    passwords = []
    for _ in range(5):
        password = ""
        for _ in range(length):
            random_symbol = random.choice(symbols)
            password += random_symbol
        passwords.append(password)

    print("Вот 5 случайных паролей:")
    for password in passwords:
        print(password)

length = int(input("Введите длину пароля: "))
use_uppercase = input("Включать ли заглавные буквы в пароль (да/нет)? ").lower() == "да"
use_digits = input("Включать ли цифры в пароль (да/нет)? ").lower() == "да"
use_symbols = input("Включать ли символы в пароль (да/нет)? ").lower() == "да"

generate_passwords(length, use_uppercase, use_digits, use_symbols)