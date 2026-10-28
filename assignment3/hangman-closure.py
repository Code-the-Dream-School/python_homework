# Task 4: Closure Practice
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = "".join(ch if ch in guesses else "_" for ch in secret_word)
        print(display)
        return all(ch in guesses for ch in secret_word)

    return hangman_closure


if __name__ == "__main__":
    secret = input("Enter the secret word: ").strip().lower()
    print("\n" * 50)  # scroll the secret off the screen
    game = make_hangman(secret)
    done = False
    while not done:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue
        done = game(guess)
    print("You got it!")
