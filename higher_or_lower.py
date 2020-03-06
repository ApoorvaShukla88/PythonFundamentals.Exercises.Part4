import random


def evaluate():
    number = random.randint(1, 5)
    print(number)
    guessTaken = int(input("Give me a number "))
    #while guessTaken != number:
    if guessTaken < number:
        print("Too Low")
    elif guessTaken > number:
        print("Too High")
    elif guessTaken == number:
        print("HIT! You guessed it right " + str(number))
    #break



evaluate()
