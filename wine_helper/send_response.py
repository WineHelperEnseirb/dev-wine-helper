# Vendors
# https://github.com/geeknam/messengerbot
from messengerbot import MessengerClient, messages, attachments, templates, elements

# Initializing client
messenger = MessengerClient(access_token=PAGE_ACCESS_TOKEN)

def post_facebook_message(fbid, received_message):
    handle_data(fbid, json.loads("{\"type\":\"button\",\"text\":\"Quel vin?\",\"options\": [{\"text\":\"Rouge\",\"payload\":\"Rouge\"},{{\"text\":\"Blanc\",\"payload\":\"Blanc\"}}]}"))


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
