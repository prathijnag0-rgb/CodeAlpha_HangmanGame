import random

words = ["python", "computer", "coding", "program", "developer"]

secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman Game!")
print("Guess the hidden word.")

while wrong_guesses < max_guesses:

    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You Won!")
        break

    guess = input("Enter one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("Already guessed! Try another letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

if wrong_guesses == max_guesses:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("Thank you for playing!")
