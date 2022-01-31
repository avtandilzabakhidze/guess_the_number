from itertools import count
from random import randrange
import math 
def main():   
    game_mode =int(input("which one you want to play \n press 1  \n press 2;")) 

    lowe_baund = int(input("Enter lower bound: "))
    upper_baund  = int(input("Enter heighter bound: "))
    if game_mode == 1:
         guess_the_number_user(lowe_baund,upper_baund )
    elif game_mode == 2:
        guess_the_number_computer(lowe_baund,upper_baund)




def guess_the_number_user(lowe_baund,upper_baund ):
    number_to_guess = randrange(lowe_baund,upper_baund )
    user_guess = math.inf
    counter = 0
    while number_to_guess != user_guess:
        counter+=1
        user_guess = int(input(f"guess the number between{lowe_baund} and {upper_baund} "))
        if user_guess<number_to_guess:
            print("Too smaill , try again: ")
        elif user_guess>number_to_guess:
            print("Too big , try again: ")
    
    game_over = input("to return to main menu press the (m),to quest press emter")
    if  game_over =="m":
        main()   
    print(f"you are correct{number_to_guess} in {counter} tryes" )
    return 0
def guess_the_number_computer(lowe_baund,upper_baund ):
    computer_guess = math.inf
    feedback = ' '
    guess_counte = 0
    while feedback != "c":
        guess_counte+=1
        computer_guess = randrange(lowe_baund,upper_baund )
        feedback =input(f"Is {computer_guess} correct (c) ,too low(l),or height (h) :")

        if feedback == "l":
            lowe_baund=computer_guess+1
        elif feedback == "h":
            upper_baund=computer_guess-1
        if lowe_baund == upper_baund:
            guess_counte+=1
            print(f"only number left is {lowe_baund}\n")
            computer_guess=lowe_baund
            break
    print(f"correct{computer_guess} in {guess_counte} tryes ")
    game_over = input("to return to main menu press the (m),to quest press emter")
    if  game_over =="m":
        main()   
    return 0
    
main()

