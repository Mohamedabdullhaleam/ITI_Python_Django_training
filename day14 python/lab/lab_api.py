import requests
import json
def writeTojson(data):
    try:
        fileobj = open('user2.json', 'w')
    except Exception as e:
        print(e)
        return False
    else:
        # convert dict to string
        data_to_write = json.dumps(data,indent=2)
        fileobj.write(data_to_write)
        fileobj.close()

# api_key = 'a040f6a66d5442bb827221802232509'
# url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'
# print (url)
# response = requests.get(url)
#
# if response.status_code == 200:
#     data = response.json()
#     print("Current Weather in", location)
#     print(data)
#     writeTojson(data) ## show data in jason file
# else:
#     print(f"Request failed with status code: {response.status_code}")
class WeatherAPIClient:
    def __init__(self, api_key):
        self.url = "https://api.weatherapi.com/v1"
        self.api_key = api_key

    def get_current_temp(self, location):
        endpoint = "/current.json"
        params = {
            "key": self.api_key,
            "q": location,
        }
        response = self._make_request(endpoint, params)
        data = response.json()['current']['temp_c']## to get ony degree celisuis
        Time_associated=response.json()['location']['localtime']
        return data ,Time_associated
    def get_current_lat_and_long(self, location):
        endpoint = "/current.json"
        params = {
            "key": self.api_key,
            "q": location,
        }
        response = self._make_request(endpoint, params)
        latitude=response.json()['location']['lat']
        longtiude = response.json()['location']['lon']
        return longtiude,latitude

    def get_temperature_after(self, location,days,hours=None):
        endpoint = "/forecast.json"
        params = {
            "key": self.api_key,
            "q": location,
            "days": days,
        }
        response = self._make_request(endpoint, params)
        return response.json()['forecast']['forecastday'][0]['day']

    def _make_request(self, endpoint, params):
        try:
            response = requests.get(f"{self.url}{endpoint}", params=params)
            if response.status_code == 200:
                return response
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request error: {e}")



api_key = 'a040f6a66d5442bb827221802232509'
client1 = WeatherAPIClient(api_key)
location = "Cairo"
days = 5
desired_forcasted_weather_feautur ='maxtemp_c'



current_weather = client1.get_current_temp(location)[0]

associated_time = client1.get_current_temp(location)[1]

location_longlat= client1.get_current_lat_and_long(location)

forcast = client1.get_temperature_after(location,days)[desired_forcasted_weather_feautur]

writeTojson(current_weather)
writeTojson(location_longlat)
writeTojson(forcast)

print("Current Weather in", location)
print(f"temp of degree cel = {current_weather} \nand this was at {associated_time}")
print("Current location in", location)
print(f"the longitude is :{location_longlat[0]} and latitude is :{location_longlat[1]} ")
print(f"the corrosponding forcasted feature is :{desired_forcasted_weather_feautur } = {forcast} ")
