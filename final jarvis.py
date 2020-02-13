import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        print("Good Morning")
        speak("Good Morning")

    elif hour>=12 and hour<=15:
        print("Good Afternoon")
        speak("Good Afternoon")

    else:
        print("Good Evening")
        speak("Good Evening")

    time.sleep(1)
    speak("Welcome to Rajiv Gandhi International Airport Hyderabad")
    print("\nSpeak any of the following to get the service\nFLIGHT for flight information\nAIRPORT for airport information\nPNR for pnr information")
    time.sleep(1)
    speak("\nSpeak any of the following to get the service\nFLIGHT for flight information\nAIRPORT for airport information\nPNR for pnr information")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Wait....Calibrating Microphone")
        r.adjust_for_ambient_noise(source,duration=2)
        r.dynamic_energy_threshold = True
        print("It's your turn now....")
        r.phrase_threshold = 0.8
        audio = r.listen(source)
   
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language = 'en-IN')
        print("You said:",query)

    except Exception as e:
        print("Sorry.It's my fault.Will you say that again please...")
        speak("Sorry It's my fault will you say that again please...")
        query='None'
    
    return query

if __name__ == "__main__":
    wishme()
    Airport={'Port Blair':'IXZ','Visakhapatnam':'VTZ','Tirupati':'TIR','Pasighat':'IXT','Guwahati':'GAU','Patna':'PAT','Darbhanga':'DBR','Raipur':'RPR','Delhi':'DEL','Goa':'GOI','Ahmedabad':'AMD','Surat':'STV','Hisar':'HSS','Shimla':'SLV','Srinagar':'SXR','Ranchi':'IXR','Bangalore':'BLR','Mangalore':'IXE','Thiruvananthapuram':'TRV','Kochi':'COK','Bhopal':'BHO','Indore':'IDR','Aurangabad':'IXU','Mumbai':'BOM','Nagpur':'NAG','Pune':'PNQ','Imphal':'IMF','Shillong':'SHL','Aizawl':'AJL','Dimapur':'DMU','Bhubaneswar':'BBI','Puducherry':'PNY','Amritsar':'ATQ','Jalandhar':'AIP','Jaipur':'JAI','Chennai':'MAA','Madurai':'IXM','Tiruchirapalli':'TRZ','Hyderabad':'HYD','Agartala':'IXA','Dehradun':'DED','Varanasi':'VNS','Lucknow':'LKO','Kanpur':'KNU','Agra':'AGR','Siliguri':'IXB','Kolkata':'CCU','Durgapur':'RDP'}
    while True:
        query=takecommand()

        if 'flight' in query:
            initial='None'
            destination='None'
            date1='None'
            opt='None'
            date2='None'
            
            print("Enter Boarding Airport")
            speak("Enter Boarding Airport")
            while initial=='None':
                initial=takecommand()
            
            print("Enter Destination Airport")
            speak("Now,Enter Destination Airport")
            while destination=='None':
                destination=takecommand()
            
            print("Now,Enter Journey date in Year Month Date format(For example for 7 December 2019 just say 2019 12 7)")
            speak("Now,Enter Journey date Enter the date in Date Month year format.")
            while date1=='None':
                date1=takecommand()
            
            print("is it a round trip Respond in yes or no")
            speak("is it a round trip Respond in yes or no")
            while opt=='None':
                opt=takecommand()
            
            if opt=='yes':
                print("Enter return Journey date Enter the date in Date Month year format.")
                speak("Enter return Journey date Enter the date in Date Month year format.")
                while date2=='None':
                    date2=takecommand()
                webbrowser.open("https://www.google.com/flights?hl=en#flt="+Airport[initial]+"."+Airport[destination]+"."+date1+"*"+Airport[destination]+"."+Airport[initial]+"."+date2+";c:INR;e:1;sd:1;t:f")
                
            else:
                webbrowser.open("https://www.google.com/flights?hl=en#flt="+Airport[initial]+"."+Airport[destination]+"."+date1+";c:INR;e:1;sd:1;t:f;tt:o")    

        elif 'airport' in query:
            speak('Rajiv Gandhi International Airport is an international airport that serves Hyderabad, the capital of the Indian state of Telangana. It is located in Shamshabad, about 24 kilometres (15 mi) south of Hyderabad. It was opened on 23 March 2008 to replace Begumpet Airport. It is named after Rajiv Gandhi, former Prime Minister of India. It is the only airport in India ranking in AirHelp list of top 10 airports in the world')

        elif 'stop' in query:
            speak("Thank You I am going to sleep now")
            break

        elif 'what' and  'time' in query:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)
            speak(current_time)

        elif 'wikipedia' in query:
            speak("Searching Wikipedia......")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia.....")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening youtube in few seconds")
            webbrowser.open("youtube.com")

        elif 'search' and 'youtube' in query:
            query=query.replace("youtube"," ")
            query=query.replace("search"," ")
            query=query.replace("in"," ")
            speak("searching your query in youtube Give me a second")
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
            
        elif 'open google' in query:
            speak("Opening Google in few seconds")
            webbrowser.open("google.com")

        elif 'search' and 'google' in query:
            query=query.replace("google"," ")
            query=query.replace("search"," ")
            query=query.replace("in"," ")
            speak("searching your query in google Give me a second")
            webbrowser.open("https://www.google.com/search?client=firefox-b-d&q="+query)

        

            
            
        
