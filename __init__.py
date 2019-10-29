from adapt.intent import IntentBuilder
from mycroft.skills.core import (MycroftSkill, intent_handler, intent_file_handler)
import requests
from allergyrequest import get_allergy_index_for_day


class AllergyLevel(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        #TODO load zip code from config & initial zip code config
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
