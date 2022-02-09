import pyttsx3

text_speech= pyttsx3.init()
voices = text_speech.getProperty("voices")
text = input("Please enter the text: ")
option = input('Press 0 for male voice and 1 for female voice : ')

# for male voice
if option=="0":
    text_speech.setProperty("voice", voices[0].id)
    text_speech.say(text)
    text_speech.runAndWait()

# for female voice
elif option=="1":
    text_speech.setProperty("voice", voices[1].id)
    text_speech.say(text)
    text_speech.runAndWait()

else:
    print(" Wrong Input")

