# HL components 1 - Get (and Check ) user input

# To Do
# Check a lowest is an integer (any integer)
# Check that highest is more than lowest (lower bound only)
# Check that rounds is more than 1 (upper bound only)
# Check that guess is between lowest and highest (
# lower and upper bound)


# Number checking function goes here
def int_check(question, low=None, high=None):
    situation = ""

    # Check if both low and high values are given
    # If both values are given, set the situation to "both"
    # If only ;ow values is given, set the situation to "low only"
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

        while True:

            try:
                response = int(input(question))

                # checks input is not too high or
                # too low if a both upper and lower bounds
                # are specified
                if situation == "both":
                    if response < low or response > high:
                        print("Please enter a number between "
                              "{} and {}".format(low, high))
                        continue

                # checks input is not too low
                elif situation == "low only":
                    if response < low:
                        print("Please enter a number that is more"
                              "then (or equal to) {}".format(low))
                        continue

                return response

            # checks input is a integer
            except ValueError:
                print("Please enter an integer")
                continue
