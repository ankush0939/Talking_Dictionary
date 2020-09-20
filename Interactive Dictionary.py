import json
import pyttsx3
import os
from difflib import get_close_matches

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

words_data = json.load(open("C:\\Users\ANKUSH\OneDrive\Desktop\Codes\Python\Interactive_Dictionary\words.json"))

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

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

word = input("Enter a word :")

speak(word_meaning(word))

