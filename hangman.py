import random

def select_random_word():
    words = ['python', 'hangman', 'Maheshwar', 'programming', 'developer', 'code']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def hangman_game():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word:")

    while incorrect_guesses < max_incorrect_guesses:
        print(display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word:", word)
                break
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        if incorrect_guesses == max_incorrect_guesses:
            print("Sorry, you've run out of guesses. The word was:", word)

if __name__ == "__main__":
    hangman_game()
