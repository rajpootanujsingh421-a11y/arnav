import speech_recognition as sr


class Listener:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.recognizer.energy_threshold = 250
        self.recognizer.dynamic_energy_threshold = True

        self.recognizer.pause_threshold = 1.2
        self.recognizer.phrase_threshold = 0.3
        self.recognizer.non_speaking_duration = 0.8

    def listen(self):

        with sr.Microphone() as source:

            print("🎤 Listening...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            try:

                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=6
                )

            except sr.WaitTimeoutError:

                return None

        try:

            text = self.recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print("You :", text)

            return text.lower()

        except sr.UnknownValueError:

            return None

        except sr.RequestError:

            return None