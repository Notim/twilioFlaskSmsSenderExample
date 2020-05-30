from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

client = Client("AC0f03bb985735f30e0b6cbb4bfda3d119", "38cf78680eac7a874848b2aeb6f83dfa")


@app.route("/enviar-sms")
def enviar_sms():
    destinatario = request.form['destinatario']
    mensagem     = request.form['mensagem']

    trial_number = '(208) 231-3221'

    message = client.messages \
        .create(
            body=mensagem,
            from_=trial_number,
            to=destinatario
        )

    if message.__dict__["_properties"].error_message is None:
        return "Ok"

    return "Erro"


if __name__ == "main":
    app.run()
