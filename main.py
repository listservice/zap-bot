from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():
    # Pegar a mensagem que foi enviada pelo usuário
    incoming_msg = request.values.get('Body', '').lower()

    # Criar uma resposta do Twilio
    resp = MessagingResponse()
    msg = resp.message()

    # Definir um menu de respostas baseado na mensagem recebida
    if 'oi' in incoming_msg:
        msg.body("Olá! Bem-vindo ao nosso serviço. Digite 'menu' para ver as opções.")
    elif 'menu' in incoming_msg:
        msg.body("1. Informações da Conta\n2. Falar com o suporte\n3. Meus pedidos\nDigite o número da opção desejada.")
    else:
        msg.body("Desculpe, não entendi sua resposta. Digite 'menu' para ver as opções.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
