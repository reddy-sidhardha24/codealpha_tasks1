import random

WORDS = ["python", "apple", "river", "train", "music"]  # 5 predefined words
MAX_WRONG = 6

def pick_word():
    return random.choice(WORDS)

def display_progress(secret, guessed):
    return " ".join(ch if ch in guessed else "_" for ch in secret)

def play():
    secret = pick_word()
    guessed = set()
    wrong_guesses = set()

    print("Welcome! Guess the word. You have", MAX_WRONG, "wrong guesses allowed.\n")

    while True:
        print("Word:", display_progress(secret, guessed))
        print("Wrong guesses ({}/{}): {}".format(len(wrong_guesses), MAX_WRONG,
                                                ", ".join(sorted(wrong_guesses)) or "none"))
        if len(wrong_guesses) >= MAX_WRONG:
            print("\nYou've run out of guesses. The word was:", secret)
            break
        if all(ch in guessed for ch in secret):
            print("\nCongratulations! You guessed the word:", secret)
            break

        guess = input("Enter a letter (or type the full word): ").strip().lower()
        if not guess:
            print("Please enter something.\n")
            continue

        # Full-word guess
        if len(guess) > 1:
            if guess == secret:
                print("\nAmazing — correct! The word is:", secret)
                break
            else:
                if guess in wrong_guesses:
                    print("You already tried that wrong word.\n")
                else:
                    wrong_guesses.add(guess)
                    print("Wrong word guess.\n")
            continue

        # Single-letter validation
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic letter.\n")
            continue

        if guess in guessed or guess in wrong_guesses:
            print("You already guessed '{}' before.\n".format(guess))
            continue

        if guess in secret:
            guessed.add(guess)
            print("Good guess!\n")
        else:
            wrong_guesses.add(guess)
            print("Nope — that letter isn't in the word.\n")

if __name__ == "__main__":
    play()
A