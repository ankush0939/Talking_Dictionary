## Talking_Dictionary

### Pre-Requisite
- The json library can parse JSON from strings or files. The library parses JSON into a Python dictionary or list. 
It can also convert Python dictionaries or lists into JSON strings.
- pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
- The OS module in python provides functions for interacting with the operating system. OS, comes under Python's standard utility modules.
- difflib: This module provides classes and functions for comparing sequences.

### Installing libraries
     pip install json
     pip install pyttsx3
     pip install os
     pip install difflib

PS: json, os and difflib are mostly available with python distribution, if not use the above commands accordingly. pyttsx3 has to be installed.

### Importing libraries
     import json
     import pyttsx3
     import os
     from difflib import get_close_matches

### Text-to-speech initialization
     engine = pyttsx3.init('sapi5')
     voices = engine.getProperty('voices')

     engine.setProperty('voice',voices[0].id)
     
sapi5 is a referance to male voice for windows. Init() is a function to create an object
of pyttsx3 type.
getproperty() gets the current value of an engine property.
sewproperty() queues a command to set an engine property. The new property value affects all utterances
queued after this command.

### Including json file 
     words_data = json.load(open("file name/location"))
     
Its pretty simple, we are basically taking a json file which contains all the wordmeanings in the form of a list of dictionaries. 
We need to include this file. This file is available in out github repossitory.

### Word meaning function
     def word_meaning(word):
      
         word = word.lower()

         if word in words_data:
             return words_data[word]
      
         elif word.title() in words_data:
             return words_data[word.title()]
      
         elif word.upper() in words_data:
             return words_data[word.upper()]
      
         elif len(get_close_matches(word, words_data.keys())) >0:
      
             similar_words_list = list(map(str, get_close_matches(word, words_data.keys())))
    
             ans = input("Did you mean %s instead? Enter 'Y' If yes or 'N' if No " % similar_words_list)
        
             if ans.lower() == 'y':
                 index = input("Enter the position number of word to select the word. Ex 1 or 2 or 3 : ")
                 return word_meaning(get_close_matches(word, words_data.keys())[int(index)-1])
             elif ans.lower() == 'n':
                 print("Word Doesnt exists. Please double check it!!!")
             else:
                 print("Sorry, We don't understand you!!!!")
         else:
             print("Word Doesnt exists. Please double check it!!!")
             
This function takes the word in input, checks whether its a valid word or not i.e. its spelling is correct or not. If yes, it searches the 
word in the json file and on successful search it gives out the meaning that is stored in the file. If no, then it searches for the best match 
and gives the option to choose among the best matches. If the user approves the approximation then they get the meaning of the word. If not
then there is no such word available.

### speak function
     def speak(audio):
         engine.say(audio)
         engine.runAndWait()
         
It is an user defined function. The pyttsx3 function say() pronounces the actual audio.
The runAndWait() function blocks while processing all currently queued commands.
Invokes callbacks for engine notifications appropriately.
Returns when all commands queued before this call are emptied from the queue.

### Driving code
     word = input("Enter a word :")
     
Here we need to enter the word to be searched.

     speak(word_meaning(word))
     
Lets evaluate this line inside out. 'word' is our input search which is passed to word_meaning() function which 
returns the meaning in text. This text is passed as a parameter to the speak function which pronounces the text given to it.
