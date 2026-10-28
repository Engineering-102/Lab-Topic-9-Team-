# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:  Tyler Haidaczuk
# Jai Joshi
# Benjamin Sparks
# NA
# Section: 571
# Assignment: Lab Topic 8 Team
# Date: 27 October 2026
#

def print_puzzle(puzzle):
    """ Print puzzle as a long division problem. """
    puzzle = puzzle.split(",")
    for i in range(len(puzzle)):
        if i == 1:
            print(f"{len(puzzle[i].split('|')[1]) * '_': >16}")
        print(f"{puzzle[i]: >16}")
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def get_valid_letters(puzzle):
    """ Return a string of valid letters for the puzzle. """
    puzzle=puzzle.strip().replace(" ", "").replace(",", "").replace("|", "")
    valid_letters = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(puzzle)):
        if str(puzzle[i])in alphabet and not str(puzzle[i]) in valid_letters:
            valid_letters += str(puzzle[i])
    return valid_letters
    
def check_user_guess (dividend, divisor, quotient, remainder):
    """ Check if the user's guess is correct. """
    if dividend == quotient*divisor + remainder:
        return True
    else:
        return False
        
def is_valid_guess(valid_letters, guess): #Tyler
    guess=guess.strip().replace(" ", "").replace(",", "").replace("|", "")
    valid_guess = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(guess)):
        if str(guess[i])in valid_letters and not str(guess[i]) in str(valid_guess):
            valid_guess += str(guess[i])
    if len(guess) == 10 and len(valid_guess)==10:
        for i in range(len(valid_letters)):
            if valid_letters[i] in valid_guess:
                return True
            else:
                return False
    else:
        return False

def make_number(word, key): #Tyler
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    dictionary = {}
    int_equivalent = ""
    for i in range(len(key)):
        dictionary[key[i]] = numbers[i]
    for i in range (len(word)):
        if word[i] in dictionary:
            int_equivalent += dictionary[word[i]]
    return int(int_equivalent)

def make_numbers(puzzle, guess):
    parts = puzzle.split("|")

    left_words = parts[0].split(",")
    right_words = parts[1].split(",")

    quotient = left_words[0].strip()
    divisor = left_words[1].strip()
    dividend = right_words[0].strip()
    remainder = right_words[-1].strip()

    dividend_number = make_number(dividend, guess)
    quotient_number = make_number(quotient, guess)
    divisor_number = make_number(divisor, guess)
    remainder_number = make_number(remainder, guess)

    return (dividend_number, quotient_number,
            divisor_number, remainder_number)

def main():
    puzzle = input("Enter a word arithmetic puzzle: \n")
    print_puzzle(puzzle)
    valid_letters = get_valid_letters(puzzle)
    print()
    guess = input("Enter your guess, for example ABCDEFGHIJ: ")
    if not is_valid_guess(valid_letters, guess):
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
    else:
        numbers = make_numbers(puzzle, guess)
        dividend = numbers[0]
        quotient = numbers[1]
        divisor = numbers[2]
        remainder = numbers[3]
        if check_user_guess(dividend, quotient, divisor, remainder):
            print("Good job!")
        else:
            print("Try again!")

if __name__ == "__main__":
    main()
# Style Comment Thank God it finally works
