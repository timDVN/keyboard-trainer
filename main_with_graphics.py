import main
import pygame
import sys
import time

pygame.init()

HorizontalSize = 1000
VerticalSize = 1000
HorizontalCenter = HorizontalSize / 2
VerticalCenter = VerticalSize / 2
VerticalIndent = 150
HorizontalIndent = 100
LineHeight = 75
NumberOfLine = 0
screen = pygame.display.set_mode((1000, 1000))  # создание окна на экране устройства
surf = pygame.Surface((HorizontalSize - 2 * HorizontalIndent, LineHeight))
surf.fill((255, 255, 255))
screen.fill((200, 255, 200))
screen.blit(surf, (HorizontalIndent, VerticalIndent + LineHeight))


class KeyboardTrainer:
    def __init__(self):
        self.time = 0
        self.correct = 0  # number of first not entered element
        self.item = main.item_decide()  # string that you need to type
        self.wrong = 0  # quantity of mistakes
        self.length = 0
        self.speed = 0
        self.char = 0  # last entered element
        self.number = 0  # described below

    def time_start(self):  # начало отсчёта
        self.time = time.time()

    def time_end(self):  # расчётв времени
        self.time = time.time() - self.time

    def set_length(self):  # определение длинны строки
        self.length = len(self.item)

    def print_str(self):  # печать строки, которую надо ввести
        global NumberOfLine
        font = pygame.font.Font(None, LineHeight)  # шрифт
        text = font.render(self.item, True, (0, 100, 0))  # объект с текстом
        place = text.get_rect(center=(HorizontalCenter, VerticalIndent + LineHeight * NumberOfLine))  # положение текста
        NumberOfLine += 1
        screen.blit(text, place)  # вывод текста
        pygame.display.update()  # обновление окна

    def print_char(self):
        global NumberOfLine
        font = pygame.font.Font(None, LineHeight)  # шрифт
        if self.correct >= self.length:  # введена  вся строка
            text = font.render(self.item, True, (255, 100, 100))
        else:  # введена не вся строка
            text = font.render(self.item[:self.correct], True, (0, 0, 0))
        place = text.get_rect(topleft=(HorizontalIndent, VerticalIndent + LineHeight))
        # 0.5 + NumberOfLine - 1 т.к. размещение по topleft
        screen.blit(text, place)
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
        global NumberOfLine
        NumberOfLine += 2  # оставляем пустую строку после поля surface
        font = pygame.font.Font(None, LineHeight)  # шрифт
        text = font.render("time is" + str(self.time), True, (0, 100, 0))  # объект с тесктом
        place = text.get_rect(center=(HorizontalCenter, VerticalIndent + NumberOfLine * LineHeight))  # место
        NumberOfLine += 1
        screen.blit(text, place)  # вывод текста
        text = font.render("speed is" + str(self.speed), True, (0, 100, 0))  # -//-
        place = text.get_rect(center=(HorizontalCenter, VerticalIndent + NumberOfLine * LineHeight))  # -//-
        NumberOfLine += 1
        screen.blit(text, place)  # -//-
        text = font.render("number of mistakes is" + str(self.wrong), True, (0, 100, 0))  # -//-
        place = text.get_rect(center=(HorizontalCenter, VerticalIndent + NumberOfLine * LineHeight))  # -//-
        NumberOfLine += 1
        screen.blit(text, place)  # -//-
        pygame.display.update()  # обновление окна

    def main_cycle(self):
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
        self.ask_for_saving()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def ask_for_saving(self):
        global NumberOfLine
        font = pygame.font.Font(None, int(LineHeight * 0.75))  # шрифт
        text = font.render("Do yo want save the result(write in terminal)?(y/n)", True, (0, 100, 0))  # объект с текстом
        place = text.get_rect(center=(HorizontalCenter, VerticalIndent + NumberOfLine * LineHeight))  # место
        screen.blit(text, place)  # вывод
        pygame.display.update()  # обновление
        answer = input()
        if answer == 'y':
            main.saving(self.time, self.wrong, self.speed)
        else:
            return 0


trainer = KeyboardTrainer()
trainer.main_cycle()
