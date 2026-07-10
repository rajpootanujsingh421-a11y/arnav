from voice.voice_engine import VoiceEngine
from core.brain import Brain
from voice.speaker import Speaker


class VoiceChat:

    def __init__(self):
        self.voice = VoiceEngine()
        self.brain = Brain()
        self.speaker = Speaker()

    def start(self):

        print("=" * 50)
        print("🎤 Arnav Voice Chat")
        print("Type Ctrl+C to Exit")
        print("=" * 50)

        while True:

            try:
                user = self.voice.listen()

                if not user.strip():
                    print("❌ I couldn't hear anything.")
                    continue

                print(f"\nYou : {user}")

                response = self.brain.think(user)

                print(f"Arnav : {response}\n")
                self.speaker.speak(response)
                

            except KeyboardInterrupt:
                print("\n👋 Voice Chat Closed.")
                break

            except Exception as e:
                print(f"\n[Voice Error] {e}") 