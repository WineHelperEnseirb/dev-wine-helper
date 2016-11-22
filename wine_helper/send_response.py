# Vendors
# https://github.com/geeknam/messengerbot
from messengerbot import MessengerClient, messages, attachments, templates, elements

# Initializing client
PAGE_ACCESS_TOKEN = "EAAYU6e7AspIBAHvYtRp44RebfWQGlVRUNTTIpqmd27i6nSHCW61noR7yDOrpGlzaRaRO2NreAXful5OlodZAy7xB9Y6SftRW9YfYl4aQ0MPD2HLa3Ey2k6hvfVfEVxuHIMmAkgJ9gnrbdFuVbXr6wMFQzPUteYmk0x5heegZDZD"
messenger = MessengerClient(access_token=PAGE_ACCESS_TOKEN)

def post_facebook_message(fbid, received_message):
    handle_button(fbid, json.loads("{\"type\":\"button\",\"text\":\"Quel vin?\",\"options\": [{\"text\":\"Rouge\",\"payload\":\"Rouge\"},{{\"text\":\"Blanc\",\"payload\":\"Blanc\"}}]}"))


def handle_text(fbid, data):
    "TO DO"

def handle_button(fbid, data):
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
