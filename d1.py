"""Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать
“больше” или “меньше” после каждой попытки"""

from random import randint


class GuessNumberGame:
    def __init__(self):
        self.LOWER_LIMIT = 0
        self.UPPER_LIMIT = 1000
        self.NUMBER_OF_ATTEMPTS = 10
        self.secret_number = randint(self.LOWER_LIMIT, self.UPPER_LIMIT)

    def play(self):
        i = 0
        flag = False

        while i < self.NUMBER_OF_ATTEMPTS:
            print("Осталось " + str(self.NUMBER_OF_ATTEMPTS - i) + " попыток")
            try:
                user_num = int(input("Введите число - "))
                if user_num != self.secret_number:
                    if user_num < self.secret_number:
                        print("Введенное число меньше нужного")
                    else:
                        print("Введенное число больше нужного")
                    i += 1
                else:
                    flag = True
                    break
            except ValueError:
                print("Нужно вводить число")

        if flag:
            print("Вы угадали")
        else:
            print("Вы НЕ угадали")


if __name__ == "__main__":
    game = GuessNumberGame()
    game.play()
