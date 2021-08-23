# DSC510
# THE FINAL PROJECT
# Dominick Taylor
# 3/3/2021
# This program will allow user to retrieve weather data for a specific city

import requests
import time
from pprint import pprint

apkey = '4006d2ed108c0576821201078d5e77b3'


def cityapi(city, state, citycountry, temp):
    if temp == 'f':
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},{citycountry}&units=imperial&appid={apkey}')
        if r.status_code != 200:
            raise Exception("Sorry there was a connection error")
    elif temp == 'c':
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},{citycountry}&units=metric&appid={apkey}')
        if r.status_code != 200:
            raise Exception("Sorry there was a connection error")
    weather_dict = r.json()
    print("\n")
    print(" ***YOUR WEATHER INFORMATION*** ")
    print("The current temperature in", weather_dict['name'], 'is', weather_dict['main']['temp'],'degrees')
    print("It currently Feels Like: ", weather_dict['main']['feels_like'],'degrees')
    print("The High for today is: ",weather_dict['main']['temp_max'], 'degrees')
    print("The Low for today is: ",weather_dict['main']['temp_min'], 'degrees')
    print("The current weather in ",weather_dict['name'], 'is:', weather_dict['weather'][0]['description'])
    print("Today's humidity:",weather_dict['main']['humidity'], '%')
    print("Wind speed: ",weather_dict['wind']['speed'])
    print("Sunrise time: ", time.strftime("%D %H:%M", time.localtime(int(weather_dict['sys']['sunrise']))))
    print("Sunset time: ", time.strftime("%D %H:%M", time.localtime(int(weather_dict['sys']['sunset']))))


def zipcodeapi(zipcode, zipcountry, temp):
    if temp == 'f':
        d = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{zipcountry}&units=imperial&appid={apkey}')
        if d.status_code != 200:
            raise Exception("Sorry there was a connection error")
    elif temp == 'c':
        d = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{zipcountry}&units=metric&appid={apkey}')
        if d.status_code != 200:
            raise Exception("Sorry there was a connection error")
    weather_dict = d.json()
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


def main():
    print("******** Welcome to the WEATHER APP ********")
    print("\n")
    while True:
        selection= input("To look up weather using the ZIPCODE enter a. for CITY NAME enter b: ")
        temptype= input("For FAHRENHEIT enter f for CELSIUS enter c: ")
        print("\n")
        if selection == 'a' and temptype == 'f':
            zip = input("please enter zipcode: ")
            countrycode= input("please enter country code: ")
            zipcodeapi(zip, countrycode, 'f')
        elif selection == 'a' and temptype == 'c':
            zip = input("please enter zipcode: ")
            countrycode = input("please enter country code: ")
            zipcodeapi(zip, countrycode, 'c')
        elif selection == 'b' and temptype == 'f':
            city = input("please enter city name: ")
            state = input("please enter state code: ")
            countrycode = input("please enter country code: ")
            cityapi(city, state, countrycode, 'f')
        elif selection == 'b' and temptype == 'c':
            city = input("please enter city name: ")
            state = input("please enter state code: ")
            countrycode = input("please enter country code: ")
            cityapi(city, state, countrycode, 'c')
        anothertemp = input("To enter another location enter y to quit enter q: ")
        if anothertemp == 'y':
            continue
        elif anothertemp == 'q':
            print("\n")
            print("Thank you for using our app. Have a great day")
            break

main()

