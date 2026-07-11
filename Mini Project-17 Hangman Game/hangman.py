import random

def play_hangman():
    words = ['python', 'summer', 'school', 'agent', 'machine']
    word = random.choice(words)
    guesses = ''
    turns = 5
    print('Welcome to Hangman!')
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end='')
            else:
                print('_', end='')
                failed += 1
        print()
        if failed == 0:
            print('You won!')
            break
        guess = input('Guess a character: ')
        guesses += guess
        if guess not in word:
            turns -= 1
            print('Wrong!')
            print(f'You have {turns} more guesses.')
        if turns == 0:
            print('You lose. The word was:', word)

if __name__ == '__main__':
    print('Run play_hangman() to play!')