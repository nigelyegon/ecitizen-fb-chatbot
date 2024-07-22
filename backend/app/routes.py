from flask import request, jsonify
from . import db
from .models import Message

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    elif request.method == 'POST':
        data = request.json
        process_incoming_message(data)
        return "ok", 200

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid verification token"

def process_incoming_message(data):
    for entry in data['entry']:
        for messaging_event in entry['messaging']:
            sender_id = messaging_event['sender']['id']
            if 'message' in messaging_event:
                message_text = messaging_event['message']['text']
                handle_message(sender_id, message_text)

def handle_message(sender_id, message_text):
    # Generate response using Amazon Bedrock
   

# def generate_response(prompt):
#     # Use Amazon Bedrock API to generate a response
#     # This is a placeholder implementation
   

# def send_message(recipient_id, message_text):
#     # function to send the message back to front-end