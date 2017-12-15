# PyChat 2K17

import random

botname = "Chatterbot"


def start():
    pass

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ['y','yes','yeah','yah','yea', 'ya','sure','okay','alright']:
            return True
        elif answer in ["n", "no", "nope", "nah", "nein"]:
            return False
   
def has_keyword(statement, keywords):
    statement = " " + statement
    for word in keywords:
        word = " " + word
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting",
                 "Do you really think so?",
                 "That's a stupid thing to talk about",
                 "Are you kidding?", "Really?",
                 "That surely is something, huh"]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()
    
    family_words = ["mother", "father", "brother", "sister"]
    teacher_words = ["cooper"]
    question_words = ["why", "where", "when", "how", "who", "what"]
    joke_words = ["jest", "joke"] 
    
    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is really fun."
    elif has_keyword(statement, question_words) or has_keyword(statement, ["?"]):
        response = "I'm not great at answering questions."
    elif has_keyword(statement, joke_words):
        response = "What do you call an elephant fused with a rhino?.\n" + botname + ": El-if-i-no!"
    else:
        response = get_random_response()

    return response

def play():
    talking = True
    blabber = 0

    print(botname +": Hello. I'm " + botname + ".")
    print(botname +": What's your name?")
    name = input("User: ")
    name = name[0].upper() + name[1:].lower()
    print(botname +": Hello " + name + " what would you like to talk about?")
    while talking:
        statement = input(name + ": ")

        if statement in ["bye", "cya", "toodles"]:
            talking = False
        elif blabber == [7,13,18,25]:
            print(botname + ": Are you aware that we've exchanged " + str(blabber) + " statements...")
        else:
            response = get_response(statement)
            print(botname + ": " +response)
            blabber += 1
            print(blabber)
        

    print(botname +": You're leaving so soon?")

start()
playing = True
while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
