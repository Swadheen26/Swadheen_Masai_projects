import requests, json   # importing the Library

# Generated api key from openweathermap website.
api_key = 'd2d9527e33a83bbe9f2da7978e69531e'         

# Base URL to fetch the weather data.
base_URL = 'https://api.openweathermap.org/data/2.5/weather?q='  

# Taking city name from user as input.
city_name = input("Enter the city name: ")           

# Concatinating the URLs with city name.
complete_URL = base_URL + city_name + '&appid=' + api_key   

#  Fetching the weather data of given city.
response = requests.get(complete_URL)                

# verifing the status code, if successfully fetched or not.
if (response.status_code) == 200:     
    data = response.json()
    
    # assigning value to use this later to convert in to celsius.
    Kelvin = 273.15           
    
    # Reading only temperature from fetched json file as its assigned with 'main' key.
    curr_temp = data['main']['temp']
    
    # converting the unit of temperature from Kelvin to Celsius and rounding off upto 2 decimal.
    converted_temp = round(curr_temp - Kelvin,2)
    
    # used f string to print the user entered city_name along with the temperature.
    print(f"The temperature in {city_name} is {converted_temp}{chr(176)}C")   # chr(176) is used to print the degree symbol.
else:
    print("Invalid data or error in fetching data")

