import random

correctWord = "hel"
wordGuessed = False
counter = 0
while wordGuessed == False:
    guess = ""
    for i in range(len(correctWord)):
        n = random.randint(97, 122)
        if random.random() < 0.1:
            m = 32
        else:
            m = n
        guess += chr(m)
    counter += 1
    print(counter, " ", guess)
    
    if guess == correctWord:
        wordGuessed == True
        break

print("Correct! The word was " + correctWord)
