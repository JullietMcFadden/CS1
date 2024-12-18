#cat
import random                                                                   #import random
import time                                                                     #import time
import os                                                                       #import os                                                       

new_weapon = ("new weapon")                                                     #set variable new_weapon to new weapon
comp_options = ["rock", "paper", "scissors"]                                    #make list comp_options and put rock, paper, scissors in it
print ("Welcome to rock, paper, scissors (answer q to quit, m for more options, a to add a weapon)") #print "Welcome to rock, paper, scissors (answer q to quit, m for more options, a to add a weapon)"
score = 0                                                                       #set variable score to 0
time.sleep(1)                                                                   #pasuses program for 1 second

game_mode = str.lower(input("do you want to play against the computer (type c) or with another player(type p)?\n"))#ask "do you want to play against the computer (type c) or with another player(type p)?" start a new line and set variable game_mode to input

while True:                                                                     #forever loop

    human = str.lower(input("choose rock, paper, or scissors\n"))               #set variable human equal to users response and make lower case
    comp = (random.choice(comp_options))                                        #set variable comp equal to random item from list comp_options
    time.sleep(1)                                                               #pasuses program for 1 second

    if game_mode == "p":                                                        #if variable game_mode is = to p
        os.system('cls')                                                        #clear the console
        print ("joining 2 player mode")                                         #print "joining 2 player mode"
        comp = str.lower(input("second player choose rock, paper, or scissors\n")) #ask "second player choose rock, paper, or scissors" and set variable comp to input

    if score >= 3:                                                              #if variable socre is greater than or equal to 3
        print ("congrats you won the game!")                                    #print "congrats you won the game!"
        break                                                                   #end forever loop

    elif score <= -5:                                                           #elif variable socre is less than or equal to -5
        print ("oh no, you lost the game")                                      #print "oh no, you lost the game"
        break                                                                   #end forever loop

    if human == "q":                                                            #if varible human = q
        print ("quit")                                                          #print "quit"
        break                                                                   #end forever loop

    elif human == "m":                                                          #elif varible human = m
        print ("you have unlcoked  more options!")                              #print "you have unlcoked  more options!"
        print ("now you know that you can use a stapler to win against all oponents options!") #print "now you know that you can use a stapler to win against all oponents options!
        print ("this is a special feature and only you can use it")             #print "this is a special feature and only you can use it"

    elif human == "a":                                                          #elif varible human = a
        print ("you have decided to create your own weapon!")                   #print "you have decided to create your own weapon!"
        new_weapon = input("choose a name for your weapon\n")                   #ask "choose a name for your weapon" and set new_weapon to the input
        print ("beware you dont know how this weapon will act")                 #print "beware you dont know how this weapon will act"
        print ("this is a special feature and only player 1 can use it")             #print "this is a special feature and only you can use it"
        human = new_weapon                                                      #set variable human = to variable new_weapon

    elif human != "rock" and human != "paper" and human != "scissors" and human != "stapler" and human != new_weapon and human != "m" and human != "a": #elif human doesnt equal rock, paper, scissors, stapler, m, a, and the value of new_weapon
        print ("invalid response")                                              #print "invalid response"
    
    elif human == comp:                                                         #elif variables human and comp are equal to eachother
        if game_mode == "c":                                                    #if varible game_mode = c
            print(comp)                                                         #print variable comp
        print (""".__  __                      __  .__      ._.
|__|/  |_  ______ _____    _/  |_|__| ____| |
|  \   __\/  ___/ \__  \   \   __\  |/ __ \ |
|  ||  |  \___ \   / __ \_  |  | |  \  ___/\|
|__||__| /____  > (____  /  |__| |__|\___  >_
              \/       \/                \/\/""")                               #print "it's a tie"
        

    elif (human == "rock" and comp == "scissors") or (human == "paper" and comp == "rock") or (human == "scissors" and comp == "paper") or (human == "stapler"):    #elif human = rock and comp = scissors, or human = paper and comp = rock, or human = scissors and comp = paper, or human = stapler
        if game_mode == "c":                                                    #if varible game_mode = c
            print(comp)                                                         #print variable comp
        print ("""                                 _       __
   __  ______  __  __  _      __(_)___  / /
  / / / / __ \/ / / / | | /| / / / __ \/ / 
 / /_/ / /_/ / /_/ /  | |/ |/ / / / / /_/  
 \__, /\____/\__,_/   |__/|__/_/_/ /_(_)   
/____/                                     """)                                 #print "You won!"
        score += 1                                                              #add 1 to variable score
                                                                  
    elif (human == "rock" and comp == "paper") or (human == "paper" and comp == "scissors") or (human == "scissors" and comp == "rock") or (human == new_weapon) or (comp == "stapler") or (comp == new_weapon):   #elif human = rock and comp = paper, or human = paper and comp = scissors, or human = scissors and comp = rock, or human = value of varible new_weapon, or comp = new_weapon or, comp = stapler
        if game_mode == "c":                                                    #if varibel game_mode = c
            print(comp)                                                         #print variable comp
        print ("""_  _   ___   __ __    __      ___    __  ______ __
\\\//  // \\\  || ||    ||     // \\\  (( \ | || | ||
 )/  ((   )) || ||    ||    ((   ))  \\\    ||   ||
//    \\\_//  \\\_//    ||__|  \\\_//  \_))   ||   ..""")                       #print "You Lost"
        score -= 1                                                              #subtract 1 from variable score
        
print ("your score is")                                                         #print "your score is"
print (score)                                                                   #print current value of score variable

