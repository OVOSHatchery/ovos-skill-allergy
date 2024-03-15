from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler
from .zipcoderequest import get_zip_from_ip, get_my_ip
from .allergyrequest import get_allergy_index_for_day


class AllergyLevel(OVOSSkill):

    def initialize(self):
        self.zipcode = self.settings.get('zipcode')
        if self.zipcode is None:
            ipaddress = get_my_ip()
            self.zipcode = get_zip_from_ip(ipaddress)
            self.settings['zipcode'] = self.zipcode


    @intent_handler('level.allergy.today.intent')
    def handle_level_allergy_today_intent(self, message):
        allergy_index_for_today, allergy_level_for_today = get_allergy_index_for_day(day='today', zipcode=self.zipcode)
        self.speak_dialog('level.allergy', {"allergy_index": allergy_index_for_today,
                                            "allergy_level": allergy_level_for_today,
                                            "zipcode": self.zipcode, "day": "today"})

        pass

    @intent_handler('level.allergy.tomorrow.intent')
    def handle_level_allergy_tomorrow_intent(self, message):
        allergy_index_for_tomorrow, allergy_level_for_tomorrow = get_allergy_index_for_day(day='tomorrow', zipcode=self.zipcode)
        self.speak_dialog('level.allergy', {"allergy_index": allergy_index_for_tomorrow,
                                            "allergy_level": allergy_level_for_tomorrow,
                                            "zipcode": self.zipcode, "day": "tomorrow"})


