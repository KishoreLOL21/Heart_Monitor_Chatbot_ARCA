#Alex Health Tracker AI

import pyttsx3 as sp
import speech_recognition as sr
import serial
import serial.tools.list_ports
import time as t

import Arduino_Python_Tracker as A

bot = sp.init()  # start the package functionalities

property1 = bot.getProperty('rate') # Rate of dictation
bot.setProperty('rate', 175) # Rate set to 175

property2 = bot.getProperty('voices') # Voice type
bot.setProperty('voice',property2[1].id) # Voice check

# Function to make the bot announce any text
def speaking(text):
    bot.say(text)
    bot.runAndWait() # wait after completing the above sentence Dictiation. Does not execute the nest line.

speaking("Hello sir, I'm Alex. Your Personal healthcare AI.")
speaking("I'm here to give you Personalised health care.")
speaking("How are You sir?")

r = sr.Recognizer() # Instantiate Voice Recognition

with sr.Microphone() as source:
    # Background noice adjusments        
    r.energy_threshold = 10000 # Prevent very low voices
    r.adjust_for_ambient_noise(source,1.2)
    print("Listenting...")
    
    # Listening
    audio = r.listen(source) # Listen from user
    text = r.recognize_google(audio)  # Utilising the Google API to get the text from the voice input
    print(text)
    
if "How" and "are" and "you" in text or "what" and "about" and "you" in text:  
    speaking("I am good.")
    r = sr.Recognizer()
    speaking("Please Tell your name so that we can familiarise")
    with sr.Microphone() as Source:
        r.energy_threshold = 10000 
        r.adjust_for_ambient_noise(Source,1.2)
        print("Listenting...")
        audio1 = r.listen(Source)
        name = r.recognize_google(audio1)
        print("Hello" + " " + name)
        speaking("Hello" + name)          
    
    speaking("How can I help you Today?")
        
else:
    speaking("Please Tell your name so that we can familiarise")
    r = sr.Recognizer()
    with sr.Microphone() as Source:
        r.energy_threshold = 10000 
        r.adjust_for_ambient_noise(Source,1.2)
        print("Listenting...")
        audio1 = r.listen(Source)
        name = r.recognize_google(audio1)        
        print("Hello" + " " + name)
        speaking("Hello" + name)  
        
    speaking("How can I help you Today?")
 
r = sr.Recognizer()
with sr.Microphone() as Source:
        r.energy_threshold = 10000 
        r.adjust_for_ambient_noise(Source,1.2)
        print("Listenting...")
        command = r.listen(Source)
        cmd = r.recognize_google(command)        
        if "Activate" and "Command" and "mode" in cmd:
            speaking("Activating Command Mode..")
            speaking("What would you like to do?")
            speaking("Check your body conditions now.")
            print("say command mode-1")
            speaking("or")
            speaking("Track and analyse your previous health Stats?")   
            print("Say command mode-2") 

r = sr.Recognizer()
with sr.Microphone() as Source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(Source,1.2)
    print("Listening...")
    user_mode = r.listen(Source)
    mode = r.recognize_google(user_mode)
    print(mode)
  
if "mode" and "one" in mode or "mode" and "1" in mode:
    speaking("Please Acknowledge by saying Track")
    
    A.arduino() 
    

        
    
    



 



