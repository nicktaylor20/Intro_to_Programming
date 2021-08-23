# DSC510
# THE FINAL PROJECT
# Dominick Taylor
# 3/3/2021
# This program will allow user to retrieve weather data for a specific city

import requests
import time
from pprint import pprint

apkey = '4006d2ed108c0576821201078d5e77b3'  # Global variable: API key for weather data API

# the cityapi function performs an API call to the weather site to retrieve data if user
# chooses to lookup weather info by a city type search
def cityapi(city, state, citycountry, temp):
    if temp == 'f':
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},{citycountry}&units=imperial&appid={apkey}')
        if r.status_code != 200:
            raise Exception("Sorry there was a connection error")  # Exception logic for API connection
    elif temp == 'c':
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},{citycountry}&units=metric&appid={apkey}')
        if r.status_code != 200:
            raise Exception("Sorry there was a connection error")  # Exception logic for API connection
    weather_dict = r.json()
    weatherprint(weather_dict)

# the zipcodeapi function performs an API call to the weather site to retrieve data if user
# chooses to lookup weather info by a zipcode type search
def zipcodeapi(zipcode, zipcountry, temp):
    if temp == 'f':
        d = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{zipcountry}&units=imperial&appid={apkey}')
        if d.status_code != 200:
            raise Exception("Sorry there was a connection error")  # Exception logic for API connection
    elif temp == 'c':
        d = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{zipcountry}&units=metric&appid={apkey}')
        if d.status_code != 200:
            raise Exception("Sorry there was a connection error")  # Exception logic for API connection
    weather_dict = d.json()
    weatherprint(weather_dict)

# the weatherprint function prints the weather information from either the zipcodeapi function
# or the cityapi function.
def weatherprint(weather_dict):
    print("\n")
    print(" ***YOUR WEATHER INFORMATION*** ")
    print("The current temperature in", weather_dict['name'], 'is', weather_dict['main']['temp'], 'degrees')
    print("It currently Feels Like: ", weather_dict['main']['feels_like'], 'degrees')
    print("The High for today is: ", weather_dict['main']['temp_max'], 'degrees')
    print("The Low for today is: ", weather_dict['main']['temp_min'], 'degrees')
    print("The current weather in ", weather_dict['name'], 'is:', weather_dict['weather'][0]['description'])
    print("Today's humidity:", weather_dict['main']['humidity'], '%')
    print("Wind speed: ", weather_dict['wind']['speed'])
    print("Sunrise time: ", time.strftime("%D %H:%M", time.localtime(int(weather_dict['sys']['sunrise']))))
    print("Sunset time: ", time.strftime("%D %H:%M", time.localtime(int(weather_dict['sys']['sunset']))))

# The main function ties everything together. Takes user input and calls the correct function to
# produce the proper weather data.
def main():
    print("******** Welcome to the WEATHER APP ********")
    print("\n")
    # while loop allows users to continuously search weather data
    while True:
        selection= input("To look up weather using the ZIPCODE enter a. for CITY NAME enter b: ")
        temptype= input("For FAHRENHEIT enter f for CELSIUS enter c: ")
        print("\n")
        if selection == 'a':
            zip = input("please enter zipcode( ex: '90210'): ")
            countrycode = input("please enter country code ( ex: 'US for United States): ")
            if temptype == 'f':
                zipcodeapi(zip, countrycode, 'f')
            elif temptype == "c":
                zipcodeapi(zip, countrycode, 'c')
            else:
                print("Opps! Something went wrong. Be sure to enter in valid data\n" 
                      "For Fahrenheit enter lowercase 'f'\n"
                      "For Celsius enter lowercase 'c'\n"
                      "Be sure you entered a valid Zipcode or City name\n")
        elif selection == 'b':
            city = input("please enter city name: ")
            state = input("please enter state code (ex: 'TX' for Texas): ")
            countrycode = input("please enter country code( ex: 'US for United States) ")
            if temptype == 'f':
                cityapi(city, state, countrycode, 'f')
            elif temptype == 'c':
                cityapi(city, state, countrycode, 'c')
            else:
                print("Opps! Something went wrong. Be sure to enter in valid data\n"
                      "For Fahrenheit enter lowercase 'f'\n"
                      "For Celsius enter lowercase 'c'\n"
                      "Be sure you entered a valid Zipcode or City name\n")
        else:
            print("Opps! Something went wrong. Be sure to enter in valid data\n"
                  "For Fahrenheit enter lowercase 'f'\n"
                  "For Celsius enter lowercase 'c'\n"
                  "Be sure you entered a valid Zipcode or City name\n")
        anothertemp = input("To enter another location enter y to quit enter q: ")
        if anothertemp == 'y':
            print("\n")
            continue
        elif anothertemp == 'q':
            print("\n")
            print("Thank you for using our app. Have a great day")
            break


main()