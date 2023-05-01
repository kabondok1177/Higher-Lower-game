# Functions go here...
# check user answer yes / no to a question
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
    print("guess the secret number")
    print()
    print("*** Good Luck! :)  ***")
    print()
    return ""


# Main Routine goes here...
played_before = yes_no("Have you played the "
                       "game before? ")
if played_before == "no":
    instructions()

    print("Program continues")
