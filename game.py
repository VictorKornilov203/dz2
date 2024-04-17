import random

nickname = input("Введите ваш никнейм: ")

print("Правила игры:")
print("ПК загадывает 4-значное число")
print("Вы должны ввести число от 0 до 9 и угадать хотя бы 1 цифру из числа загаданного компьютером")
print("Если правильно вам начисляется 10 очков")
print("Если неправильно у вас отнимается 1 жизнь из 3")
print("Если у вас закончатся жизни, вы проигрываете")
print("Вы можете выйти из игры в любой момент нажав клавишу E ")
print("Перед выходом вам будет показан ваш рекорд")

def play_game():
    score = 0
    lives = 3
    record = 0

    while True:
        secret_number = random.randint(1000, 9999)
        guess = input("Введите число от 0 до 9: ")

        if guess == "E":
            print(f"Ваш рекорд: {record} очков")
            break

        is_correct = False
        for digit in str(guess):
            if digit in str(secret_number):
                is_correct = True
                break

        if is_correct:
            score = score + 10
            print("Правильно! Вы получаете 10 очков.")
        else:
            lives = lives - 1
            print(f"Неправильно! У вас осталось {lives} жизней.")

        if lives == 0:
            print("Вы проиграли")
            print(f"Ваш счет: {score} очков")
            if score > record:
                record = score
            break

    return record

while True:
    answer = input("Хотите сыграть еще раз? (да/нет): ")
    if answer.lower() != 'да':
        break
    record = play_game()