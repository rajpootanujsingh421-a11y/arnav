from core.brain import Brain

brain = Brain()

print("=" * 60)
print("🤖 Arnav AI Agent Test")
print("Type 'exit' to quit")
print("=" * 60)

while True:

    user = input("\nYou : ")

    if user.lower() in ["exit", "quit"]:
        break

    try:

        reply = brain.think(user)

        print(f"Arnav : {reply}")

    except Exception as e:

        print(f"\n[ERROR] {e}")