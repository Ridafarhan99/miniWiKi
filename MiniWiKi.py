import json
from difflib import get_close_matches #help to correct user inputed word 

pap=json.load(open("data.json")) #pap holds all data from data.json

def wiki(w):
    w=w.lower() #turn all character into lowercase
    if w in pap:
        return pap[w] #it will return real value
    elif len(get_close_matches(w, pap.keys())) > 0: #this condition check thw wrong word or misspell word 
        yn=input("Did you mean %s instead?\nEnter 'Y' if yes, or 'N' if no: " % get_close_matches(w, pap.keys())[0]) #first value of related word's key sequence
        if yn=='Y':
            return pap[get_close_matches(w, pap.keys())[0]] #return first word from the key sequence
        elif yn=='N':
            return "Please check your word."
        else:
            return "Invalid entry."
    else:
        return "The word doesn't exist."
    
word=input("Enter the word you are curious about: ") #user input the main word

output=wiki(word)

if type(output) == list: #for removing unwanted "[],''"
    for line in output:
        print(line)
else:
    print(output)
