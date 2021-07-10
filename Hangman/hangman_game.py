from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear
import random

#Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


end_of_game = False
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')
name=input("Enter your name: ")
print(f"Welcome {name} to hangman game.")
#Create blanks
display = []
for _ in range(word_length):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    # clear() #to remove all the backlogs .
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You have already guessed {guess}")
      
    
    #Check guessed letter
    for position in range(0,word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    # print(display)
    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess},that's not in the word.You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOOSE !!BETTER LUCK NEXT TIME")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("WOHOOO!! YOU WIN")

    # Import the stages from hangman_art.py 
    print(stages[lives])

print(f"The word was {chosen_word}.")