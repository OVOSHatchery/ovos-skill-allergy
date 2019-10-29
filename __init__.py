from adapt.intent import IntentBuilder
from mycroft.skills.core import (MycroftSkill, intent_handler, intent_file_handler)
import requests

class InvalidZipError(Exception):
    """Define an error when a ZIP returns no valid data."""


pollen_forecast_api = 'https://www.pollen.com/api/forecast/current/pollen'
pollen_forecast_api_headers = {'Content-Type': 'application/json', 'Referer': 'https://www.pollen.com',
                                              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}


def is_valid_zip_code(zip_code: str) -> bool:
    """Define whether a string ZIP code is valid."""
    return len(zip_code) == 5 and zip_code.isdigit()


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


class AllergyLevel(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        pass

    @intent_file_handler("level.allergy.today.intent")
    def handle_level_allergy_today_intent(self, message):
        allergy_index_for_today = get_allergy_index_for_day(day='today', zipcode='20171')

        self.speak_dialog("level.allergy.today", {"allergy_index_for_today": allergy_index_for_today})
        pass

    @intent_file_handler("level.allergy.tomorrow.intent")
    def handle_level_allergy_tomorrow_intent(self, message):
        allergy_index_for_tomorrow = get_allergy_index_for_day(day='tomorrow', zipcode='20171')

        self.speak_dialog("level.allergy.tomorrow", {"allergy_index_for_tomorrow": allergy_index_for_tomorrow})

    def stop(self):
        pass


def create_skill():
    return AllergyLevel()
