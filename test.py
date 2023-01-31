
import pygame
from pygame.locals import *
import random

def stock_words():
    words = []
    with open("mots.txt", "r") as file:
        for mot in file:
            mot = mot.rstrip()
            words.append(mot)
    return(words)

def random_word():
    return(random.randint(0, len(stock_words())))

def display_guess(nb):
    j = 0
    text=""
    while j < len(stock_words()[nb]):
        text+="_ "
        j+=1
    font1 = pygame.font.SysFont('freesanbold.ttf', 50)
    text1 = font1.render(text, True, (255, 255, 255))
    textRect1 = text1.get_rect()
    textRect1.center = (250, 70)
    display_surface.fill((0, 0, 0))
    display_surface.blit(text1, textRect1)
    return(text)
 

def check_letter(win_letters, letter):
    temp = 0
    for i in win_letters:
        if i == letter:
            temp += 1


def errors_check(errors, win_letters, letter):
    i = 0
    while letter != win_letters[i]:
        i+=1
    if i == len(win_letters):
        errors += letter
    return(True)
        


pygame.font.init()

pygame.font.get_init()

display_surface = pygame.display.set_mode((500, 500))

word = random_word()
win_letters = []
errors = []
i = 0
for i in stock_words()[word]:
    win_letters.append(i)
print(win_letters)

display_guess(word)

while True:
    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		    pygame.quit()
		    quit()
	    pygame.display.update()
