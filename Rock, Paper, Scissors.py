import random
def rock_paper_scissors(user_choice, computer_choice):  #Creating a function called "rock_paper_scissors" that takes in two variables, "user_choice and computer_choice"
    if user_choice == computer_choice:                  #Creating if/else statements to establish win, lose and draw conditions
        print("It's a tie, try again...")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("You lose, get good")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("You lose, get good")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("You lose, get good")
    else:
        print("Incorrect spelling, try again")
        main()
    print("Would you like to play again?")                  #Creating the loop section to continuosly play the game until the user says "no" with an if/else statement
    addicted = input("Enter yes or no: ").lower()           ## Note: Also achievable by using a while loop
    if addicted == "yes":
        main()
    else:
        pass
def main():                                                 #Creating a function called "main" which will serve as the parent function of "rock_paper_scissors" to call at any point
    user_choice = input("Enter rock, paper or scissors: ").lower()              #Creating the user input variable coupled with ".lower()" to automatically account for case senstitive inputs
    possibilities = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possibilities)
    print("You chose: " + user_choice + " and " + "The computer chose: " + computer_choice)
    rock_paper_scissors(user_choice, computer_choice)
main()