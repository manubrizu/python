while True:
    number = 15
    guess = 0
    print("Guess the number from 1-20")
    guess = input()
    guess = int(guess)
    if guess == number:
        print("Well done!")
        break