# Initial word to guess
Word = ["F", "A", "I", "L", "E", "D"]
# List to store correct guesses by the user
wordbox = []
# Initial points
point = 0
# Initial chances
chance = 5

# Introduction message for the game
print("You have 5 chances. Every mistake will cost you 1 chance. Every correct answer will give you 1 point. So let's start!")

# Main game loop, continues until chances are exhausted or all letters are guessed
while chance > 0:
    # Prompt the user to enter a letter and convert it to uppercase
    UserInput = input("Enter a letter: ").upper()

    # Check if the guessed letter is in the word
    if UserInput in Word:
        print(f"You are right. {UserInput} is in the word.")

        # Add the correct guess to wordbox
        wordbox.append(UserInput)
        print("Current wordbox:", wordbox)

        # Remove the guessed letter from the Word list
        Word.remove(UserInput)
        # Increment points for a correct guess
        point += 1
        print(f"Points = {point}")
        print(f"Chances left: {chance}")

        # If all letters are guessed, break the loop
        if not Word:
            break
    else:
        # If the guess is incorrect
        print("You guessed it wrong.")
        # Decrement chances
        chance -= 1
        print(f"You have {chance} chances left.")
        # Decrement points if points are greater than 0
        if point > 0:
            point -= 1
            print(f"Points = {point}")

# End of game messages based on remaining chances
if chance == 0:
    print("Oh! You lost. You can try again though.")
else:
    print(f"Congratulations! You have won the game. The word is FAILED. Total points: {point}")