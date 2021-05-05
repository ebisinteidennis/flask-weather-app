import requests
import json

def country(code):
	response = requests.get("https://restcountries.eu/rest/v2/alpha/" + code)
	return json.loads(response.text)["name"]

def weather(cityName = "London"):
    key = "secret"
    url = "http://api.openweathermap.org/data/2.5/weather?q="
    try:
        response = requests.get(url + cityName + key, timeout=10)
        if response.status_code == 200:
        	return 200,json.loads(response.text),country(json.loads(response.text)["sys"]["country"])
        else:
        	return response.status_code,json.loads(response.text), ""
    except requests.exceptions.Timeout:
    	return 400,"Connection timeout",  "error"
    except requests.exceptions.ConnectionError:
    	return 400, "Connection error", "error"
    else:
        CountryName = Country(json.loads(response.text)["sys"]["country"])
        return json.loads(response.text)



# ()