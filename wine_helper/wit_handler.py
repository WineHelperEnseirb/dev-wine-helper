from wit import Wit
import os
import json

import json_creator as jc

# Sends response to server



def treatment(request, sender_id):
    return client.run_actions(sender_id, request)


def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val


def askColor(request):
    context = request['context']
    print request

    #creation de la reponse de type bouton et ajout des boutons
    context['response'] = []
    question = {}
    question['type'] = 'text'
    question['text'] = 'Quel type de vin souhaitez-vous acheter? (rouge, rose, blanc, sucre, petillant, peu importe)'

    context['response'].append(question)

    return context

def getColor(request):
    entities = request['entities']
    #recuperation de la couleur du vin
    color = first_entity_value(entities, 'wit_color')

    context['criteria'].append(jc.create_criterion('color', color))



def askPrice(request):
    context = request['context']
    entities = request['entities']
    print request

    #recuperation de la couleur du vin
    color = first_entity_value(entities, 'wit_color')

    #creation de la reponse de type bouton et ajout des boutons
    context['response'] = []
    question = {}
    question['type'] = 'text'
    question['text'] = 'Quel prix de vin? (exemple : "entre 10 et 20 euros")'
    
    context['response'].append(question)

    return context

def send(request, response):
    print "sending to server..."

actions = {
    'askColor': askColor,
    'askPrice': askPrice,
    'getColor' : getColor,
    'send' : send
}


client = Wit(access_token=os.getenv('WIT_TOKEN'), actions=actions)

