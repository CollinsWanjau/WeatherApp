import requests
from dotenv 
def get_lan_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?
            q={city_name},{state_code},{country_code}&limit={limit}&
            appid={API_key}')
