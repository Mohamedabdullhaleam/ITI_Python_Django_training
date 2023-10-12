import requests

class WeatherAPIClient:
    def __init__(self, api_key):
        self.base_url = "https://api.weatherapi.com/v1"
        self.api_key = api_key

    def get_current_weather(self, location):
        """
        Get current weather information for a given location.

        Args:
            location (str): The location for which to retrieve weather information (e.g., "New York").

        Returns:
            dict: A dictionary containing current weather data.
        """
        endpoint = "/current.json"
        params = {
            "key": self.api_key,
            "q": location,
        }

        response = self._make_request(endpoint, params)
        return response.json()

    def get_forecast(self, location, days=1):
        """
        Get weather forecast information for a given location.

        Args:
            location (str): The location for which to retrieve weather forecast (e.g., "Los Angeles").
            days (int): Number of days to forecast (1 to 10).

        Returns:
            dict: A dictionary containing weather forecast data.
        """
        endpoint = "/forecast.json"
        params = {
            "key": self.api_key,
            "q": location,
            "days": days,
        }

        response = self._make_request(endpoint, params)
        return response.json()

    def _make_request(self, endpoint, params):
        try:
            response = requests.get(f"{self.base_url}{endpoint}", params=params)

            if response.status_code == 200:
                return response
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request error: {e}")

# Example usage:
if __name__ == "__main__":
    api_key = "a040f6a66d5442bb827221802232509"
    weather_client = WeatherAPIClient(api_key)

    location = "New York"
    current_weather = weather_client.get_current_weather(location)
    print("Current Weather in", location)
    print(current_weather)

    forecast_location = "Los Angeles"
    forecast_days = 5
    forecast = weather_client.get_forecast(forecast_location, days=forecast_days)
    print(f"Weather Forecast for {forecast_location} ({forecast_days} days)")
    print(forecast)
