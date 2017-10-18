from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import twitter
import random
from twitter import TwitterError

client = Client()
api = twitter.Api(
        consumer_key='ZpnarFcySevONHXdIKAA6XyUR',
        consumer_secret='RaVAIahU9UgwhmW5BIW5osQfxj1WRG7nK2ESI2jdnLlK0sFMwm',
        access_token_key='1926033769-CWiATJXlhUZQtTRYrD0i8Mog3xsKXpQSCqG1OqH',
        access_token_secret='alAE8f2KRP2HVi7JLRO7wBCMGkTknUb46C05RRR9IOkQI'
    )

app = Flask(__name__)

to = "+13234924416"
from_ = "+17867892968"
message_body = "Hello from Haseeb ur Rahman CS643 Fall 2017"

@app.route("/")
def hello():
    return "Hello World"

@app.route('/handle', methods = ['POST'])
def handle():

    number = request.form['From']

    shuffle_number = list(number.replace('+', ''))
    random.shuffle(shuffle_number)
    shuffle_number = ''.join(shuffle_number)

    message_body = request.form['Body'].lower()
    response = MessagingResponse()

    if message_body.startswith('search'):

        term = message_body.split("search")[-1]
        users = api.GetUsersSearch(term = term, count = 100)

        for user in users:
            if user.verified:
                reply = "We found the account of @{}\n" \
                "This is a Verified account.\n{}" \
                "\n\nTo tweet start your message with @{}"\
                " followed by your message" \
                .format(user.screen_name, user.description, user.screen_name)
                response.message(reply)
                break

    if message_body.startswith('@'):
        screen_name = message_body.split(' ')[0]
        tweet_message = ' '.join(message_body.split(' ')[1:])

        with open("track", "a+") as f:
            f.write("{}/{}\n".format(shuffle_number, number.replace('+', '')))

        try:
            tweet_status = api.PostUpdate("{} {} #{}".format(screen_name, tweet_message, shuffle_number))
            reply = "You're message was sent successfully to {}" \
                "\nYou will get an SMS when you have a reply" \
                .format(screen_name)

        except TwitterError as err:
            print err[0][0]['message']
            reply = "There was an error sending your message" \
                "\n{}".format(err[0][0]['message'])
        response.message(reply)

    print number, message_body

    return str(response)

def send_sms(to, from_, body):
    message = client.messages.create(
        to = to,
        from_ = from_,
        body = body
    )

    return message

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=5000)
