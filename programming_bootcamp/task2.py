"""
This program is a simple guess the number game which allows user to guess a random generated number.
User enters their guess, and the program will check it with the answer and tell them whether it's correct or not.
The game will keep on prompting the user for an input until the right answer is guessed by the user.

When the program is run, a number within the range of 1 to 100 will be generated randomly.
This is done within the generate_random_num function, which generates the random number using the randint method within the random module and returns it.

The next step is asking user for input, through the get_user_guess function.
The sole purpose of this function is to ask user for their guess and stores it as an integer.
In order to ensure that the value stored by the program is valid, try-except is used to catch a Value Error exception, which happens when the input is not an integer.
If-else is used to check if user's guess is within the given range. If the guess is not within the given range, an error message will be shown.
While loop is also used in this function to keep asking until a valid input is provided by the user.

check_user_guess function is used to check user's guess with the answer.
It takes two parameters, which are user's guess and the answer, and uses if-else to check it with the answer.
'if' statement will be executed first, and if it's false, the program will go to 'elif', and then 'else' if the previous two statements are false. 
Using this conditional ensures that only necessary statements are executed.
After comparing user's guess with the answer, the program will output one of the three conditions, which are correct, too low, and too high.

The last function is the play function, which is the main function of the program.
It's purpose is to execute the game so that it can be played by users.
This function will first call the generate_random_num function to generate a random number as answer. Next, get_user_guess will be called to get user input and validate it.
Then, the function check_user_guess will be used to check user's guess with the answer.
The program will inform the user whether their guess is correct, too low, or too high.
Since a while loop is used here, the game will keep on running until the user enters a correct guess.
"""

# import python library to generate random numbers
import random

# function to generate a random number
def generate_random_num():
    # randint method to generate a random number between 1 and 100 (range shown by digits in the bracket)
    num = random.randint(1,100)

    return num

# function to get user's guess
def get_user_guess():
    while True:
        try:
            # convert user's guess to an integer
            guess = int(input("Guess a number between 1 to 100: "))

            # check if user's guess is between the given range
            if 0 <= guess <= 100:
                return guess
            else:
                print("Invalid guess! Number should be an integer between 1 to 100.")
        # error for when input is not an integer
        except ValueError:
            print("Please enter a valid integer between 1 to 100.")

# function to check user's guess with the answer
def check_user_guess(guess, answer):
    # if user's guess is correct
    if guess == answer:
        print("Yay! You guessed the correct number!")
    # if user's guess is too low
    elif guess < answer:
        print("Your guess is too low!")
    # if user's guess is too high
    else:
        print("Your guess is too high!")

# main function which allows user to play the guessing game
def play():
    # generate a random number as the answer
    answer = generate_random_num()

    print("GUESS THE NUMBER")
    print("-----------------")
    guess = get_user_guess()

    check_user_guess(guess, answer)
    while guess != answer:
        guess = get_user_guess()
        check_user_guess(guess, answer)

# call the function to start the game  
play()