import pyttsx3

text_speech= pyttsx3.init()

text = input("Please enter the text: ")

text_speech.say(text)
text_speech.runAndWait()

