import random
import math


def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")


def instructions():
    print()
    print("**** Welcome to the Higher Lower Game ****")
    print()
    print("For each game you will be asked to...")
    print("- Enter a 'low' and 'higher' number. The computer will randomly \n"
          "generate a \n"
          "'secret' number between your two chosen numbers. It will use \n"
          "these numbers for all \n"
          "the rounds in a given game.")
    print("The computer will calculate how many guesses you are allowed")
    print("enter the number of rounds you want to play")
    print()
    print("press enter for INFINITE mode")
    print()
    print("guess the secret number")
    print()
    print("*** Good Luck! :)  ***")
    print()
    return ""


def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    if low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check that integer is valid (ie: not too low / too hig etc)
            if situation == "any integer":
                return response

            elif situation == "both":
                if low <= response <= high:
                    return response

            elif situation == "low only":
                if response >= low:
                    return response

            print(error)

        except ValueError:
            print(error)


# main routine goes here

rounds_played = 0
rounds_won = 0

low_number = 1
high_number = 10

# work out the maximum number of guesses based on the range
var_range = high_number - low_number + 1
max_raw = math.log2(var_range)  # finds maximum # of guesses use
max_upped = math.ceil(max_raw)  # rounds up (ceil --> ceiling
max_guesses = max_upped + 1

mode = "regular"

# Ask user if they have played before and display
# instructions if it's their first time.
played_before = yes_no("Have you played the "
                       "game before? ")
if played_before == "no":
    instructions()

    print("Program continues")

#  Ask user number of rounds <enter> for infinite
rounds = int_check("How many rounds would you like to play?", 1, exit_code="")

print()

if rounds == "":
    mode = "infinite"
    rounds = 5

# Start of Game
end_game = "no"
while end_game == "no":

    if mode == "infinite":
        heading = f"Round {rounds_played + 1} (infinite mode)"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1

    secret = random.randint(low_number, high_number)
    print(f"Spoiler alert: {secret}")

    guesses_allowed = max_guesses
    already_guessed = []
    guesses_left = guesses_allowed

    # Start Round!!
    while True:

        guess = int_check("Guess (or 'xxx' to exit): ", low_number, high_number, "xxx")
        print()
        print("You guessed", guess)

        if guess == "xxx":
            end_game = "yes"
            break

        # checks that guess is not a duplicate
        if guess in already_guessed:
            print("You already guessed that number! Please try again "
                  "you still have {} guesses left".format(guesses_left))
            continue

        guesses_left -= 1
        already_guessed.append(guess)

        if guesses_left >= 1:

            if guess < secret:
                print("Too low,try a higher number. Guesses left:")
                print()

            elif guess > secret:
                print("Too high, try a lower number. Guesses left:")
                print()
        else:
            if guess < secret:
                print("Too low!")
            elif guess > secret:
                print("Too high!")

        if guess == secret:
            rounds_won += 1
            print("well done you got it")
            print()
            break

    # check if we are out of rounds
    if rounds_played >= rounds:
        break
