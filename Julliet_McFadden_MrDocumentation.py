import time
import datetime
def print_colored_text(text, color_name):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',  # Reset to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m')  # Default to white if color not found
    print(f"{color_code}{text}\033[0m")  # Print text with color and reset

print_colored_text ("alarm!", 'red')                                    #print message "Alarm!" in red

current_time = datetime.datetime(2024, 10, 23, 5, 20, 0)                #set current time to 5:20 AM
print(current_time.strftime("%H:%M:%S"), end='\r')                      #display current time

while True:                                                             #forever loop
    snooze = str.lower(input("\nsnooze? yes/no: "))                     #stores user response in variable snooze and starts new line and converts to lower case

    if snooze == "yes":                                                 #if user says yes to snooze
        print_colored_text ("go back to sleep again",'cyan')            #Print message "go back to sleep again" in cyan
        time.sleep(2)                                                   #pauses program for 2 seconds
        current_time += datetime.timedelta(minutes=5)                   #adds 5 minutes to current time
        print_colored_text("alarm!",'red')                              #Print message "Alarm!" in red
    elif snooze == "no":                                                #if user says no to sooze
        break                                                           #Ends forver loop
    else:                                                               #if user says anything but yes or no
        print_colored_text("invalid response",'red')                    #print message "invalid response" in red
        
print(current_time.strftime("%H:%M:%S"), end='\r')                      #Display current time
print_colored_text("\nwake up",'blue')                                  #print message "wake up" in red and start new line
current_time += datetime.timedelta(minutes=1)                           #adds 1 minutes to current time

print_colored_text("get out of bed",'magenta')                          #print message "get out of bed" in magenta
current_time += datetime.timedelta(minutes=1)                           #adds 1 minutes to current time


while True:                                                             #forever loop
    walk = str.lower(input("walk to the bathroom? yes/no: "))           #stores user response in variable walk

    if walk == "no":                                                    #if user says no to walk
        print_colored_text("go on my phone",'cyan')                     #print message "go on my phone" in cyan
        current_time += datetime.timedelta(minutes=5)                   #adds 5 minutes to current time
        time.sleep(2)                                                   #pauses program for 2 seconds
    elif walk == "yes":                                                 #if user says yes to walk
        current_time += datetime.timedelta(minutes=3)                   #adds 5 minutes to current time
        break                                                           #ends forever loop
    else:                                                               #if user says anything but yes or no
        print_colored_text("invalid response",'red')                    #print message "invalid response" in red

print(current_time.strftime("%H:%M:%S"), end='\r')                      #Display current time
print_colored_text("\nbrush my teeth",'blue')                           #Print message "brush my teeth" in blue and start new line
time.sleep(5)                                                           #pauses program for 5 seconds
current_time += datetime.timedelta(minutes=3)                           #adds 3 minutes to current time
print_colored_text("wash my face",'cyan')                               #Print message "wash my face" in cyan
time.sleep(1)                                                           #pauses program for 1 second
current_time += datetime.timedelta(minutes=10)                          #adds 10 minutes to current time
print_colored_text("choose my clothes for the day",'green')             #Print message "choose my clothes for the day" in green
time.sleep(1)                                                           #pauses program for 1 second
current_time += datetime.timedelta(minutes=1)                           #adds 1 minutes to current time
print_colored_text("finish getting ready",'yellow')                     #Print message "finish getting ready" in yellow
time.sleep(1)                                                           #pauses program for 1 second
current_time += datetime.timedelta(minutes=10)                          #adds 10 minutes to current time

while True:                                                             #forever loop
    moisturizer = str.lower(input("use moisturizer? yes/no: "))         #stores user response in variable moisturizer

    if moisturizer == "no":                                             #if user says no to moisturizer
        print_colored_text("don't use moisturizer",'magenta')           #Print message "don't use moisturizer" in magenta
        break                                                           #ends forever looop
    elif moisturizer == "yes":                                          #if user says yes to moisturizer
        print_colored_text("use moisturizer",'magenta')                 #Print message "use moisturizer" in magenta
        current_time += datetime.timedelta(minutes=2)                   #adds 2 minutes to current time
        break                                                           #ends forever loop
    else:                                                               #if user says anything but yes or no
        print_colored_text("invalid response",'red')                    #print message "invalid response" in red

print_colored_text(current_time.strftime("%H:%M:%S"), 'cyan')           #display current time in cyan

while True:                                                             #forever loop
    straighten = str.lower(input("\nstraighten my hair? yes/no: "))     #stores user response in variable starighten

    if straighten == "no":                                              #if user says no to straighten
        print_colored_text("don't straighten my hair",'yellow')         #Print message "don't straighten my hair" in yellow
        break                                                           #ends forever loop
    elif straighten == "yes":                                           #if user says yes to straighten
        print_colored_text("straighten my hair",'yellow')               #Print message "straighten my hair" in yellow
        current_time += datetime.timedelta(minutes=10)                  #adds 10 minutes to current time
        time.sleep(2)                                                   #pauses program for 2 seconds
        break                                                           #ends forever loop
    else:                                                               #if user says anything but yes or no
        print_colored_text("invalid response",'red')                    #print message "invalid response" in red

print_colored_text("pack my backpack",'green')                          #Print message "pack my backpack" in green
current_time += datetime.timedelta(minutes=1)                           #adds 1 minutes to current time
time.sleep(1)                                                           #pauses program for 1 second
print_colored_text("take my bag to the door",'cyan')                    #Print message "take my bag to the door" in cyan
current_time += datetime.timedelta(minutes=1)                           #adds 1 minutes to current time
time.sleep(1)                                                           #pauses program for 1 second

while True:                                                             #forever loop
    leave = str.lower(input("go out the door? yes/no: "))

    if leave == "no":                                                   #if user says no to leave
        print_colored_text("stay inside",'blue')                        #Print message "stay inside" in blue
        current_time += datetime.timedelta(minutes=5)                   #adds 5 minutes to current time
        time.sleep(2)                                                   #pauses program for 2 seconds
    elif leave == "yes":                                                #if user says yes to leave
        print_colored_text("walk to my car",'red')                      #Print message "walk to my car" in red
        current_time += datetime.timedelta(minutes=1)                   #adds 1 minutes to current time
        break                                                           #ends forever loop
    else:                                                               #if user says anything but yes or no
        print_colored_text("invalid response",'red')                    #print message "invalid response" in red
        
print(current_time.strftime("%H:%M:%S"), end='\r')                      #Display current time

print_colored_text("\nget into the car",'red')                          #Print message "get into the car" in red
time.sleep(1)                                                           #pauses program for 1 second
print_colored_text("drive to school",'blue')                            #Print message "drive to school" in blue
current_time += datetime.timedelta(minutes=40)                          #adds 40 minutes to current time
time.sleep(1)                                                           #pauses program for 1 second
print_colored_text("get starbucks",'magenta')                           #Print message "get starbucks" in magenta
current_time += datetime.timedelta(minutes=5)                           #adds 5 minutes to current time
time.sleep(1)                                                           #pauses program for 1 second
print_colored_text("arrive at school",'blue')                           #Print message "arrive at school" in blue

print_colored_text(current_time.strftime("%H:%M:%S"),'magenta')         #Display current time in magenta
