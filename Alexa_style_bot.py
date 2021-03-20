import speech_recognition as sr
import pyttsx3
#pywhatkit lets you enable the application to do tasks
import pywhatkit
# get the application to recognize your commands through your microphone, if it cant recognize then it will pass
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
# we will now use the pytt package to get the application to speak back to me
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
 try:
    with sr.Microphone() as source:
        #we must now add in some text to let us know minime is listening
        print('listening...')
        voice = listener.listen(source)
        #we now need to turn the audio into text by using the google api
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'minime' in command:
            command = command.replace('minime', ' ')
            talk(command)

 except:
    pass
 return command

#now that we have mini me speaking and listening, its time to get her to work
def run_minime():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('cranking up ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') # I and P give you the 12 hour clock and the AM/PM format =, if we want 24 hours we can do %H:m%
        talk('Hello Sheila, the time is ' + time)
        print(time)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'what do you think' in command:
        talk('I am more of a techno girl myself, it gets my ints jumping')
    elif 'comedy' in command:
        talk('my code makes me laugh alright')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please can ypu say that again, I got lost in the sound of your magical voice')

while True:
    run_minime()
