import time
import random
import pygame
import sys
pygame.init()

sc = pygame.display.set_mode((1000, 700))
surf = pygame.Surface((800, 75))
surf.fill((255, 255, 255))
sc.fill((200, 255, 200))
sc.blit(surf, (100, 200))

f = open("input.txt", "r")

def decorator(funk):
    def wrap(a):


    return wrap



class stroka:
    def __init__(self):
        self.time = 0
        self.correct = 0
        self.item = ""
        self.wrong = 0
        self.lenght = 0
        self.accuracy = 0
        self.speed = 0
        self.c = 0
        self.i = 0

    def item_dicide(self):
        text = f.readlines()
        self.item = text[403] #random.randint(0, len(text) - 1)
        self.item = self.item[:-1]

    def time_start(self):
        self.time = time.time()

    def time_end(self):
        self.time = time.time() - self.time

    def set_lenght(self):
        self.lenght = len(self.item)
    def print_str(self):
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


    @decorator
    def is_correct(self):
        if self.c == self.item[self.correct]:
            self.correct = self.correct + 1
            self.print_c()
        else:
            self.wrong = self.wrong + 1

    def accuracy_calc(self):
        self.accuracy = 100 * self.wrong / self.lenght

    def speed_calc(self):
        self.speed = self.lenght / self.time

    def print_result(self):
        print("accuracy is ", self.accuracy, " %")
        print("time is", self.time)
        print("speed is", self.speed)

    def write_res(self, file):
        file.write(self.time,' ', self.speed,' ', self.accuracy)

    def main_cikle(self):
        self.item_dicide()
        self.set_lenght()
        self.print_str()
        self.time_start()
        while self.correct < self.lenght:
            self.is_correct()
        print("\n")
        self.time_end()
        self.accuracy_calc()
        self.speed_calc()
        self.print_result()
        self.saving()

    def saving(self):
        print("Do yo want save  the result?(y/n)")
        answ = input()
        if answ == 'y':
            print("File:")
            name_file = str(input())
            save_file = open(name_file, "a+")
            save_file.write(str(self.time))
            save_file.write(' ')
            save_file.write(str(self.speed))
            save_file.write('      ')
            save_file.write(str(self.wrong))
            save_file.write('      ')
            save_file.write(str(self.accuracy))
            save_file.write('% \n')



a = stroka()
a.main_cikle()
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

