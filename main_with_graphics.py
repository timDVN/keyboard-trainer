import pygame
import random
import sys
import time

pygame.init()

sc = pygame.display.set_mode((1000, 1000))  # создание окна на экране устройства
surf = pygame.Surface((800, 75))
surf.fill((255, 255, 255))
sc.fill((200, 255, 200))
sc.blit(surf, (100, 200))

inputfile = open("in(out)put/input.txt", "r")


class stroka:
    def __init__(self):
        self.time = 0
        self.correct = 0  # number of first not entered element
        self.item = ""  # string that you need to type
        self.wrong = 0  # quantity of mistakes
        self.length = 0
        self.speed = 0
        self.char = 0  # last entered element
        self.number = 0  # described below

    def item_decide(self):  # определение строки, которая будет вводиться
        text = inputfile.readlines()  # массив из строк
        self.item = text[random.randint(0, len(text) - 1)]  # случайный элемент этого массива
        self.item = self.item[:-1]  # удаление символа '\n' из строки

    def time_start(self):  # начало отсчёта
        self.time = time.time()

    def time_end(self):  # расчётв времени
        self.time = time.time() - self.time

    def set_length(self):  # определение длинны строки
        self.length = len(self.item)

    def print_str(self):  # печать строки, которую надо ввести
        font = pygame.font.Font(None, 72)  # шрифт
        text = font.render(self.item, True, (0, 100, 0))  # объект с текстом
        place = text.get_rect(center=(500, 150))  # положение текста
        sc.blit(text, place)  # вывод текста
        pygame.display.update()  # обновление окна

    def print_char(self):
        font = pygame.font.Font(None, 72)  # шрифт
        if self.correct >= self.length:  # введена  вся строка
            text = font.render(self.item, True, (255, 100, 100))
        else:  # введена не вся строка
            text = font.render(self.item[:self.correct], True, (0, 0, 0))
        place = text.get_rect(topleft=(100, 220))
        sc.blit(text, place)
        pygame.display.update()

    def is_correct(self):  # проверка введённого символа на корректность
        if self.char == self.item[self.correct]:
            self.correct = self.correct + 1  # увеличение количества правильно введённых символов
            self.print_char()
        else:
            self.wrong = self.wrong + 1  # увеличение количества ошибок

    def speed_calc(self):
        self.speed = self.length / self.time

    def print_result(self):
        font = pygame.font.Font(None, 50)  # шрифт
        text = font.render("time is" + str(self.time), True, (0, 100, 0))  # объект с тесктом
        place = text.get_rect(center=(500, 600))  # место
        sc.blit(text, place)  # вывод текста
        text = font.render("speed is" + str(self.speed), True, (0, 100, 0))  # -//-
        place = text.get_rect(center=(500, 650))  # -//-
        sc.blit(text, place)  # -//-
        text = font.render("number of mistakes is" + str(self.wrong), True, (0, 100, 0))  # -//-
        place = text.get_rect(center=(500, 700))  # -//-
        sc.blit(text, place)  # -//-
        pygame.display.update()  # обновление окна

    def main_cycle(self):
        self.item_decide()
        self.set_length()
        self.print_str()
        self.time_start()
        while self.correct <= self.length - 1:  # пока введена не вся строка
            events = pygame.event.get()  # лист с действиями
            for i in range(
                    len(events) - self.number):
                # перебор событий из листа, которые происходили после введения последнего считанного элемента
                if events[i + self.number].type == pygame.KEYDOWN and events[i + self.number].key <= ord(
                        'z'):  # действие - нажатие клавиши
                    self.char = chr(events[i + self.number].key)
                    self.is_correct()
                    self.number = i + self.number  # новый номер последнего считанного элемента
        self.time_end()
        self.speed_calc()
        self.print_result()
        self.saving()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def saving(self):
        font = pygame.font.Font(None, 50)  # шрифт
        text = font.render("Do yo want save the result(write in terminal)?(y/n)", True, (0, 100, 0))  # объект с текстом
        place = text.get_rect(center=(500, 750))  # место
        sc.blit(text, place)  # вывод
        pygame.display.update()  # обновление
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
            save_file.write('\n')
        else:
            return 0


trainer = stroka()
trainer.main_cycle()
