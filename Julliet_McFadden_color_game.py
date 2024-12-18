import random   #allows the code to choose a random item from a list (import library)
import time #new line
import os   #new line

def print_colored_text(text, color_name): #a dictionary of colors are their ANSI code numbers including the option to reset the color to normal
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',  # Reset to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m')  #tells the computer to get the ANSI code for the provided color
    print(f"{color_code}{text}\033[0m")  #prints text with given color
round=0 #sets rounds to 0
score=0 #sets score to 0
colors= ['red','yellow','green','blue','purple','white']    #makes list of colors

name = input("whats your name?\n")  #asks the user their name
time.sleep(1)   #new line 
print(f"hello {name}, Welcome to the color guessing game. You will be presented with a color word that will be a certain color. To win correcly name the  color of the word, and not the word itself.") #tell the user their name and the object of the game
time.sleep(5)   #new line

while True:  #forever loop
    text_color = (random.choice(colors))    #text_color is a random color form colors list
    print_color = (random.choice(colors))   #print_color is a random color form colors list
    print("your word is....")   #new line print
    print_colored_text(text_color,print_color)  #prints the random text_color in print_color
    time.sleep(1)   #new line
    os.system('cls')    #new line

    user_guess=str.lower(input("quikcly! what color is it?\n")) #tells the user to quickly enter the color of the text
    
    if user_guess == print_color:   #if the user enters matches the color of the text
        print("congrats you got it!")   #it tells them they are correct
        time.sleep(1)   #new line
        score += 1  #adds 1 to their score

    else:   #if they do not quess the correct color 
        print("you go it wrong!")   #it tells them they are wrong
        time.sleep(1)   #new line

    round +=1   #adds 1 to round number
    print(f'you got {score}, out of {round} correct.')  #tells the user how many they got correct out of how many rounds
    time.sleep(1)   #new line
    while True: #new line
        play_again=str.lower(input("do you want to play again? yes/no\n"))  #it asks the user if they want to play again

        if play_again == "yes": #new line
            print("playing again...")   #new line
            break   #new line
        elif play_again == "no":    #if no
            print("ending game..")  #new line
            exit()  #it will end the forever loop (adjusted)
        else:   #new line
            print("invalid response")   #new line
    time.sleep(1)   #new line
