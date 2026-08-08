#List, Tuples, Set
names = []

ai_basic_details = ("BabyBot",)

greetings = {
    "hello",
    "hi",
    "hey",
    "yo",
    "good morning"
}

salutations = {
    "bye",
    "farewell",
    "goodbye",
    "bye bye",
    "chat later",
    "later"
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