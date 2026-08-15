#List, Tuples, Set
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

#Greet the user
print("BabyBot: Hello, I am Babyot")

#Ask for user's name
print("What is your name?")
userName = input().capitalize()
names.append(userName)
you = names[0]
print(f"{you}: {userName}")

#Remember user's name

print(f"BabyBot: Hello there {userName} ")

#Respond to basic commands
while True:
    userInput = input(f"{you}: ").lower()

    if userInput == "how are you":
        print("BabyBot: I am doing good. How are you?")

    elif userInput in greetings:
        print(f"BabyBot: Hello there {userName}, How can I assist you today?")

    elif userInput == "what is your name":
        print(f"BabyBot: {ai_basic_details[0]}, a rule based assistant.")

    elif userInput == "what is my name":
        print(f"BabyBot: your name is {userName}!")

    elif userInput == "what can you do":
        print("I can help you discuss your thoughts and provide helpful tips")

    #elif greetings in userInput:
    #   print(f"BabyBot: Hello there {userName}, How can I assist you today?")

    elif userInput in salutations:
        print("BabyBot: Goodbye!")
        break

    else:
        print("I don't understand that yet!")
