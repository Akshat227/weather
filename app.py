import requests

Api_key = "lauda mera"
Base_url ="http://api.weatherapi.com/v1/current.json"

def weather(city):

    url = f"{Base_url}?key={Api_key}&q={city}&aqi=no"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city_name = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        feelslike = data["current"]["feelslike_c"]

        print(f"\nWeather in {city_name}, {region}, {country}")
        print(f"Temperature: {temp_c}°C")
        print(f"Feels Like: {feelslike}°C")
        print(f"Condition: {condition}\n")

city = input("Enter the desiered city: ")
weather(city)

