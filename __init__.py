from adapt.intent import IntentBuilder
from mycroft.skills.core import (MycroftSkill, intent_handler, intent_file_handler)
import requests
from .zipcoderequest import get_zip_from_ip, get_my_ip
from .allergyrequest import get_allergy_index_for_day

class AllergyLevel(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.zipcode = self.settings.get('zipcode')
        if self.zipcode is None:
            ipaddress = get_my_ip()
            self.zipcode = get_zip_from_ip(ipaddress)
            self.settings['zipcode'] = self.zipcode


    @intent_file_handler("level.allergy.today.intent")
    def handle_level_allergy_today_intent(self, message):
        allergy_index_for_today, allergy_level_for_today = get_allergy_index_for_day(day='today', zipcode=self.zipcode)
        self.speak_dialog("level.allergy.today", {"allergy_index_for_today": allergy_index_for_today, "allergy_level_for_today":allergy_level_for_today, "zipcode":self.zipcode})
        pass

    @intent_file_handler("level.allergy.tomorrow.intent")
    def handle_level_allergy_tomorrow_intent(self, message):
        allergy_index_for_tomorrow, allergy_level_for_tomorrow = get_allergy_index_for_day(day='tomorrow', zipcode=self.zipcode)
        self.speak_dialog("level.allergy.tomorrow", {"allergy_index_for_tomorrow": allergy_level_for_tomorrow, "allergy_level_for_tomorrow": allergy_index_for_tomorrow, "zipcode":self.zipcode})


    def stop(self):
        pass


def create_skill():
    return AllergyLevel()
