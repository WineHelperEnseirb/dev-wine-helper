import json, requests, random, re
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

#  ------------------------ Fill this with your page access token! -------------------------------
PAGE_ACCESS_TOKEN = "EAAYU6e7AspIBAOeiW55147fhZAgcchl3lJ45gb4xHlEvp8kdJyQoOb6ZCWGZCmEfhlaXom1bXuteol8XROjHtOLYdBJPZBbYO3GW1pqYkg8qb8ZCNWXHNkCTSbBR9oMIjz2Y6lmM3TNUcQesZAAZACQn741ZCAEHApuAHWG0OjnhFQZDZD"
VERIFY_TOKEN = "verify_me"

jokes = { 'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""", 
                     """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""], 
         'fat':      ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""", 
                      """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """], 
         'dumb': ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""", 
                  """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] }

# This function should be outside the BotsView class
def post_facebook_message(fbid, recevied_message):           
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + PAGE_ACCESS_TOKEN 
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())

# Create your views here.
class YoMamaBotView(generic.View):

    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events 
                if 'message' in message:
                    # Print the message to the terminal
                    pprint(message)
                    post_facebook_message(message['sender']['id'], message['message']['text'])
        return HttpResponse()    