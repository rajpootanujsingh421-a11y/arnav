from core.brain import Brain

brain = Brain()

while True:
    user = input("You : ")

    reply = brain.think(user)

    print("Arnav :", reply)