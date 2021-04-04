import time
import random
import getch
# import pygame
import sys

# pygame.init()

# sc = pygame.display.set_mode((1000, 700))
# surf = pygame.Surface((800, 75))
# surf.fill((255, 255, 255))
# sc.fill((200, 255, 200))
# sc.blit(surf, (100, 200))

f = open("input.txt", "r")


class stroka:
    def __init__(self):
        self.time = 0
        self.correct = 0  # number of first not enetered element
        self.item = ""  # string rhat you need to type
        self.wrong = 0  # quantity of mistakes
        self.lenght = 0
        self.speed = 0
        self.c = 0  # last entered element

    def item_deciding(self):
        text = f.readlines()
        self.item = text[random.randint(0, len(text) - 1)]
        self.item = self.item[:-1]

    def time_start(self):
        self.time = time.time()

    def time_end(self):  # calculating of time
        self.time = time.time() - self.time

    def set_lenght(self):
        self.lenght = len(self.item)

    def print_str(self):
        print(self.item)
        # font = pygame.font.Font(None, 72)
        # text = font.render(self.item, True, (0, 100, 0))
        # place = text.get_rect(center=(500, 150))
        # sc.blit(text, place)
        # pygame.display.update()

    def get_c(self):
        self.c = getch.getch()

    def is_correct(self):
        self.get_c()
        if self.c == self.item[self.correct]:
            self.correct = self.correct + 1
            print(self.c)
        else:
            self.wrong = self.wrong + 1

    def speed_calc(self):
        self.speed = self.lenght / self.time

    def print_result(self):
        print("time is", self.time)
        print("speed is", self.speed)
        print("number of mistakes is ", self.wrong)

    def write_res(self, file):
        file.write(self.time, ' ', self.speed)

    def main_cikle(self):
        self.item_deciding()
        self.set_lenght()
        self.print_str()
        self.time_start()
        while self.correct <= self.lenght - 1:
            self.is_correct()
        print("\n")
        self.time_end()
        self.speed_calc()
        self.print_result()
        self.saving()

    def saving(self):
        print("Do yo want save  the result?(y/n)")
        answer = input()
        if answer == 'y':
            print("File:")
            name_file = str(input())
            save_file = open(name_file, "a+")
            save_file.write(str(self.time))
            save_file.write(' ')
            save_file.write(str(self.speed))
            save_file.write('      ')
            save_file.write(str(self.wrong))
            save_file.write('\n')


a = stroka()
a.main_cikle()
