from twilio.rest import Client
from twilio.rest import Client

TWILIO_SID = "ACad7c3a45b3b970de3f58d5f2edf50316"
TWILIO_AUTH_TOKEN = "ea669178fcb6768d3b4e8acf42c31785"
TWILIO_VIRTUAL_NUMBER = "+"
TWILIO_VERIFIED_NUMBER = "+94762193001"


class NotificationManager:
    pass

    # def __init__(self):
    #     self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    #
    # def send_sms(self, message):
    #     message = self.client.messages.create(
    #         body=message,
    #         from_=TWILIO_VIRTUAL_NUMBER,
    #         to=TWILIO_VERIFIED_NUMBER,
    #     )
    #     # Prints if successfully sent.
    #     print(message.sid)
