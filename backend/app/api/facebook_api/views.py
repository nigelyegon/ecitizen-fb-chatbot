import os
import sys
from flask import request, Blueprint


facebook_api_bp = Blueprint("facebook_api_bp", __name__)


@facebook_api_bp.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        print("Gett Endpoint")
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    elif request.method == "POST":
        data = request.json
        # print(data)
        process_incoming_message(data)
        return "ok", 200


def verify_fb_token(token_sent):
    """
    Verifies facebook webhook subscription
    Successful when verify_token is same as token sent by facebook
    app"""
    print(os.getenv("VERIFY_TOKEN"))
    if token_sent == os.getenv("VERIFY_TOKEN"):
        return request.args.get("hub.challenge")
    return "Invalid verification token"


def process_incoming_message(data):
    for entry in data["entry"]:
        for messaging_event in entry["messaging"]:
            sender_id = messaging_event["sender"]["id"]
            if "message" in messaging_event:
                message_text = messaging_event["message"]["text"]
                print(message_text)
                handle_message(sender_id, message_text)


def handle_message(sender_id, message_text):
    pass
    # Generate response using Amazon Bedrock


# def generate_response(prompt):
#     # Use Amazon Bedrock API to generate a response
#     # This is a placeholder implementation


# def send_message(recipient_id, message_text):
#     # function to send the message back to front-end


def log(message):
    print(str(message))
    sys.stdout.flush()
