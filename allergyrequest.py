import requests
from .errors import InvalidZipError
from .config import pollen_forecast_api, pollen_forecast_api_headers

def is_valid_zip_code(zip_code: str) -> bool:
    """Define whether a string ZIP code is valid."""
    return len(zip_code) == 5 and zip_code.isdigit()


def convert_allergy_index_to_level(index=0):

    #TODO define scale to map index to level: low,low-medium,medium, medium-high, high
    level = ''
    if index < 2:
        level = "low"
    if 2 <= index< 4:
        level = "low-medium"
    if 4 <= index < 6:
        level = "medium"
    if 6 <= index < 8:
        level = "medium-high"
    if index > 8:
        level = "high"
    return level

def get_allergy_index_for_day(day='none', zipcode='12345'):
    try:
        if is_valid_zip_code(zipcode) is False:
            raise InvalidZipError

        response = requests.get(url='{api}/{zip}'.format(api=pollen_forecast_api,zip=zipcode),
                                     headers=pollen_forecast_api_headers)
        allergy_data_index = response.json()['Location']['periods'][1]["Index"]
        allergy_data_level = convert_allergy_index_to_level(index=allergy_data_index)
        return allergy_data_index, allergy_data_level
    except IndexError:
             print("none")


    except IndexError:
             print("none")