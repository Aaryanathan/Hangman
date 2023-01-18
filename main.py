import random

player = input("What is your name? ")
print("Good Luck ! " + player)
word = ["hello", "what", "impossible", "possible", "cricket", "football", "india", "country", "state", "district"]
chance = 12
guessword = random.choice(word)
guess = input("Enter a Letter: ")
a = ""

while chance >= 0:
    fail = 0
    for letter in guessword:
        if letter in a:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            fail += 1
    if fail == 0:
        print("\n You win")
        print(guessword)
        break
    guess = input("\n Enter a Letter: ")
    a += guess
    if guess not in word:
        chance -= 1
        print("\n You Lose")
        print("You have {} guess left.".format(chance))
        if chance <= 0:
            print("GAME OVER")