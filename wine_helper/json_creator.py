import json

#generic function to create button
def create_button(text, payload):
	button = {}
	button['text'] = text
	button['payload'] = payload

	return button

#generic function to create criterion
def create_criterion(name, value):
	criterion = {}
	criterion['name'] = name
	criterion['value'] = value

	return criterion

def create_text_response(text)
	question = {}
	question['type'] = 'text'
	question['text'] = text

	return question