import json
import random
import os

def load_words():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, 'words.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

def load_hangman(stage):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, f'hangman{stage}.txt'), 'r', encoding='utf-8') as f:
        return f.read()

def display_hangman(wrong_guesses):
    if wrong_guesses > 0:
        print(load_hangman(wrong_guesses))

def play_hangman():
    words_data = load_words()
    word_entry = random.choice(words_data)
    word = word_entry['word'].upper()
    hint = word_entry['hint']

    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("Игра 'Виселица на поле чудес'!")
    print(f"Подсказка: {hint}")

    while wrong_guesses < max_wrong:
        display_word = ''
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + ' '
            else:
                display_word += '_ '
        print(display_word.strip())

        if all(letter in guessed_letters for letter in word):
            print(f"Поздравляю! Вы угадали слово: {word}")
            break

        guess = input("Введите букву: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Введите одну букву!")
            continue

        if guess in guessed_letters:
            print("Вы уже называли эту букву!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Правильно!")
        else:
            wrong_guesses += 1
            print(f"Неправильно! Осталось попыток: {max_wrong - wrong_guesses}")
            display_hangman(wrong_guesses)
    else:
        print(f"Вы проиграли! Загаданное слово: {word}")

if __name__ == "__main__":
    play_hangman()
