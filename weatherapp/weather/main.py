from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def health():
    return "The service is running", 200

@app.route('/weather/<city>')
def get_weather(city):
    api_key = os.getenv("ecbc396f46mshb65cbb1f82cf334p1fcc87jsna5e962a3c542")
    if not api_key:
        return "OpenWeatherMap API key is missing", 500

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return jsonify(weather_data)
    except requests.exceptions.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0")
