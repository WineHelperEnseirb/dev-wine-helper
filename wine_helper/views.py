#!/usr/bin/python
# -*- coding: utf-8 -*-

# Sytem dependencies
import json
from pprint import pprint

# Vendors
import requests
# https://github.com/geeknam/messengerbot
from messengerbot import MessengerClient, messages, attachments, templates, elements

# Django
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


#  ------------------------ Fill this with your page access token! -------------------------------
PAGE_ACCESS_TOKEN = "EAAYU6e7AspIBAHvYtRp44RebfWQGlVRUNTTIpqmd27i6nSHCW61noR7yDOrpGlzaRaRO2NreAXful5OlodZAy7xB9Y6SftRW9YfYl4aQ0MPD2HLa3Ey2k6hvfVfEVxuHIMmAkgJ9gnrbdFuVbXr6wMFQzPUteYmk0x5heegZDZD"
VERIFY_TOKEN = "verify_me" # TODO: change token

# Initializing client
messenger = MessengerClient(access_token=PAGE_ACCESS_TOKEN)

def post_facebook_message(fbid, received_message):
    # Warning: "hard-coded" filters. It should be delegate to Wit.ai
    if (received_message == "Bonjour"):
        handle_welcome(fbid, received_message)
    elif received_message == "Rouge" or received_message == "Blanc" or received_message == "Rose":
        handle_color(fbid, received_message)


def handle_welcome(fbid, received_message):
    recipient = messages.Recipient(recipient_id=fbid)
    red_button = elements.PostbackButton(
        title='Rouge',
        payload='Rouge'
    )
    white_button = elements.PostbackButton(
        title='Blanc',
        payload='Blanc'
    )
    rose_button = elements.PostbackButton(
        title='Rose',
        payload='Rose'
    )
    template = templates.ButtonTemplate(
        text='Bonjour, quelle couleur de vin desirez-vous ?',
        buttons=[
            red_button, white_button, rose_button
        ]
    )
    attachment = attachments.TemplateAttachment(template=template)
    message = messages.Message(attachment=attachment)
    request = messages.MessageRequest(recipient, message)
    messenger.send(request)

# TODO: change the function, call API
def handle_color(fbid, received_message):
    recipient = messages.Recipient(recipient_id=fbid)

    message = messages.Message(text=received_message)
    request = messages.MessageRequest(recipient, message)
    messenger.send(request)


class FacebookCallbackView(generic.View):
    """
    This endpoint serves as the Facebook Messenger callback
    The bot can be messaged at this url: http://m.me/scorelab.winehelper

    Cf. docs: https://developers.facebook.com/docs/graph-api/webhooks
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Handles server verification performed by Facebook
        """
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')
        if token == VERIFY_TOKEN:
            if challenge:
                return HttpResponse(challenge)
            else:
                HttpResponse('Error, invalid challenge')
        else:
            return HttpResponse('Error, invalid token')

    def post(self, request, *args, **kwargs):
        """
        Handles Facebook messages
        """
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(request.body.decode('utf-8'))

        pprint("My debug")
        pprint(json.dumps(incoming_message))

        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events
                if 'message' in message:
                    pprint(message)
                    post_facebook_message(message['sender']['id'], message['message']['text'])
                if 'postback' in entry:
                    pprint(message)
                    post_facebook_message(message['sender']['id'], message['postback']['payload'])
        return HttpResponse()
