import random

COLORS = ["R", "G", "B", "Y", "W", "O"]

TRIES = 10
CODE_LENGTH = 4


def generate_code():
    """Generates a random code using the available colors."""
    return random.sample(COLORS, CODE_LENGTH)  # Uses random.sample for efficiency


def guess_code():
    """Prompts the user for a guess and validates it."""
    while True:
        guess = input("Guess code: ").upper().split()
        if len(guess) != CODE_LENGTH:
            print("Wrong code length")
            continue
        if all(color in COLORS for color in guess):
            return guess
        print("Wrong color")


def check_code(guess, code):
    """Calculates the correct and incorrect positions."""
    correct_positions = sum(g == c for g, c in zip(guess, code))
    incorrect_positions = sum(
        min(guess.count(color), code.count(color)) for color in set(guess)
    ) - correct_positions
    return correct_positions, incorrect_positions


def give_hint(position, code, guess):
    """Provides a hint for a specific position if it's incorrect."""
    if position not in range(1, CODE_LENGTH + 1) or guess[position - 1] == code[position - 1]:
        return "Invalid position or already correct."
    available_colors = list(set(code) - set(guess))
    if available_colors:
        return f"Hint for position {position}: One possible color is {' or '.join(available_colors)}."
    return "No hint available for this position."


def game():
    """Runs the mastermind game."""
    print("Welcome to the Mastermind game!")
    print(f"Colors used: {', '.join(COLORS)}")

    code = generate_code()

    for attempt in range(1, TRIES + 1):
        guess = guess_code()
        correct_positions, incorrect_positions = check_code(guess, code)

        if correct_positions == CODE_LENGTH:
            print(f"You cracked the code in {attempt} attempts! The code was: {code}")
            break

        print(f"Correct positions: {correct_positions} | Incorrect positions: {incorrect_positions}")
        print("Enter 'X' to exit, 'A' to see the answer, or 'H' for hints (enter a number between 1 to 4).")
        choice = input("> ").upper()

        if choice == "X":
            print("Exiting the game.")
            break
        elif choice == "A":
            print(f"The code was: {code}")
            break
        elif choice == "H":
            position = int(input("Enter the position (1-4) for a hint: "))
            hint = give_hint(position, code, guess)
            print(hint)

    print("Thanks for playing!")


if __name__ == "__main__":
    game()




