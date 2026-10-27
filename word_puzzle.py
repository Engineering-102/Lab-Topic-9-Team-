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
    print(puzzle)
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
        
if __name__ == "__main__":
    main()


def is_valid_guess(valid, guess): #Tyler
    counter = 0
    valid = valid.split()
    for x in guess:
        for y in valid:
            if x == y:
                counter += 1
                valid.remove(x)
    if counter == 10:
        return True
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
def make_numbers (puzzle, key):
    puzzle = puzzle.split(",")
    numbers = []
    for i in range(len(puzzle)):
        numbers.append(make_number(puzzle[i], key))
    return numbers

def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    words = input("Enter a word arithmetic puzzle: ")
    print()
    print_puzzle(words)
    guess = input("Enter your guess, for example ABSDEFGHIJ: ")
    if(is_valid_guess(words,guess)):
        num = make_numbers(words, guess)
        if(check_user_guess(num(1),num(2),num(3),num(4))):
            print("Good job!)")
        else:
            print("Try again!")
    else:
        print("Your guess should contain exactly the 10 unique letters used")
    
