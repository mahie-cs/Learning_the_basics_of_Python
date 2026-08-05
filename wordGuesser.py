import random

with open('words.txt', 'r') as file:
    words = [line.strip() for line in file if len(line.strip()) >= 5]

random_word: str = random.choice(words)
word: str = random_word[0] + '_' * (len(random_word) - 2) + random_word[-1]
last_word_index: int = len(random_word) - 1
chances: int = 0
to_guess: str = random_word[1:-1]
used_letters: str = ''
print(word)

if len(random_word) > 9:
    chances = 7
elif len(random_word) > 7:
    chances = 6
else:
    chances = 5


incomplete: bool = True
while incomplete:
    if chances == 0:
        print(f'You have no more chances! The word was: {random_word}')
        break
    if '_' not in word:
        print(f'Congratulations! You guessed the word: {random_word}')
        break   
    guess: str = input('Guess a letter: ')
    if len(guess) != 1 or not guess.isalpha():
        print('Please enter a single letter.')
        continue
    if guess in used_letters:
        print(f'You already guessed {guess}.')
        continue
    used_letters += guess
    if guess in to_guess:
        print(f'{guess} is in the word!')
        for i in range(1, last_word_index):
            if random_word[i] == guess:
                word = word[:i] + guess + word[i + 1:]
    else:
        print(f'{guess} is not in the word!')
        chances -= 1
    print(word)
