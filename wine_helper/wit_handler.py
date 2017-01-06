from wit import Wit
import json


# Sends response to server
def send(request, response):
    data = request['context']
    data['toPrint'] = response
    json_data = json.dumps(data)
    print('Sending to server...', json_data)




def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val



def getColor(request):
    context = request['context']
    entities = request['entities']
    print request
    color = first_entity_value(entities, 'wit_color')
    if entities:
        if color:
            context['type'] = 'text'
            context['api_call'] = True
            context['criterion'] = {}
            context['criterion']['name'] = 'color'
            context['criterion']['value'] = color
            context['true'] = ""
    else:
       context['type'] = 'text'
       context['text'] = 'Je n\'ai pas compris ce que vous voulez dire'
       context['false'] = ""
    return context


def getAnswer(request):
    context = request['context']
    entities = request['entities']
    print request

    context['answer'] = ''

    greetings = first_entity_value(entities, 'wit_greetings')
    color = first_entity_value(entities, 'wit_color')
    minprice = first_entity_value(entities, 'wit_minprice')
    maxprice = first_entity_value(entities, 'wit_maxprice')
    currency = first_entity_value(entities, 'wit_currency')

    if entities:
        if greetings:
            context['type'] = 'button'
            context['text'] = 'Quel vin souhaitez-vous ?'
            context['options'] = []
            # vin rouge
            rouge = {}
            rouge['text'] = 'Rouge'
            rouge['payload'] = 'Rouge'
            context['options'].append(rouge)
            # vin rose
            rose = {}
            rose['text'] = 'Rose'
            rose['payload'] = 'Rose'
            context['options'].append(rose)
            # vin blanc
            blanc = {}
            blanc['text'] = 'Blanc'
            blanc['payload'] = 'Blanc'
            context['options'].append(blanc)

        if color:
            context['type'] = 'text'
            context['api_call'] = True
            context['criterion'] = {}
            context['criterion']['name'] = 'color'
            context['criterion']['value'] = color

    else:
       context['type'] = 'text'
       context['text'] = 'Je n\'ai pas compris ce que vous voulez dire'
    return context


def getPrice(request):
    context = request['context']
    entities = request['entities']
    print request

    minprice = first_entity_value(entities, 'wit_minprice')
    maxprice = first_entity_value(entities, 'wit_maxprice')
    currency = first_entity_value(entities, 'wit_currency')

    return context


def proposeColor(request):
    context = request['context']
    entities = request['entities']
    print request

    context['type'] = 'button'
    context['text'] = 'Quel vin souhaitez-vous ?'
    context['options'] = []
    # vin rouge
    rouge = {}
    rouge['text'] = 'Rouge'
    rouge['payload'] = 'Rouge'
    context['options'].append(rouge)
    # vin rose
    rose = {}
    rose['text'] = 'Rose'
    rose['payload'] = 'Rose'
    context['options'].append(rose)
    # vin blanc
    blanc = {}
    blanc['text'] = 'Blanc'
    blanc['payload'] = 'Blanc'
    context['options'].append(blanc)
    return context



actions = {
    'send': send,
    'getColor': getColor,
    'getPrice': getPrice,
    'proposeColor': proposeColor
}



client = Wit(access_token=os.getenv('WIT_TOKEN'), actions=actions)

def treatment(request):
    session_id = 'my-user-session-41'
    context0 = {}
    context1 = client.run_actions(session_id, request, context0)
    #client.interactive()
    return context1


print treatment("apero")
print treatment("rouge")