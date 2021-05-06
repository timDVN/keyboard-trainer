import getch
import random
import time


class KeyboardTrainer:
    def __init__(self):
        self.time = 0
        self.correct = 0  # количество правильно введённых символов
        self.item = item_decide()  # строка, которую необходимо ввести
        self.wrong = 0  # кол-во ошибок
        self.length = 0  # длинна строки
        self.speed = 0  # скорость напечатания
        self.char = 0  # символ, считаный с ввода

    def time_start(self):  # начало отсчёта времени
        self.time = time.time()

    def time_end(self):  # окончание отсчёта времени
        self.time = time.time() - self.time

    def set_length(self):  # определение длинны строки
        self.length = len(self.item)

    def print_str(self):  # печать строки
        print(self.item)

    def get_char(self):  # считывание символа с ввода
        self.char = getch.getch()

    def is_correct(self):  # проверка введённого элемента на корректность
        self.get_char()
        if self.char == self.item[self.correct]:
            self.correct = self.correct + 1  # увеличение количества правильно введённых элементов
            print(self.char)
        else:
            self.wrong = self.wrong + 1  # увеличкние количества ошибок

    def speed_calc(self):  # определение скорости
        self.speed = self.length / self.time

    def print_result(self):  # вывод результатов
        print("time is", self.time)
        print("speed is", self.speed)
        print("number of mistakes is ", self.wrong)

    def main_cycle(self):  # главный цикл, который включает в себя весь функционал программы
        self.set_length()
        self.print_str()
        self.time_start()
        while self.correct <= self.length - 1:
            self.is_correct()
        print("\n")
        self.time_end()
        self.speed_calc()
        self.print_result()
        self.ask_for_saving()

    def ask_for_saving(self):  # сохранение результатов
        print("Do yo want save  the result?(y/n)")
        answer = input()
        if answer == 'y':
            saving(self.time, self.wrong, self.speed)


def saving(duration, mistakes, speed):
    print("File:")
    name_file = input()
    with open(name_file, "a+") as save_file:
        save_file.write(str(duration))
        save_file.write(' ')
        save_file.write(str(speed))
        save_file.write(' ' * 6)
        save_file.write(str(mistakes))
        save_file.write('\n')


def item_decide():  # определение строки, которая будет вводиться
    with open("in(out)put/input.txt", "r") as inputfile:
        text = inputfile.readlines()  # массив из строк
    item = text[random.randint(0, len(text) - 1)]  # случайный элемент этого массива
    item = item[:-1]  # удаление символа '\n' из строки
    return item


trainer = KeyboardTrainer()
trainer.main_cycle()
