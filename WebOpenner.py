#Imports
import os
import time
import playsound
import speech_recognition as sr
import keyboard
import webbrowser
from gtts import gTTS

#Don't touch the close funtion to except from the os.system("Find in google you browser kill link.")
#One of the most requested one will be here.
#Google Kill Link : os.system("taskkill /im chrome.exe /f")
#Mozila Kill Link : os.system("taskkill /im firefox.exe /f")
#Only your default browser will work! because that's what the code will open!
def close(): 
    isListening = True
    while isListening == True:
        audio()
        if 'close' in say: #If you say the word close will kill the program and shutsdown the whole browser
            os.system("taskkill /im firefox.exe /f") #Change only this for change your default browser.
            print "The browser is closed!"
            isListening = False
        else:
            print say
            isListening = True

def web():
    #Webbrowsers
    #You can put and continue with other websites the same way
    if 'YouTube' in say:
        webbrowser.open("https://www.youtube.com/")
        close()
    elif 'Facebook' in say:
        webbrowser.open("https://www.facebook.com/")
        close()
    #Continue with other websites the same way as above and like:
    #elif 'something' in say: <-- 'something' is the word you will say in the whole speach
    #   webbrowser.open("https://www.what ever browser you like to open./") <-- Link of the web!
    #   close()

#You will need 100% microphone for this not Microphone(Camera & other).Headset Microphone.             
def audio(): #Do not Touch The Audio Funtion!
    global say
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        audio = r.listen(mic)
        say =''
        try:
            say = r.recognize_google(audio)
            print say
            web()
        except Exception as e:
            print 'exception' + str(e)

            return say


audio() #Starting the function.

    
