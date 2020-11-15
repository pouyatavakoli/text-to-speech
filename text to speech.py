# import the pyttsx module inside program
import pyttsx3

# initializing the module
voice_engine = pyttsx3.init()

#this will show and set the engines volume and speaking speed
rate = voice_engine.getProperty('rate')
volume = voice_engine.getProperty('volume')
voice = voice_engine.getProperty('voice')
 
print (rate)
print (volume)
print (voice)
# Testing different voice rates from 50 to 300( you can choose your favorite one) . 
newVoiceRate = 50
while newVoiceRate <= 300:
    voice_engine.setProperty('rate', newVoiceRate)
    voice_engine.say('Testing different voice rates.')
    voice_engine.runAndWait()
    newVoiceRate = newVoiceRate+50
 
voice_engine.setProperty('rate', 125)
# Testing different voice volumes from 0.1 to 1 ( you can choose your favorite one) . 
newVolume = 0.1
while newVolume <= 1:
    voice_engine.setProperty('volume', newVolume)
    voice_engine.say('Testing different voice volumes.')
    voice_engine.runAndWait()
    newVolume = newVolume+0.3
# you can set the above setting as you like 

# .say() function is used to speak the text you have written inside the function
voice_engine.say("Anything you write here will be spoken by your computer during the running of the program")

# this is used to process and run the program commands
voice_engine.runAndWait()