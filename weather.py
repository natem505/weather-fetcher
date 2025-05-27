import requests
import os

def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")  # We'll set this later
    if not api_key:
        print("ERROR: API key not set. Set OPENWEATHER_API_KEY as an environment variable.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to get weather data. Check city name or API key.")
        return

    data = response.json()
    temp_c = data['main']['temp']
    desc = data['weather'][0]['description']
    country = data['sys']['country']
    temp_f = (temp_c * 9/5) + 32

    print(f"\n{city.capitalize()}, {country} is currently {temp_f:.1f}°F with {desc}.\n")


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
