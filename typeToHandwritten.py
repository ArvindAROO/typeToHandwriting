# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:52:19 2020

@author: Ak
"""
from PIL import Image

BG = Image.open("bg.png")
#creating the instance of background image
sizeOfSheet = BG.width
gap, _ = 50, 25
#size of each image or character

#these are the only allowed characters
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.?! 1234567890'
def writeIt(char):
    """Takes indivial chars and adds them to image"""
    global gap, _
    if char == '\n':
        pass
    else:
		#this will generate and open the image file
        char.lower()
        cases = Image.open("%s.png"%char)
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size
        del cases

def caller(word):
    global gap, _
    if gap > sizeOfSheet - 100*(len(word)):
        gap = 50
        _ += 200
    print("word revieced by caller is {} and its size is {}".format(word, len(word)))
	#this works on a word by word process
    for letter in word:        
        if letter in allowedChars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += 'upper'            
            elif letter == '.':
                letter = "fullstop"
            elif letter == '!':
                letter = 'exclamation'
            elif letter == '?':
                letter = 'question'
            elif letter == ',':
                letter = 'comma'
            writeIt(letter)
			#naming the character
			#upper is appended to upper case characters
def dataHandling(Input):
    """Handles the input"""
    wordlist=Input.split(' ')
    for i in wordlist:
        caller(i)
        writeIt('space')
    #add word handling... it is splitting\
    #the word to accomodate new line
if __name__ == '__main__':
    try:
        n = int(input("Enter number of lines:"))
        for i in range(n):
            string = input("Enter text:")
            dataHandling(string)
            writeIt('\n')
        BG.show()
    except ValueError as E:
        print("{}\nTry again".format(E))
