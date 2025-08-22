def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        display = ''.join([c if c in guesses else '_' for c in secret_word])
        print(display)
        all_guessed = all(c in guesses for c in set(secret_word))
        return all_guessed
    return hangman_closure

# Interactive hangman game
secret_word = input("Enter the secret word: ").lower()
game = make_hangman(secret_word)
print("Let's play Hangman!")
while True:
    guess = input("Guess a letter: ").lower()
    if not guess or len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    finished = game(guess)
    if finished:
        print(f"Congratulations! You guessed the word '{secret_word}'.")
        break
