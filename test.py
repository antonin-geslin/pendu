
import pygame
from pygame.locals import *
import random

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

def display_errors(errors):
    text_bis = "Wrong letters : "
    for i in errors:
        print(i)
        text_bis += " " + i
    text2 = font1.render(text_bis, True, (255,255,255))
    textRect2 = text2.get_rect()
    textRect2.center = (275, 120)
    display_surface.blit(text2, textRect2)

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
            win += compt
            temp1 = win_letters.index(letter)
            print(temp1)
            fill_text(letter, temp1)
            compt -= 1
            while compt != 0:
                temp2 = win_letters.index(letter, temp1 + 1)
                print(temp2)
                temp1 = temp2
                fill_text(letter, temp1)
                compt -= 1


def fill_text(letter, nb):
    global text
    s = list(text)
    if nb == 0:
        s[nb] = letter
    else:
        s[nb] = letter
    text = "".join(s)


def is_win(word):
    global win
    if win == len(stock_words()[word]):
   
        return()

pygame.font.init()

pygame.font.get_init()

display_surface = pygame.display.set_mode((550, 550))
display_surface.fill((0, 0, 0))
font1 = pygame.font.SysFont('freesanbold.ttf', 50)





word = random_word()
text = ""
index = 0
j = 0
print(len(stock_words()[word]))
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
print(win_letters)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and ((event.unicode >= 'a' and event.unicode <= 'z') or (event.unicode >= 'A' and event.unicode <= 'Z')):
            letter = event.unicode
            if check_letter(win_letters, letter, errors) == False:
                display_surface.fill((0, 0, 0))
                display_win(text1)
                display_errors(errors)
                draw_lines(errors)
            else:
                display_surface.fill((0, 0, 0))
                display_win(text1)
                display_errors(errors)
                draw_lines(errors)
    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		    pygame.quit()
		    quit()
	    pygame.display.update()
