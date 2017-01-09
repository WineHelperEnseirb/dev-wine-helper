from wit import Wit
import os
import json


# Sends response to server
def send(request, response):
    data = request['context']
    json_data = json.dumps(data)
    print('Sending to server...', json_data)


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
    question['type'] = 'button'
    question['text'] = 'Quel couleur de vin?'
    question['options'] = []
    # vin rouge
    rouge = {}
    rouge['text'] = 'Rouge'
    rouge['payload'] = 'Rouge'
    question['options'].append(rouge)
    # vin rose
    rose = {}
    rose['text'] = 'Rose'
    rose['payload'] = 'Rose'
    question['options'].append(rose)
    # vin blanc
    blanc = {}
    blanc['text'] = 'Blanc'
    blanc['payload'] = 'Blanc'
    question['options'].append(blanc)

    context['response'].append(question)

    return context


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
    
    context['criteria'] = []
    criterion = {}
    criterion['name'] = 'value'
    criterion['value'] = color

    context['criteria'].append(criterion)
    context['response'].append(question)

    return context



actions = {
    'askColor': askColor,
    'askPrice': askPrice,
    'send': send
}



client = Wit(access_token=os.getenv('WIT_TOKEN'), actions=actions)

def treatment(request, sender_id):
    return client.run_actions(sender_id, request)

#a corriger:
#voir interet de la fonction send et de la fonction treatment
#dans la fonction treatment voir l'interet de session id