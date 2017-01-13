#!/usr/bin/python
# -*- coding: utf-8 -*-

# System dependencies
import os
import json

# Vendors
from wit import Wit

import json_creator as jc


def treatment(request, sender_id):
    return client.run_actions(sender_id, request)


def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val


def askStoryline(request):
    context = request['context']
    print request

    context['response'] = []
    context['response'].append(jc.create_text_response('Bonjour, souhaitez vous un vin pour : un aperitif, un repas, un cadeau ?'))

    return context


def askColor(request):
    context = request['context']
    print request
    context['response'] = []
    context['response'].append(jc.create_whatever_button('Quel type de vin souhaitez-vous acheter? (rouge, rose, blanc, sucre, petillant)'))

    return context


def askPrice(request):
    context = request['context']
    print request

    #creation de la reponse de type bouton et ajout des boutons
    context['response'] = []
    context['response'].append(jc.create_whatever_button('Quel prix de vin? (exemple : "entre 10 et 20 euros", "moins de 100 euros"...)'))

    return context


def askAdjustment(request):
    context = request['context']

    context['response'] = []

    button_table = jc.create_button_table('Êtes-vous satisfait ou souhaitez-vous réajuster le prix ?')
    button_table['options'].append(jc.create_button('Je suis satisfait', 'satisfait'))
    button_table['options'].append(jc.create_button('Réajuster le prix', 'réajuster'))
    context['response'].append(button_table)

    return context


def sayGoodbye(request):
    context = request['context']

    context['response'] = []
    context['response'].append(jc.create_text_response('Merci d\'avoir utilisé mes services, je vais me coucher dis moi bonjour pour me réveiller si tu as besoin de moi !'))

    return context


def getColor(request):
    context = request['context']
    entities = request['entities']
    #recuperation de la couleur du vin
    color = first_entity_value(entities, 'wit_color')

    context['criteria'] = []
    context['criteria'].append(jc.create_criterion('color.fr', color))

    return context


def getPrice(request):
    context = request['context']
    print request

    entities = request['entities']
    min = first_entity_value(entities, 'minprice')
    max = first_entity_value(entities, 'maxprice')

    context['criteria'] = []
    context['criteria'].append(jc.create_criterion('priceMin', min))
    context['criteria'].append(jc.create_criterion('priceMax', max))
    #context['criteria'].append(jc.create_criterion('currency', currency))

    return context


def reset(request):
    context = request['context']
    context['action'] = 'reset'

    return context


def apiCall(request):
    context = request['context']
    context['action'] = 'api_call'

    return context


def send(request, response):
    print "sending to server..."


actions = {
    'askColor': askColor,
    'askPrice': askPrice,
    'askStoryline' : askStoryline,
    'askAdjustment' : askAdjustment,
    'sayGoodbye' : sayGoodbye,
    'getColor' : getColor,
    'getPrice' : getPrice,
    'reset' : reset,
    'apiCall' : apiCall,
    'send' : send
}


client = Wit(access_token=os.getenv('WIT_TOKEN'), actions=actions)
