from random import randint
n = randint(1, 100)
k=0
guess = []

def instruction():
    print("WELCOME TO GUESS ME!")
    print("I'm thinking of a number between 1 and 100")
    print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
    print("If your guess is within 10 of my number, I'll tell you you're WARM")
    print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
    print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
    print("LET'S PLAY!\n")


instruction()
while True:
    guess.append(int(input('Enter your Guess: ')))
    if guess[-1] == n:
        print('Correctly Guessed:)')
        print(f'Number of Guesses taken: {len(guess)}')
        break

    if guess[-1] < 1 or guess[-1] > 100:
        print('OUT OF BOUNDS!!!')
        continue

    if k==0:
        if abs(guess[-1] - n) <= 10:
            print('WARM!')
        else:
            print('COLD!')
        k += 1
        continue

    if abs(guess[-1] - n) <= abs(guess[-2] - n):
        print('WARMER!')
    else:
        print('COLDER!')


