import random
from collections import Counter
output = ''
cGuesses = ''
chances = 0
guessNum = 0
letters = ""

# creates list of animals
someAnimals = "african elephant, bengal tiger, great white shark, Giraffe, Red Panda, Polar Bear, Giant Panda, Snow Leopard, Blue Whale, Komodo Dragon, Sloth, Golden Eagle, Kangaroo, Monarch Butterfly, Sea Turtle, Hummingbird, Wombat, Narwhal, Hedgehog, Cheetah"
someAnimals = someAnimals.split(', ')

#random list of fruits
someFruits = "apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon"
someFruits = someFruits.split(' ')

#chooses the category, word, and chances
categoryTypes = [someAnimals, someFruits]
category = random.choice(categoryTypes)
word = random.choice(category).lower()
chances = len(word)+2

#decides what hint to give
if category == someAnimals:
    hint = 'ANIMALS!'
else:
    hint = 'FRUITS!'

#creating the initial bit where the game is announced and the dashes are given
print("\n\nWelcome to Hang Man \nTry to Guess the word. This hint is: ", hint)
print("you have {h} chances to get it right".format(h=chances))

#prints out the hang man blank thingy
for x in range (0, len(word), 1):
    if word[x] == ' ':
       cGuesses += '  '
    else:
        cGuesses += '_ '      
print(cGuesses)


guessedLetters = ''

guessedRight = False
#recieve the user's guess
while True: 
    

    #ensures that teh guess is valid
    if len(guessedLetters) > 0:
        print('\n________________\nguessed letters: ', guessedLetters)
        print('you have {x} chances remaining'.format(x=chances-guessNum))
    while True:
        guess = input("Guess a letter:- ").lower()
        if len(guess) == 1 and guess.isalpha():
            guessedLetters += guess
            break
        elif not guess.isalpha():
            print('Hitansh no way you tried this')
        
        else:
            print('please only guess one letter at a time Hitansh')
    
    #finds teh guessed letter in the actual word and adds to a list as many times as it appears    
    for x in range (0, len(word), 1):
        if word[x] == guess:
            letters += word[x]

    #searching the word for guessed characters   
    for char in word:  
        answerIndex = 0
        
        #for each letter in the word we go through all the letters in guessed letters to find match
        while answerIndex<=len(guessedLetters):

            #if we go through all the letters then we leave a blank          
            if answerIndex == len(guessedLetters):
                output+= '_ '
                break

            #if we get a letter correct then we add it
            if char == guessedLetters[answerIndex]:
                output += guessedLetters[answerIndex]
                output += ' '
                break

            #spaces stay spaces
            elif char == ' ':
                output += ' ' 
                break  

            #if nothing aplicable then move on to next letter
            elif char != guessedLetters[answerIndex] and char != ' ':
                answerIndex += 1

    #prints out the progress of the hang man           
    print(output)

    #check to see if there is any blanks left, if not, we win
    if output.find('_') == -1:
        print('CONGRATS, you found the word!')
        break

    output = ' '
    #check if there are any chances left
    guessNum +=1
    if guessNum == chances:
        print('Womp Womp, you Lose!')
        print(f'the correct word was {word}')
        break

    
    





#probbably two different counts for the two different things, maybe a for loop?
