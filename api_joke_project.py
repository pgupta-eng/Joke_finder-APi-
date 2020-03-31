#In this project we will be using api(hence the library request) to search jokes using a keyword entered by the user if we get multiple results on the keyword entered then one of those jokes will be displayed randomly hence random header file also is used
import requests
#import pyfiglet
#import termcolor
from random import choice
#my compiler did not support pyfiglet library but you may uncomment below lines to give a colorful header (in output) 
#header = pyfiglet.figlet_format("Dad Joke 3000")   
#header = termcolor.colored(header, color="magenta")
#print(header)

term = input("Let me tell you a joke! Give me a topic: ")
response_json = requests.get("https://icanhazdadjoke.com/search",headers={"Accept": "application/json"},params={"term": term}).json()
results = response_json["results"]
total_jokes = response_json["total_jokes"]
if total_jokes > 1:
    print(f"I've got {total_jokes} jokes about {term}. Here's one:\n",choice(results)['joke'])
elif total_jokes == 1:
    print(f"I've got one joke about {term}. Here it is:\n",results[0]['joke'])
else:
    print(f"Sorry, I don't have any jokes about {term}! Please try again.")