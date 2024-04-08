import serial
import serial.tools.list_ports
import pyttsx3 as sp
import speech_recognition as sr

bot = sp.init()

property1 = bot.getProperty('rate')  # Rate of dictation
bot.setProperty('rate', 175)  # Rate set to 175

property2 = bot.getProperty('voices')  # Voice type
bot.setProperty('voice', property2[1].id)  # Voice check

def speaking(text):
    bot.say(text)
    bot.runAndWait()

def arduino():
    ports = serial.tools.list_ports.comports()    
    using = None

    # Find the selected port in the list of available ports
    for port in ports:
        if "USB" in port.description and "SERIAL" in port.description:
            using = port.device
            print(using)

    # If the selected port is found, configure and open the serial connection
    if using:
        with serial.Serial(using, 9600) as serialinst:
            r = sr.Recognizer() 
            try:
                with sr.Microphone() as source:
                    # Background noise adjustments        
                    r.energy_threshold = 10000  # Prevent very low voices
                    r.adjust_for_ambient_noise(source, 1.2)
                    print("Listening...")
                    
                    # Listening
                    audio = r.listen(source)  # Listen from user
                    message = r.recognize_google(audio)  # Utilizing the Google API to get the text from the voice input
                    print("You said:", message)
                    
                    if "track" in message.lower():
                        # Sending "on" message to Arduino to activate sensor tracking
                        serialinst.write("on\n".encode('utf-8'))  # Send "on" message with a newline character
                    else:
                        speaking("Keyword 'track' not detected.")
                    
                # Receiving and printing sensor data from Arduino
                
                while True:
                    response = serialinst.readline().decode('utf-8').strip()
                    if response.startswith("BPM:"):
                        print("Arduino:", response)
                        speaking(response)
                    
            except KeyboardInterrupt:  # Catch Ctrl+C termination
                print("\nTerminating script...")
                serialinst.write("TERMINATE\n".encode('utf-8'))  # Send termination signal
    else:
        print("Selected port not found.")
        resp = "No Sensor Found!"
        speaking(resp)

#arduino()
