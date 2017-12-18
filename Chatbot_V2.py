# PyChat 2K17
#Eliot D.

import random

botname = "Chatterbot"


def start():
    print("╦ ╦╔═╗╦  ╦  ╔═╗┬")
    print("╠═╣║╣ ║  ║  ║ ║│")
    print("╩ ╩╚═╝╩═╝╩═╝╚═╝o")
    
def end():
    print("╔═╗╔═╗╔═╗╔╦╗╔╗ ╦ ╦╔═╗┬")
    print("║ ╦║ ║║ ║ ║║╠╩╗╚╦╝║╣ │")
    print("╚═╝╚═╝╚═╝═╩╝╚═╝ ╩ ╚═╝o")

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
                 "Oh, that's interesting.",
                 "Do you really think so?",
                 "That's a stupid thing to talk about.",
                 "Are you kidding?", "Really?",
                 "That surely is something, huh."]

    return random.choice(responses)

def get_random_response_family():
    responses = ["Tell me about your family.", 
                 "Family is an iteresting concept!",
                 "I never had a family..."]

    return random.choice(responses)
    
def get_random_response_teacher():
    responses = ["I hear Mr. Cooper is the best!",
                 "Mr. Cooper has the dankest memes.",
                 "Wow that Cooper is a real cool dude!"]

    return random.choice(responses)
  
def get_random_response_question():
    responses = ["I can't answer that.",
                 "I don't get what you're asking.",
                 "THIS QUESION IS BEYOND MY PROGRAMMING!"]

    return random.choice(responses)

def get_random_response_joke():
    responses = ["What do you call an elephant fused with a rhino?.\n" + 
                 botname + ": El-if-i-no!", "Did you hear about the hungry clock?.\n" + botname + ": It went back four seconds.", "What do you call a laughing jar of mayonnaise?.\n" + botname + ": LMAYO"]

    return random.choice(responses)

def get_random_response_laughter():
    responses = ["Was it really that funny?", "I'm glad you found that funny!", "haha!"]

    return random.choice(responses)
def get_response(statement):
    statement = statement.lower()
    
    family_words = ["mother", "father", "brother", "sister"]
    teacher_words = ["cooper", "teacher"]
    question_words = ["why", "where", "when", "how", "who", "what"]
    joke_words = ["jest", "joke", "funny"] 
    laughter_words = ["haha", "ha", "lol", "lmao", "lmfao"] 
    
    if has_keyword(statement, family_words):
        response = get_random_response_family()
    elif has_keyword(statement, teacher_words):
        response = get_random_response_teacher()
    elif has_keyword(statement, question_words) or has_keyword(statement, ["?"]):
        response = get_random_response_question()
    elif has_keyword(statement, joke_words):
        response = get_random_response_joke()
    elif has_keyword(statement, laughter_words):
        response = get_random_response_laughter()
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
        

    print(botname +": You're leaving so soon?")

start()
playing = True
while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
