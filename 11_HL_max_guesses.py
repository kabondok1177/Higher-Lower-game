# HL componenr 11 - Maximum guesses Calculator

import match

for item in range(0,4):   # loop component for easy testing...

    low = int(input("Low: "))   # use int check in due course
    high = int(input("high: "))  # use int check in due course

    range = high - low + 1
    max_raw = math.log2(range)  Finds maximum # of guesses use
    max_upped = math,ceil (max_raw)