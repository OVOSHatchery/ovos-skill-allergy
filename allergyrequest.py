import requests
from errors import InvalidZipError

from config import pollen_forecast_api, pollen_forecast_api_headers

def is_valid_zip_code(zip_code: str) -> bool:
    """Define whether a string ZIP code is valid."""
    return len(zip_code) == 5 and zip_code.isdigit()


def convert_allergy_index_to_level(index=0):
    #TODO define scale to map index to level: low,low-medium,medium, medium-high, high
    level = ''
    return level


def get_allergy_index_for_day(day=None, zipcode='12345'):
    try:
        if is_valid_zip_code(zipcode) is False:
            raise InvalidZipError

        response = requests.get(url='{api}/{zip}'.format(api=pollen_forecast_api,zip=zipcode),
                                     headers=pollen_forecast_api_headers)
        allergy_data = response.json()['Location']['periods']
        if day == 'today':
            return allergy_data[0]["Index"]
        if day == 'tomorrow':
            return allergy_data[1]["Index"]
    except IndexError:
             print("none")


