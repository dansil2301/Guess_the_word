import random
# I have no button in this version (i had it a flowchart)
# Changed point system to make more interesting (implimented a multiplier for guessing letters in a row)
# Haven't done difficulty system. Want to add it in a final version
# Also there is no restart or stop button as in the flowchart but again it will be a final version

# The list of words will be in a text file (there will be much more words to pick, like more than 1000)
words = ['apple', 'orange', 'fontys', 'great', 'nothing', 'coach']
points = 0
streak = 0
letter_counter = 0

# cycle of words, when the word is guessed it will give a new random one
while True:
    word = list(words[random.randrange(1, len(words))])
    guessedWord = ['*' for letter in word]
    print(*guessedWord)

    # cycle of letters. Shows correct ones
    while '*' in guessedWord:
        userLetter = input('input a letter: ')
        if userLetter in word:
            # point counter with a streak (differs a little form the flowchart)
            if streak > 10:
                streak = 10
            points += 100 + 10 * streak

            # actually shows words
            ind = word.index(userLetter) if userLetter in word else -1
            while ind != -1:
                guessedWord[ind] = userLetter
                word[ind] = '*'
                ind = word.index(userLetter) if userLetter in word else -1
            if letter_counter != 0:
                letter_counter -= 1
            streak += 1
        else:
            streak = 0
            letter_counter += 1
            print('the letter is not in the word')
        # stops if there are too many mistakes
        if letter_counter >= 5:
            break
        print(*guessedWord)
        print(f'Your points: {points}, tries left: {5 - letter_counter}')

    # stops if there are too many mistakes
    if letter_counter >= 5:
        break
    print('You guessed the word!')
    points += 500
    print(f'Your points: {points}, tries left: {5 - letter_counter}')

print(f'Game Over, score: {points}')