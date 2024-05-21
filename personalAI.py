import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import pyautogui
import pyscreeze
from edenAPI import talkToAi
from smtplib import *
import pywhatkit as kit
import sample
x=pyttsx3.init()
def speak(audio):
    x.say(audio)
    x.runAndWait()
# speak("Hi I am Itachi AI How can i help you")
def time():
    t=datetime.datetime.now().strftime("%H:%M:%S")
    # print(t)
    speak(t)
# time()

def sendEmail(to,msg):
    server = SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('blshvardhan15@gmail.com','svkp qcqz wepj frrn')
    server.sendmail("blshvardhan15@gmail.com",to,msg)
    server.close()

def youtube(search):
    kit.playonyt(search)

def browse(search):
    kit.search(search)

def whatsapp(num, msg):
    kit.sendwhatmsg_instantly(num, msg)

def date():
    y=str(datetime.datetime.now().year)
    m=str(datetime.datetime.now().month)
    d=str(datetime.datetime.now().day)
    speak(d)
    speak(m)
    speak(y)
    # print(y)
# date()
def wish():
    h = datetime.datetime.now().hour
    if h<12:
        speak("Good Morning ")
    elif h>=12 and h<=18:
        speak("Good Afternoon ")
    elif h>18 and h<=21:
        speak("Good Evening")
    else:
        speak("Good Night ")
    # speak("Hello Srinivas")
    speak("How can i help you today")
# str=input()
# wish()
def inp():
    x1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        x1.pause_threshold=1
        audio=x1.listen(source)
        try:
            print("Recognizing...")
            query = x1.recognize_google(audio,language='en-in')
            print(query)
        except Exception as e:
            print(e)
            speak("Can you repeat again")
            inp()
            return "None"
        return query
#inp()

def screenshot():
    im1 = pyscreeze.screenshot()
    im2 = pyscreeze.screenshot('C:/Users/blshv/OneDrive/Desktop/AI/image.png')

if __name__=="__main__":
    wish()
    while True:
        query = inp().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("I'm summarizing the wikipedia search...")
            query = query.replace("wikipedia", "")
            try:
                result = wiki.summary(query, sentences=2)
                print(result)
                speak(result)
            except Exception as e:
                print(e)
                speak("Explain more about what you want to search...")
        elif "screenshot" in query:
            speak("I'm taking screenshot of the screen...")
            screenshot()
        elif "youtube" in query:
            speak("What should I search in youtube")
            elem = inp()
            speak("opening youtube")
            youtube(elem)
            exit()
        elif "chrome" in query:
            speak("What should I search?")
            ques = inp()
            speak("Searching")
            browse(ques)
        elif "whatsapp" in query:
            try:
                speak("Enter the number...")
                number = input()
                speak("What is the messagge to be sent...")
                message = inp()
                whatsapp(number, message)
            except exception as e:
                print(e)
                speak(e, "Failed to send`")
        elif "exit" in query:
            speak("Your AI is shutting down...")
            speak("Hope you return...")
            exit()
        elif "remember" in query:
            speak("What I have to remember...")
            data = inp()
            speak("Yout said me"+data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "data history" in query:
            remember = open("data.txt","r")
            speak("The data in your history is", remember.read())
            remember.close()
        elif "email" in query:
            try:
                speak("To whom we have to send...")
                recipient = input()
                speak("What is your message")
                message = inp()
                sendEmail(recipient,message)
            except Exception as e:
                print(e)
                speak("Failed to attempt due to"+e)
        elif "play song" in query:
            sample.songPlayer(r'C:\FFOutput\ilu14.wav')
        elif "pause the song" in query:
            sample.songControl("pause")
        elif "resume the song" in query:
            sample.songControl("continue")
        elif "play" in query:
            try:
                sample.songPlayer("path")
            except Exception as e:
                print("please say play a song")
        elif "stop song" in query:
            sample.songControl("stop")
        elif "shutdown the system" in query:
            os.system('shutdown /s /t 1')
        elif "restart the system" in query:
            os.system('shutdown /r /t 1')
        else:
            print(talkToAi(query))
            speak(talkToAi(query))
        
