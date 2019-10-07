import random
r = random.randint(0,100)
print("I have thought of a number. Its your time to guess")

guesses = []
while True:
    ui = int(input("Enter your guess [0,100] : "))
    guesses.append(ui)
    if ui < r:
        print("Low")
    elif ui > r:
        print("High")
    else:
        print("Bingo! You guessed it right")
        print("You took", len(guesses), "guesses")
        print("These were your guesses ->", guesses)
        break