from adapt.intent import IntentBuilder
from mycroft.skills.core import (MycroftSkill, intent_handler, intent_file_handler)
import asyncio
from aiohttp import ClientSession
from pyiqvia import Client
from pyiqvia.errors import IQVIAError


async def get_allergy_index_for_day(day=None) -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
        try:
            client = Client("20171", websession)
            allergy_data = await client.allergens.current()
            if day == 'today':
                return allergy_data['Location']['periods'][0]["Index"]
            if day == 'tomorrow':
                return allergy_data['Location']['periods'][1]["Index"]
        except IQVIAError as err:
            return err


class AllergyLevel(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        pass

    @intent_file_handler('level.allergy.today.intent')
    def handle_level_allergy_today_intent(self, message):
        allergy_index_for_today = asyncio.get_event_loop() \
            .run_until_complete(get_allergy_index_for_day(day='today'))

        self.speak_dialog("level.allergy.today", {"allergy_index_for_today": allergy_index_for_today})
        pass

    @intent_file_handler('level.allergy.tomorrow.intent')
    def handle_level_allergy_tomorrow_intent(self, message):
        allergy_index_for_tomorrow = asyncio.get_event_loop()\
            .run_until_complete(get_allergy_index_for_day(day='tomorrow'))

        self.speak_dialog("level.allergy.today", {"allergy_index_for_tomorrow": allergy_index_for_tomorrow})

    def stop(self):
        pass


def create_skill():
    return AllergyLevel()
