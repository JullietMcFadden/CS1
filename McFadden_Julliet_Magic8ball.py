import random
import time
response = ["yes of course!!", "no...", "that could be a possiblity", "not availible right now..call back later!"]
question_word = ["what", "how", "who", "where", "when", "whose" "why", "which", "whom", "will", "whether"]

while True:
    question = (input("ask a question\n"))

    first_word = question.split()[0]
    if "?" in question or first_word in question_word:
        time.sleep(1)
        print (random.choice(response))
        break
    else:
        print ("try again you didn't ask a question")
