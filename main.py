from flask import Flask
from twilio.rest import Client
from twilio import twiml

client = Client()

app = Flask(__name__)

#to = "+13234924416"
to = "+13234924416"
from_ = "+17867892968"
message_body = "Hello from Haseeb ur Rahman CS643 Fall 2017"

@app.route("/")
def hello():
    # message = client.messages.create(
    #     to=to,
    #     from_=from_,
    #     body=message_body
    # )

    return "Hello World"
    # return "Message ID: {} sent to {} from {}".format(message.sid, to, from_)

@app.route('/handle', methods = ['POST'])
def handle():

    number = request.form['From']
    message_body = request.form['Body']

    print number, message_body

    response = twiml.messaging_response("sup")

def send_sms(to, from_, body):
    message = client.messages.create(
        to = to,
        from_ = from_,
        body = body
    )

    return message

# send_sms(to, from_, message_body)

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=5000)
