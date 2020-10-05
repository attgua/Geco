from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from database import DB, experiment_fields
#import importlib.util
#spec = importlib.util.spec_from_file_location("database", "/home/pido/Geco9000/rasa/Geco/database.py")
#foo = importlib.util.module_from_spec(spec)
#spec.loader.exec_module(foo)



class ShowField(Action):

    def name(self) -> Text:
        return "action_show_field"  

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ##MANCA AGGIORNARE DATABASE CON VALORI GIA SCELTI
        field = tracker.get_slot("field")

        dispatcher.utter_message("in our slot we have: {}".format(field))
              
        return []


class ShowValue(Action):

    def name(self) -> Text:
        return "action_show_value"  

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        

        field = tracker.get_slot("field")

        if(field== "cell"):
        #field_db = getattr(database, request_field + '_db')
            dispatcher.utter_message("you can choose between k562, h1a549 and cardiac cell.")
        if(field== 'source'):  
            dispatcher.utter_message("you can choose between tcga, encode, 1000 genomes, roadmap epigenomics, tads")
        if(field== 'source_ann'):   
            dispatcher.utter_message("you can choose between refseq, gencode, roadmap epigenomics")
        else:
            a=0

        return[]


class CheckValue(Action):

    def name(self) -> Text:
        return "action_control"  

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        field = tracker.get_slot("field")
        value =  tracker.get_slot(field)

        #field_db = getattr(database, request_field + '_db')
        
        if(True):
            dispatcher.utter_message("you have chose {} from {} ".format(value, field))
        else:
            dispatcher.utter_message("Il valore non c'è nel database.")
                
        return []

