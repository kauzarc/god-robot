# Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
import os

from commandline import *
from user import *

users_list = []

app = Flask(__name__)
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot(ACCESS_TOKEN)

# We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    # if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    message_text = message['message'].get('text')

                    current_user = None

                    for user in users_list:
                        if user.id == recipient_id:
                            current_user = user
                            break
                    else:
                        users_list.append(User(recipient_id))
                        current_user = users_list[-1]

                    if message_text:
                        current_user.message_list.append(message_text)

                        response_sent_text = get_message(current_user)
                        send_message(recipient_id, response_sent_text)

                    # if user sends us a GIF, photo,video, or any other non-text item
                    # message_nontext = message['message'].get('attachments')
                    # if message_nontext:
                    #     response_sent_nontext = get_message()
                    #     send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def get_message(user):
    last_message = user.message_list[-1]

    if last_message[0:4] == "@bot":
        command = last_message[5:]
        if command == "help":
            return help_command(command)
        elif command == "test":
            return test_command(command)
        elif command[0:6] == "random":
            return random_command(command)
        elif command[0:3] == "say":
            return say_command(command)
        else:
            return no_command(command)
    return ""

# uses PyMessenger to send response to user


def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


if __name__ == "__main__":
    app.run()
