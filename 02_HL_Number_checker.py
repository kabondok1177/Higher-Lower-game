# HL components 1 - Get (and Check ) user input

# To Do
# Check a lowest is an integer (any integar)
# Check that highest is more than lowest (lower bound only)
# Check that rounds is more than 1 (upper bound only)
# Check that guess is between lowest and highest (
# lower and upper bound)


# Number checking function goes here
def int_check(question, low=None, high=None):

    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

        while True :

            try 

