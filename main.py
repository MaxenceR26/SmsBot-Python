import vonage

# Vonage API !

# Grace à cette outils tu peux envoyer des messages, à n'importe qui tout en étant inconnu :P

# By Maxence.R

class BotMessage:
    def __init__(self):
        self.client = vonage.Client(key='TonApiKey', secret='TaCléSecrete')
        self.sms = vonage.Sms(self.client)

        self.name = None
        self.number = None
        self.message = None
        self.Data = None

    def SendMessage(self):
        self.name = input("Name : ")
        self.number = input("Number of phone : ")
        self.message = input("Message : ")

        self.Data = self.sms.send_message(
            {
                "from": self.name,
                "to": self.number,
                "text": self.message,
            }
        )

        self.Verification()

    def Verification(self):
        if self.Data["messages"][0]["status"] == "0":
            print("Le message à était envoyé avec succés.")
        else:
            print(f"Échec du message : {self.Data['messages'][0]['error-text']}")


BotMessage().SendMessage()
