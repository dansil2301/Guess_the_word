from random import randrange


def word_difficulty(DIF_LVL):
    if DIF_LVL == 'easy':
        with open(r'words//easy.txt', 'r', encoding='utf-8') as words:
            list_word = list()
            for word in words:
                list_word.append(word.replace('\n', ''))
    elif DIF_LVL == 'medium':
        with open(r'words//medium.txt', 'r', encoding='utf-8') as words:
            list_word = list()
            for word in words:
                list_word.append(word.replace('\n', ''))
    elif DIF_LVL == 'difficult':
        with open(r'words//difficult.txt', 'r', encoding='utf-8') as words:
            list_word = list()
            for word in words:
                list_word.append(word.replace('\n', ''))

    return list_word[randrange(0, len(list_word))]


def find_letter_ind(word, user_letter):
    ind = list()

    for i, letter in enumerate(word):
        if letter == user_letter:
            ind.append(i)

    return ind


def main_alt(word, word_guess, user_letter, points, streak, tries, used_letters, whaat):
    cont = 0
    if user_letter + ' ' not in used_letters:
        if user_letter in word:
            points += 100 + 10 * streak
            if streak < 10:
                streak += 1
            if tries < 5:
                tries += 1
            for i in find_letter_ind(word, user_letter):
                word_guess[i] = user_letter
        else:
            streak = 0
            tries -= 1
            if tries == 0:
                cont = True
        if user_letter.isalpha():
            used_letters.append(user_letter)
        else:
            whaat.append(user_letter)
    else:
        tries -= 1
        streak = 0
        if tries == 0:
            cont = True

    return word_guess, points, streak, tries, cont, used_letters, whaat
