import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import smtplib
import random
import pyautogui
from PIL import Image
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk('Good Morning')
    elif hour >= 12 and hour < 18:
        talk('Good Afternoon')
    else:
        talk('Good Evening')
    talk('I am Simon, your personal assistant. How may I help you?')
engine.runAndWait()
wishMe()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chaudharyreepa@gmail.com', '9634853521')
    server.sendmail('chaudharyreepa@gmail.com', to, content)
    server.close()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'simon' in command:
                command = command.replace('simon', '')
                print(command)
    except:
        pass
    return command

def run_simon():
    command = take_command()
    print(command)
    if 'song' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())      

    elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com/")

    elif 'open google' in command:
            webbrowser.open("google.com") 

    elif 'email to veer' in command:
            try:
                talk("What should I say?")
                content = take_command()
                to = "veer.singh.cseaiml.2020@miet.ac.in"    
                sendEmail(to, content)
                talk("Email has been sent!")
            except Exception as e:
                print(e)
                talk("Sorry,I am not able to send this email")    

    elif 'how are you' in command:
        talk("I am fine, thanks for asking you")

    elif "search for" in command:
        search_term = command.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        talk("Here is what I found for" + search_term + "on google")

    elif 'on youtube' in command:
        search_term = command.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        talk("Here is what I found for " + search_term + "on youtube")

    elif "spotify" in command:
        search_term= command.split("for")[-1]
        url="https://open.spotify.com/search/"+search_term
        webbrowser.get().open(url)
        talk("You are listening to"+ search_term +"enjoy sir")  

    elif "amazon" in command:
        search_term = command.split("for")[-1]
        url="https://www.amazon.in/"+search_term
        webbrowser.get().open(url)
        talk("here is what i found for"+search_term + "on amazon.com")
               
    elif "open instagram" in command:
        search_term=command.split("for")[-1]
        url="https://www.instagram.com/"
        webbrowser.get().open(url)
        talk("opening instagram")
        
    elif "open facebook" in command:
        search_term=command.split("for")[-1]
        url="https://www.facebook.com/"
        webbrowser.get().open(url)
        talk("opening facebook")

    elif "open twitter" in command:
        search_term=command.split("for")[-1]
        url="https://www.twitter.com/"
        webbrowser.get().open(url)
        talk("opening twitter") 

    elif "open linkedin" in command:
        search_term=command.split("for")[-1]
        url="https://www.linkedin.com/"
        webbrowser.get().open(url)
        talk("opening linkedin")    

    elif "open github" in command:
        search_term=command.split("for")[-1]
        url="https://www.github.com/"
        webbrowser.get().open(url)
        talk("opening github")

    elif "open stackoverflow" in command:   
        search_term=command.split("for")[-1]
        url="https://www.stackoverflow.com/"
        webbrowser.get().open(url)
        talk("opening stackoverflow")

    elif "weather" in command:
        search_term = command.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        talk("Here is what I found for on google")

    elif "my mail" in command:
        search_term = command.split("for")[-1]
        url="https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        talk("here you can check your gmail")

    elif "goodbye" in command:
        talk("okey sir, byee and have a nice day")
        exit()
    

    else:
        talk('Please say the command again.')


while True:

    run_simon()