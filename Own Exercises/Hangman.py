import numpy as np
import csv
import pandas as pd
import random

def letter_guess(random_word, guessed_letters):
    temp_dict = dict()
    mistake_increment = False
    letter = input("Please guess a letter: ")
    for x in guessed_letters:
        while x == letter:
            print('The letter you guessed has already been guessed, please guess another letter')
            letter = input("Please guess a letter: ")
    for letters in random_word:
        if letters == letter:
            temp_dict[letter] = True
            return temp_dict, mistake_increment;
    else:
        temp_dict[letter] = False
        mistake_increment = True
        return temp_dict, mistake_increment;
    
def display(random_word, guessed_letters):
    word = ''
    for x in random_word:
        for y in guessed_letters:
            if x == y:
                word += y + "\u0332" + ' '
                break
        else:
            word += '_ '
    return word

def CheckWinCondition(word):
    for x in word:
        if x == '_':
            return False
    else:
        print('Congratulations, You Win~')
        return True

file = pd.read_csv(r'C:\Users\Javier\Desktop\Python\Python-Own-Exercises\Own Exercises\englishwords.csv', sep = ';', skiprows=3)
file = file.dropna(thresh=2)
words = file['word']
index = random.randint(0, len(words) - 1)
HM_word = words[index]

guessed_letters = {}

lines = ''
for number_of_letters in range(len(HM_word)):
    lines += '_ '
#print(HM_word)
print(lines)
mistakes = 0
Win = False
while mistakes < 6 and Win == False:
    guess_phase, mistakebool = letter_guess(HM_word, guessed_letters)
    if mistakebool == True:
        mistakes += 1
    guessed_letters.update(guess_phase)
    stage_word = display(HM_word, guessed_letters)
    print(stage_word)
    Win = CheckWinCondition(stage_word)
if Win == False:
    print('The correct word is "' + HM_word + '"')
    print('Try harder next time :^)')


