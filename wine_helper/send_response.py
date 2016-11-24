import json
import api_tools as api
import Criteria as C

# Vendors
# https://github.com/geeknam/messengerbot
from messengerbot import MessengerClient, messages, attachments, templates, elements

# Initializing client
PAGE_ACCESS_TOKEN = "EAAYU6e7AspIBAHvYtRp44RebfWQGlVRUNTTIpqmd27i6nSHCW61noR7yDOrpGlzaRaRO2NreAXful5OlodZAy7xB9Y6SftRW9YfYl4aQ0MPD2HLa3Ey2k6hvfVfEVxuHIMmAkgJ9gnrbdFuVbXr6wMFQzPUteYmk0x5heegZDZD"
messenger = MessengerClient(access_token=PAGE_ACCESS_TOKEN)

# TODO: change this function
def send_facebook_message(fbid, received_message):
    if (True):
        ""
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
    fake_data_text = {}
    fake_data_text["type"] = "text"
    fake_data_text["api_call"] = "False"
    fake_data_text["text"] = "Bonjour petit robot"
    handle_text(fbid, json.dumps(fake_data_text))


def handle_text(fbid, data):
    recipient = messages.Recipient(recipient_id=fbid)
    data = json.loads(data)
    if (data["api_call"] == False):
        message = messages.Message(text=data["text"])
        request = messages.MessageRequest(recipient, message)
        messenger.send(request)
    else:
        criteria = data["criteria"]
        criteria_list = []
        for criterium in criteria:
            criteria_list.append(C.Criteria(criterium["name"],criterium["value"]))
        wine_list = api.get_wines_by_criteria(criteria)
        text = ""

        for wine in wine_list:
            text += "Nom: " + wine.get_name() + ", Appellation: " + wine.get_appellation() + ", Annee: " + wine.get_vintage() + "\n"
        message = messages.Message(text=text)
        request = messages.MessageRequest(recipient, message)
        messenger.send(request)

# TODO: write description for this function
def handle_button(fbid, data):
    recipient = messages.Recipient(recipient_id=fbid)
    data = json.loads(data)
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
