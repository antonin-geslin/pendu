
import pygame
from pygame.locals import *
import random
import os

def draw_lines(errors):
    if len(errors) < 10:
        if len(errors) == 1:
            pygame.draw.line(display_surface, (255,255,255), (10,500),(300,500),8)
        if len(errors) == 2:
            pygame.draw.line(display_surface, (255,255,255), (10,500),(300,500),8)
            pygame.draw.line(display_surface, (255,255,255), (50,150),(50,500),8)
        if len(errors) == 3:
            pygame.draw.line(display_surface, (255,255,255), (10,500),(300,500),8)
            pygame.draw.line(display_surface, (255,255,255), (50,150),(50,500),8)
            pygame.draw.line(display_surface, (255,255,255), (40,150),(350,150),8)
        if len(errors) == 4:
            pygame.draw.line(display_surface, (255,255,255), (10,500),(300,500),8)
            pygame.draw.line(display_surface, (255,255,255), (50,150),(50,500),8)
            pygame.draw.line(display_surface, (255,255,255), (40,150),(350,150),8)
            pygame.draw.line(display_surface, (255,255,255), (175,150),(175,180),8)
        if len(errors) == 5:
            pygame.draw.line(display_surface, (255,255,255), (10,500),(300,500),8)
            pygame.draw.line(display_surface, (255,255,255), (50,150),(50,500),8)
            pygame.draw.line(display_surface, (255,255,255), (40,150),(350,150),8)
            pygame.draw.line(display_surface, (255,255,255), (175,150),(175,180),8)
            pygame.draw.circle(display_surface, (255,255,255), (175,200),25,8)
        if len(errors) == 6:
            pygame.draw.line(display_surface, (255,255,255), (10,500),(300,500),8)
            pygame.draw.line(display_surface, (255,255,255), (50,150),(50,500),8)
            pygame.draw.line(display_surface, (255,255,255), (40,150),(350,150),8)
            pygame.draw.line(display_surface, (255,255,255), (175,150),(175,180),8)
            pygame.draw.circle(display_surface, (255,255,255), (175,200),25,8)
            pygame.draw.line(display_surface, (255,255,255), (175,225),(175,325),8)
        if len(errors) == 7:
            pygame.draw.line(display_surface, (255,255,255), (10,500),(300,500),8)
            pygame.draw.line(display_surface, (255,255,255), (50,150),(50,500),8)
            pygame.draw.line(display_surface, (255,255,255), (40,150),(350,150),8)
            pygame.draw.line(display_surface, (255,255,255), (175,150),(175,180),8)
            pygame.draw.circle(display_surface, (255,255,255), (175,200),25,8)
            pygame.draw.line(display_surface, (255,255,255), (175,225),(175,325),8)
            pygame.draw.line(display_surface, (255,255,255), (200,270),(175,230),8)
        if len(errors) == 8:
            pygame.draw.line(display_surface, (255,255,255), (10,500),(300,500),8)
            pygame.draw.line(display_surface, (255,255,255), (50,150),(50,500),8)
            pygame.draw.line(display_surface, (255,255,255), (40,150),(350,150),8)
            pygame.draw.line(display_surface, (255,255,255), (175,150),(175,180),8)
            pygame.draw.circle(display_surface, (255,255,255), (175,200),25,8)
            pygame.draw.line(display_surface, (255,255,255), (175,225),(175,325),8)
            pygame.draw.line(display_surface, (255,255,255), (200,270),(175,230),8)
            pygame.draw.line(display_surface, (255,255,255), (150,270),(175,230),8)
        if len(errors) == 9:
            pygame.draw.line(display_surface, (255,255,255), (10,500),(300,500),8)
            pygame.draw.line(display_surface, (255,255,255), (50,150),(50,500),8)
            pygame.draw.line(display_surface, (255,255,255), (40,150),(350,150),8)
            pygame.draw.line(display_surface, (255,255,255), (175,150),(175,180),8)
            pygame.draw.circle(display_surface, (255,255,255), (175,200),25,8)
            pygame.draw.line(display_surface, (255,255,255), (175,225),(175,325),8)
            pygame.draw.line(display_surface, (255,255,255), (200,270),(175,230),8)
            pygame.draw.line(display_surface, (255,255,255), (150,270),(175,230),8)
            pygame.draw.line(display_surface, (255,255,255), (200,370),(175,320),8)
    pygame.display.update()



def stock_words():
    words = []
    with open("mots.txt", "r") as file:
        for mot in file:
            mot = mot.rstrip()
            words.append(mot)
    return(words)

def random_word():
    return(random.randint(0, len(stock_words()) - 1))


def display_win(text1):
    global text
    text1 = font1.render(text, True, (255, 255, 255))
    textRect1 = text1.get_rect()
    textRect1.center = (275, 70)
    display_surface.blit(text1, textRect1)
    pygame.display.update()

def display_errors(errors):
    text_bis = "Wrong letters : "
    for i in errors:
        text_bis += " " + i
    text2 = font1.render(text_bis, True, (255,255,255))
    textRect2 = text2.get_rect()
    textRect2.center = (275, 120)
    display_surface.blit(text2, textRect2)
    pygame.display.update()

def check_letter(win_letters, letter, errors):
    global index
    global win
    if letter not in win_letters:
        errors.append(letter)
        return(False)
    else:
        compt = 0
        i  = 0
        while i <= len(win_letters) - 1:
            if win_letters[i] == letter:
                compt += 1
            i += 1
        if compt == 1:
            win += 1
            index = win_letters.index(letter)
            fill_text(letter, index)
        else:
            win += 1
            temp1 = win_letters.index(letter)
            fill_text(letter, temp1)
            compt -= 1
            while compt != 0:
                win+=1
                temp2 = win_letters.index(letter, temp1 + 1)
                temp1 = temp2
                fill_text(letter, temp1)
                compt -= 1
        return(True)


def fill_text(letter, nb):
    global text
    s = list(text)
    if nb == 0:
        s[nb] = letter
    else:
        s[nb] = letter
    text = "".join(s)


def is_win(word, errors, running):
    global win
    if win == len(stock_words()[word]) *2:
        text3 = font1.render("YOU WIN", True, (255,255,255))
        textRect3 = text3.get_rect()
        textRect3.center = (300, 275)
        display_surface.blit(text3, textRect3)
        return(True)
    elif len(errors) == 9:
        text3 = font1.render("YOU LOSE", True, (255,255,255))
        textRect3 = text3.get_rect()
        textRect3.center = (300, 275)
        display_surface.blit(text3, textRect3)
        text4 = font1.render(stock_words()[word], True, (255,255,255))
        textRect4 = text4.get_rect()
        textRect4.center = (300, 320)
        display_surface.blit(text4, textRect4)
        return(False)


def display():
    display_surface.fill((0, 0, 0))
    title = font1.render("PENDU", True, (255,255,255))
    titleRect = title.get_rect()
    titleRect.center = (270, 20)
    display_surface.blit(title, titleRect)
    pygame.display.update()


pygame.font.init()
pygame.init()
pygame.font.get_init()

display_surface = pygame.display.set_mode((550, 550))
time = pygame.time.Clock()
font1 = pygame.font.SysFont('freesanbold.ttf', 50)
display()





word = random_word()
text = ""
index = 0
j = 0
while j < len(stock_words()[word]):
    text+="_ "
    j+=1
text1 = font1.render(text, True, (255, 255, 255))
textRect1 = text1.get_rect()
textRect1.center = (275, 70)
display_surface.blit(text1, textRect1)

win_letters = []
win = 0
letter = ""
errors = []
i = 0
for i in stock_words()[word]:
    win_letters.append(i)
    win_letters.append(" ")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and ((event.unicode >= 'a' and event.unicode <= 'z') or (event.unicode >= 'A' and event.unicode <= 'Z')):
            letter = event.unicode
            pygame.display.update()
            if check_letter(win_letters, letter, errors) == False:
                display()
                display_win(text1)
                display_errors(errors)
                draw_lines(errors)
                is_win(word, errors, running)
                pygame.display.update()
            elif  check_letter(win_letters, letter, errors) == True:
                display()
                display_win(text1)
                display_errors(errors)
                draw_lines(errors)
                is_win(word, errors, running)
                pygame.display.update()
            if is_win(word, errors, running) == False:
                running = False
            else:
                running = False
    time.tick(10000000000)
    pygame.display.update()

pygame.quit()

