import requests

def get_weather(city_name, api_key):
    """
    Fetch weather data for a given city using OpenWeatherMap API.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use metric units (Celsius)
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()

        # Extract relevant weather information
        city = data["name"]
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {weather_description.capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError:
        print("Error: Unable to retrieve weather information. Please check the city name or API key.")