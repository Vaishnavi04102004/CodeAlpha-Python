import random

words = [
    "python",
    "computer",
    "keyboard",
    "internet",
    "programming",
    "developer",
    "database",
    "software",
    "algorithm",
    "network"
]

while True:
    word = random.choice(words)
    guessed = set()
    wrong = set()
    attempts = 6

    print("\n" + "=" * 40)
    print("HANGMAN GAME")
    print("=" * 40)

    while attempts > 0:
        display = ""

        for ch in word:
            if ch in guessed:
                display += ch + " "
            else:
                display += "_ "

        print("\nWord:", display.strip())

        if "_" not in display:
            print("\nCongratulations! You guessed the word:", word)
            break

        if wrong:
            print("Wrong Letters:", " ".join(sorted(wrong)))

        print("Attempts Left:", attempts)

        guess = input("Enter a letter: ").strip().lower()

        if guess == "":
            print("Input cannot be empty.")
            continue

        if len(guess) != 1:
            print("Enter only one letter.")
            continue

        if not guess.isalpha():
            print("Only alphabets are allowed.")
            continue

        if guess in guessed or guess in wrong:
            print("You already guessed that letter.")
            continue

        if guess in word:
            guessed.add(guess)
            print("Correct!")
        else:
            wrong.add(guess)
            attempts -= 1
            print("Wrong!")

    else:
        print("\nGame Over!")
        print("The correct word was:", word)

    choice = input("\nDo you want to play again? (y/n): ").strip().lower()

    if choice != "y":
        print("Thank you for playing!")
        break