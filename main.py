import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "b6907d289e10d714a6e88b30761fae22"

def get_weather_data(city, api_key):
    params = {
        'q': city,
        'appid': api_key
    }
    response = requests.get(API_BASE_URL, params=params)
    return response.json()

def get_temperature(data, date_time):
    for forecast in data['list']:
        if forecast['dt_txt'] == date_time:
            temperature = forecast['main']['temp']
            return temperature
    return "Date and time not found in the forecast."

def get_wind_speed(data, date_time):
    for forecast in data['list']:
        if forecast['dt_txt'] == date_time:
            wind_speed = forecast['wind']['speed']
            return wind_speed
    return "Date and time not found in the forecast."

def get_pressure(data, date_time):
    for forecast in data['list']:
        if forecast['dt_txt'] == date_time:
            pressure = forecast['main']['pressure']
            return pressure
    return "Date and time not found in the forecast."

def main():
    city = "London,us"
    data = get_weather_data(city, API_KEY)

    while True:
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date_time = input("Enter date with time (e.g., YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature(data, date_time)
            print(f"Temperature: {temperature} °C")
        elif choice == '2':
            date_time = input("Enter date with time (e.g., YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(data, date_time)
            print(f"Wind Speed: {wind_speed} m/s")
        elif choice == '3':
            date_time = input("Enter date with time (e.g., YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(data, date_time)
            print(f"Pressure: {pressure} hPa")
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
