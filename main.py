from flask import Flask, render_template, request
import Guess_the_word_code

app = Flask(__name__)
DIF_LEVEL = 'medium'
word = Guess_the_word_code.word_difficulty(DIF_LEVEL)
word_guess = [' ' for _ in word]
points = 0
streak = 0
tries = 6
cont = False
letter = '_'
used_letters = list()
whaat = list()


def set_def():
    global word
    global word_guess
    global points
    global streak
    global tries
    global cont
    global letter
    global used_letters
    global whaat

    word = Guess_the_word_code.word_difficulty(DIF_LEVEL)
    word_guess = [' ' for _ in word]
    points = 0
    streak = 0
    tries = 6
    cont = False
    letter = '_'
    used_letters = list()
    whaat = list()


@app.route("/")
def index():
    global DIF_LEVEL
    return render_template('index.html', dif_level=DIF_LEVEL[0].upper())


@app.route("/rules")
def rules():
    return render_template('rules.html')


@app.route("/difficulty", methods=["POST", "GET"])
def difficulty():
    global DIF_LEVEL
    global word
    global word_guess

    if request.method == 'POST':
        if request.form['name'] == 'easy':
            DIF_LEVEL = 'easy'
        elif request.form['name'] == 'medium':
            DIF_LEVEL = 'medium'
        elif request.form['name'] == 'difficult':
            DIF_LEVEL = 'difficult'
        word = Guess_the_word_code.word_difficulty(DIF_LEVEL)
        word_guess = [' ' for _ in word]
        return index()

    return render_template('difficulty.html')


@app.route("/game", methods=["POST", "GET"])
def game():
    global word
    global word_guess
    global points
    global streak
    global tries
    global cont
    global letter
    global used_letters
    global whaat

    if request.method == 'POST':
        if request.form.get('leave') == 'Leave':
            set_def()
            return index()
        elif request.form.get('restart') == 'Restart':
            set_def()
        else:
            letter = request.form.get('Letter').lower()
    print(word, word_guess)
    word_guess, points, streak, tries, cont, used_letters, whaat = Guess_the_word_code.main_alt(word=word,
                                                                                                word_guess=word_guess,
                                                                                                user_letter=letter,
                                                                                                points=points,
                                                                                                streak=streak,
                                                                                                tries=tries,
                                                                                                used_letters=used_letters,
                                                                                                whaat=whaat)
    if ' ' not in word_guess:
        points += 500
        word = Guess_the_word_code.word_difficulty(DIF_LEVEL)
        word_guess = [' ' for _ in word]
        used_letters = list()

    empty = ['_' if i % 2 == 0 else ' ' for i in range(len(word_guess) + len(word_guess) - 1)]
    show_word = [(word_guess[i//2].upper() if word_guess[i//2] != ' ' else ' ') if i % 2 == 0 else
                 ' ' for i in range(len(word_guess) + len(word_guess) - 1)]

    used_letters = sorted(list(set([used_letters[i] + (' ' if ' ' not in used_letters[i] else '')
                                    for i in range(len(used_letters)) if letter != '_'])))
    whaat = sorted(list(set([whaat[i] + (' ' if ' ' not in whaat[i] else '')
                             for i in range(len(whaat)) if letter != '_'])))

    return render_template('game.html', points=points, streak=streak,
                           tries=tries, empty_word=empty, guessed_letters=show_word,
                           cont=cont, not_guessed_w=word, used_letters=used_letters,
                           whaat=whaat)


if __name__ == "__main__":
    app.run(debug=True)
