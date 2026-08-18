# List, Tuple, Set
names = []

ai_basic_details = ("BabyBot",)

greetings = {
    "hello", "hi", "hey", "yo", "good morning",
    "good afternoon", "good evening", "howdy", "hiya", "heya",
    "hey there", "hi there", "hello there", "greetings", "sup",
    "what's up", "whats up", "wassup", "how are you", "how's it going",
    "hows it going", "how are things", "welcome", "morning", "afternoon",
    "evening", "good day", "salutations", "hey hey", "hey buddy"
}

salutations = {
    "bye", "farewell", "goodbye", "bye bye", "chat later", "later",
    "see you", "see ya", "see you later", "catch you later", "take care",
    "have a good day", "have a nice day", "until next time", "talk soon",
    "talk to you later", "gotta go", "got to go", "I'm off", "I'm out",
    "peace", "peace out", "see ya soon", "see you soon", "good night",
    "have a good night"
}

#Functions
def greet_user():
    print("BabyBot: Hello, I am BabyBot")
    print("What is your name?")


def get_user_name():
    userName = input().capitalize()
    names.append(userName)
    return userName


def introduce_user(userName):
    print(f"{userName}: {userName}")
    print(f"BabyBot: Hello there {userName}")


def respond_to_input(userInput, userName):
    
    if userInput == "how are you":
        print("BabyBot: I am doing good. How are you?")
        return True

    elif userInput in greetings:
        print(f"BabyBot: Hello there {userName}, how can I assist you today?")
        return True

    elif userInput == "what is your name":
        print(f"BabyBot: {ai_basic_details[0]}, a rule based assistant.")
        return True

    elif userInput == "what is my name":
        print(f"BabyBot: Your name is {userName}!")
        return True

    elif userInput == "what can you do":
        print("BabyBot: I can help you discuss your thoughts and provide helpful tips.")
        return True

    elif userInput in salutations:
        print("BabyBot: Goodbye!")
        return False

    else:
        print("BabyBot: I don't understand that yet!")
        return True


def chat(userName):
    while True:
        userInput = input(f"{userName}: ").lower()

        if not respond_to_input(userInput, userName):
            break

#Main
greet_user()

userName = get_user_name()

introduce_user(userName)

chat(userName)
