
def ask_for_input():
    while True: 
        guess= input("Single letter: ")
        if  len(guess)==1 & guess.isalpha():
            check_guess(guess)
            break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")

def check_guess(guess):
    pass

ask_for_input()