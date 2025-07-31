def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = ''.join([char if char in guesses else '_' for char in secret_word])
        print(display)
        return set(secret_word).issubset(set(guesses))

    return hangman_closure

if __name__ == "__main__":
    secret = input("Enter secret word: ").lower()
    game = make_hangman(secret)

    while True:
        guess = input("Guess a letter: ").lower()
        if game(guess):
            print("You've guessed the word!")
            break
