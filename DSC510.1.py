#DSC510
#Assignment 10.1
#Dominick Taylor
#2/21/2021
# Your program should allow the user to request a Chuck Norris joke as many times as they would like.

import requests
from pprint import pprint

url = "https://api.chucknorris.io/jokes/random"

print("Hello User ! If you like Chuck Norris jokes, you are the right place")
print(' '*21)


while True:
    new_joke = input("To receive a new Chuck Norris joke enter:'y'. To quit the program enter:'q'-  ")
    r = requests.request("GET", url)
    if r.status_code != 200:
        raise Exception("Sorry there was a connection error")
    joke_dict = r.json()
    jokes = joke_dict['value']
    if new_joke == 'y':
        print('\n')
        print('*************************')
        print('\n', jokes)
        print('\n')
        print('*************************')
        print('\n')
    elif new_joke == 'q':
        print('\n')
        print('Thank you for joining')
        break
    elif new_joke != 'y' or 'q':
        print('You entered an invalid value. Please try again')











