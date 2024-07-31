import speech_recognition as sr

recognizer = sr.Recognizer()

try:
    with sr.Microphone() as mic:
        print("Please wait. Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(mic, duration=5)
        print("Say something!")
        audio = recognizer.listen(mic)

    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
