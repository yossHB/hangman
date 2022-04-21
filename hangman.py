import random
import string

wordList = '''
squinted against the sun at distant dust trail raked car on its up Big House horses kicked and flicked their tails flies not caring about owners first visit in ten months Sam waited Mr Carter did come here unless to which was just fine by more he kept out of his bosss way longer had have a job
'''.split()

def getRandomWord():
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex].upper()

def hangman():
    word = getRandomWord()    #example
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f'You have {lives} lives left and you have used these letters: {" ".join(used_letters)}')

        # the current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(HANGMAN_PICS[lives-1])
        print(f"Current word: {' '.join(word_list)}")

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print(f'Your letter {user_letter} is not in the word.')

        elif user_letter in used_letters:
            print('You have already used that letter. Guess another letter.')

        else:
            print('That is not a valid letter.')

    if lives == 0:
        print(HANGMAN_PICS[lives-1])
        print(f'You died, sorry. The word was{word}')
    else:
        print(f'YAY! You guessed the word {word} !!')


HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']


if __name__ == '__main__':
    hangman()
