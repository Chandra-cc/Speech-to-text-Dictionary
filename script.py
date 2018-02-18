import speech_recognition as sr
import time
import json
import time
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys(),cutoff=0.7))>0:
        yn=input("Did you mean '%s' instead? \nEnter Y if Yes, or N if No: " % get_close_matches(w,data.keys())[0])
        if yn == "Y" or yn=="y" or yn==" y" or yn==" Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N" or yn=="n" or yn==" n" or yn==" N":
            print("Entered word has no meaning!.\nplease double check it.")
        else:
            return "We didn't understand your entry."
    else:
        print("Entered word has no meaning!.\nplease double check it.")
#print("-----Dictionary-----")
#a=int(input("Enter how many words you want to search for :"))
#for i in range(a):
#    word=input("Enter a word: ")
#        for item in output:
#            print('--|>>','"',item,'"')
#    else:
#        print(output)

def speech():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nSay something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("\nYou said: " + r.recognize_google(audio))
        return(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
a=int(input("\nHow Many times do you wan to try: "))
while a:
    output=(translate(speech()))
    if type(output) == list:
        for item in output:
            print('The Meaning of your Word is --|>>','"',item,'"')
    else:
        print(output)
    a=a-1



time.sleep(5)
