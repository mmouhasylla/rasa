# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


import random

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

animals_db = {
    'puppy': 'https://i.imgur.com/9UDrkNM.jpeg',
    'butterflies': 'https://i.imgur.com/wuaYap6.jpeg',
    'koala': 'https://i.imgur.com/lDt3nJ8.jpeg',
    'kangaroo': 'https://i.imgur.com/7jKQ33i.jpeg',
    'elephant': 'https://i.imgur.com/KrHBQG0.jpeg',
    'turtle': 'https://i.imgur.com/qHwvqj8.jpeg',
    'giraffe': 'https://i.imgur.com/htl4k1N.jpeg',
    'panda': 'https://i.imgur.com/szGkrhj.jpeg',
    'dog': 'https://i.imgur.com/fSgnUKW.jpeg',
    'cat': 'https://i.imgur.com/pAugc21.jpeg',
    'horse': 'https://i.imgur.com/X2JsgbZ.jpeg',
    'girafe': 'https://i.imgur.com/iEFckkC.gif'
}

class ActionShowImage(Action):

     def name(self) -> Text:
         return "action_show_image"
        
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        animal_type = next(tracker.get_latest_entity_values("animal"),None)
        
        if not animal_type: 
             msg = f"I'm sorry, I don't have photos of that animal. Try another one! for exemple koala, kangaroo, puppy or panda!"
             dispatcher.utter_message(text=msg)
             return []
        
        animal_image = animals_db.get(animal_type,None) 
        
        dispatcher.utter_message(text = "Let me see... I found this... Does it help?",
        			             image=animal_image)

class ActionRandomImage(Action):

     def name(self) -> Text:
         return "action_random_image"
        
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        animal_type = random.choice(list(animals_db.keys()))
        
        animal_image = animals_db.get(animal_type,None) 
        
        dispatcher.utter_message(text = f"I found this cute {animal_type} ! Does it help?",
        			             image=animal_image)

class ActionFavoriteAnimal(Action):

     def name(self) -> Text:
         return "action_favorite_animal"
        
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        animal_type = next(tracker.get_latest_entity_values("animal"),None)
        if not animal_type: 
             msg = f"They are really cute !"
             dispatcher.utter_message(text=msg)
             return []
        
        animal_image = animals_db.get(animal_type,None) 
        
        dispatcher.utter_message(text = "Me too ! I found this picture !",
        			             image=animal_image)