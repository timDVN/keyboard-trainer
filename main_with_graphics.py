import getch
import pygame
import random
import sys
import time

pygame.init()

sc = pygame.display.set_mode((1000, 1000))
surf = pygame.Surface((800, 75))
surf.fill((255, 255, 255))
sc.fill((200, 255, 200))
sc.blit(surf, (100, 200))

f = open("NoCodeFiles/input.txt", "r")


class stroka:
    def __init__(self):
        self.time = 0
        self.correct = 0  # number of first not enetered element
        self.item = ""  # string rhat you need to type
        self.wrong = 0  # quantity of mistakes
        self.lenght = 0
        self.speed = 0
        self.c = 0  # last entered element
        self.number = 0

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
        font = pygame.font.Font(None, 72)
        text = font.render(self.item, True, (0, 100, 0))
        place = text.get_rect(center=(500, 150))
        sc.blit(text, place)
        pygame.display.update()

    def print_c(self):
        font = pygame.font.Font(None, 72)
        if self.correct >= self.lenght:
            text = font.render(self.item, True, (255, 100, 100))
        else:
            text = font.render(self.item[:self.correct], True, (0, 0, 0))
        place = text.get_rect(topleft=(100, 400))
        sc.blit(text, place)
        pygame.display.update()

    def is_correct(self):
        if self.c == self.item[self.correct]:
            self.correct = self.correct + 1
            self.print_c()
        else:
            self.wrong = self.wrong + 1

    def speed_calc(self):
        self.speed = self.lenght / self.time

    def print_result(self):
        font = pygame.font.Font(None, 50)
        text = font.render("time is" + str(self.time), True, (0, 100, 0))
        place = text.get_rect(center=(500, 600))
        sc.blit(text, place)
        text = font.render("speed is" + str(self.speed), True, (0, 100, 0))
        place = text.get_rect(center=(500, 650))
        sc.blit(text, place)
        text = font.render("number of mistakes is" + str(self.wrong), True, (0, 100, 0))
        place = text.get_rect(center=(500, 700))
        sc.blit(text, place)
        pygame.display.update()

    def main_cikle(self):
        self.item_deciding()
        self.set_lenght()
        self.print_str()
        self.time_start()
        while self.correct <= self.lenght - 1:
            events = pygame.event.get()
            #events_r = events[::-1]
            for i in range(len(events) - self.number):
                if events[i].type == pygame.KEYDOWN and events[i].key <= ord('z'):
                    #number = len(events) - events_r.index(i) - 1
                    if i > self.number:
                        self.c = chr(events[i].key)
                        self.is_correct()
                        self.number = i
        self.time_end()
        self.speed_calc()
        self.print_result()
        self.saving()

    def saving(self):
        font = pygame.font.Font(None, 50)
        text = font.render("Do yo want save the result?(y/n)", True, (0, 100, 0))
        place = text.get_rect(center=(500, 750))
        sc.blit(text, place)
        pygame.display.update()
        answer = input()
        if answer == 'y':
            print("File(write in terminal):")
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
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
