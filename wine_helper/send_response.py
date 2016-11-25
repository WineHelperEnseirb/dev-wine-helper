#!/usr/bin/python
# -*- coding: utf-8 -*-

# Sytem dependencies
import json
from pprint import pprint

# Vendors
# https://github.com/geeknam/messengerbot
from messengerbot import MessengerClient, messages, attachments, templates, elements

import api_tools as api
from Criteria import Criteria

# Initializing client
PAGE_ACCESS_TOKEN = "EAAYU6e7AspIBAHvYtRp44RebfWQGlVRUNTTIpqmd27i6nSHCW61noR7yDOrpGlzaRaRO2NreAXful5OlodZAy7xB9Y6SftRW9YfYl4aQ0MPD2HLa3Ey2k6hvfVfEVxuHIMmAkgJ9gnrbdFuVbXr6wMFQzPUteYmk0x5heegZDZD"
messenger = MessengerClient(access_token=PAGE_ACCESS_TOKEN)

# TODO: change this function
def send_facebook_message(fbid, data):
    recipient = messages.Recipient(recipient_id=fbid)
    pprint("TYPE DATA")
    pprint(type(data))
    pprint("TYPE json.loads(data)")
    pprint(type(json.loads(data)))
    new_data = json.loads(data).decode('utf-8')
    if (new_data["type"] == "text"):
        handle_text(fbid, new_data)
    else:
        handle_button(fbid, new_data)

def post_facebook_message(fbid, received_message):
    fake_data = {}
    fake_data["type"] = "button"
    fake_data["text"] = "Quel vin ?"
    fake_data["options"] = []
    fake_button1 = {}
    fake_button1["text"] = "Rouge"
    fake_button1["payload"] = "rouge"
    fake_button2 = {}
    fake_button2["text"] = "Blanc"
    fake_button2["payload"] = "blanc"
    fake_data["options"].append(fake_button1)
    fake_data["options"].append(fake_button2)

    fake_data_api = {}
    fake_data_api["type"] = "text"
    fake_data_api["api_call"] = True
    fake_criteria1 = {}
    fake_criteria1["name"] =  "color"
    fake_criteria1["value"] =  "rouge"
    fake_data_api["criteria"] = []
    fake_data_api["criteria"].append(fake_criteria1)
    handle_text(fbid, json.dumps(fake_data_api))


def handle_text(fbid, data):
    """
    Handles the sending to messenger of a text message
    """
    recipient = messages.Recipient(recipient_id=fbid)
    if (data["api_call"] == False):
        message = messages.Message(text=data["text"])
        request = messages.MessageRequest(recipient, message)
        messenger.send(request)
    else:
        criteria = data["criteria"]
        criteria_list = []
        for criterium in criteria:
            crit = Criteria(criterium["name"],criterium["value"])
            criteria_list.append(crit)
        wine_list = api.get_wines_by_criteria(criteria_list)
        text = ""

        for wine in wine_list:
            text += wine.get_name()
            text += "," + wine.get_appellation()
            text += "," + wine.get_vintage()
            text += "\n"
        message = messages.Message(text=text)
        request = messages.MessageRequest(recipient, message)
        messenger.send(request)


def handle_button(fbid, data):
    """
    Handles the sending to messenger of a button template of postback buttons
    """
    recipient = messages.Recipient(recipient_id=fbid)
    text = data["text"]
    button_list = []
    for option in data["options"]:
        button_text = option["text"]
        button_payload = option["payload"]
        button_list.append(elements.PostbackButton(
            title=button_text,
            payload=button_payload
            )
        )
    template = templates.ButtonTemplate(
        text=text,
        buttons=button_list
    )
    attachment = attachments.TemplateAttachment(template=template)
    message = messages.Message(attachment=attachment)
    request = messages.MessageRequest(recipient, message)
    messenger.send(request)
