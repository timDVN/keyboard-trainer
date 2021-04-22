import getch
import random
import time

f = open("in(out)put/input.txt", "r")


class stroka:
    def __init__(self):
        self.time = 0
        self.correct = 0  # количество правильно введённых символов
        self.item = ""  # строка, которую необходимо ввести
        self.wrong = 0  # кол-во ошибок
        self.length = 0  # длинна строки
        self.speed = 0  # скорость напечатания
        self.char = 0  # символ, считаный с ввода

    def item_decide(self):  # определение строки, которая будет вводиться
        text = f.readlines()  # массив из строк
        self.item = text[random.randint(0, len(text) - 1)]  # случайный элемент этого массива
        self.item = self.item[:-1]  # удаление символа '\n' из строки

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
        self.item_decide()
        self.set_length()
        self.print_str()
        self.time_start()
        while self.correct <= self.length - 1:
            self.is_correct()
        print("\n")
        self.time_end()
        self.speed_calc()
        self.print_result()
        self.saving()

    def saving(self):  # сохранение результатов
        print("Do yo want save  the result?(y/n)")
        answer = input()
        if answer == 'y':
            print("File:")
            name_file = input()
            save_file = open(name_file, "a+")
            save_file.write(str(self.time))
            save_file.write(' ')
            save_file.write(str(self.speed))
            save_file.write(' ' * 6)
            save_file.write(str(self.wrong))
            save_file.write(' ' * 6 + '\n')


trainer = stroka()
trainer.main_cycle()
