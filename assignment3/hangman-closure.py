def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        nonlocal guesses
        guesses.append(letter.lower())

        displayed = []
        for char in secret_word.lower():
            if char in guesses:
                displayed.append(char)
            else:
                displayed.append('_')

        print(' '.join(displayed))

        all_guessed = all(char in guesses for char in secret_word.lower())
        return all_guessed

    return hangman_closure


def play_hangman():
    secret_word = input("Enter the secret word: ").strip()
    while not secret_word.isalpha():
        print("Please enter a valid word (letters only).")
        secret_word = input("Enter the secret word: ").strip()

    game = make_hangman(secret_word)

    print("\nLet's play Hangman!")
    print(' '.join(['_'] * len(secret_word)))

    while True:
        guess = input("Guess a letter: ").strip().lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        solved = game(guess)

        if solved:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break


if __name__ == "__main__":
    play_hangman()