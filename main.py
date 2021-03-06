import re
from twilio.rest import Client

account_sid = '<Your Twilio account SID>'
auth_token = '<Your Twilio auth token>'

client = Client(account_sid, auth_token)

from flask import Flask, redirect, render_template
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():

    if account_sid == '<Your Twilio account SID>' or auth_token  == '<Your Twilio auth token>':
        return "You must set up your Twilio account SID and auth token on lines 4, 5 in main.py"

    return render_template('main.html')

@app.route("/chat/")
def no_chat():
    return redirect('/')

@app.route('/chat/<number>')
def show_chat(number):
    # sanitize the phone number, remove anything that's not a number
    number = re.sub('[^0-9]', '', number)
    if number[0] != '1':
        number = '1' + number
    number = '+' +  number

    user_messages = getSMS(number)
    if len(user_messages) == 0:
        return "Couldn't find any messages to/from %s" % (number, )

    return render_template('main.html', messages=user_messages, user_number=number)

def getSMS(user_number):
    from_messages = client.messages.list(from_=user_number) # messages from them
    to_messages = client.messages.list(to=user_number) # messages to them
    all_messages = []
    for message in from_messages + to_messages:

        display_message = {
            'time': message.date_sent,
            'date_sent': message.date_sent.strftime("%b %d, %Y %H:%M"),
            'from_number': message.from_,
            'to_number': message.to,
            'message': message.body,
            'num_media': message.num_media,
            'from_them': message.from_== user_number
        }

        if int(message.num_media) > 0:
            media_domain = 'https://api.twilio.com'
            media_uris = []
            for media in  message.media.list():
                img_uri = media.uri
                if img_uri[-5:] == ".json":
                    img_uri = img_uri[:-5]

                media_uris.append(media_domain + img_uri)

            display_message['media'] = media_uris

        all_messages.append(display_message)

    # Sort all the messages by time
    all_messages.sort(key=lambda x: x['time'], reverse=False)

    return all_messages

if __name__ == "__main__":
    app.debug = False
    app.run(host='127.0.0.1', port=8000)
