def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
            guesses.append(letter)

            display = ""

            for char in secret_word:
                if char in guesses:
                    display += char
                else:
                    display += "_"
            print(display)  

            return all(char in guesses for char in secret_word)  

    return hangman_closure

secret_word = input("Enter the secret word: ").lower()

game = make_hangman(secret_word)

while True:
    letter = input("Guess a letter: ").lower()
    
    if game(letter):
         print("Congratulations! You guessed the word!")
         break