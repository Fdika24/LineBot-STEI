from flask import Flask, request, abort
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from tokens import line_bot_api, handler


app = Flask(__name__)


# stuff that you should never touch if you do not know how to build one
@app.route("/")
def index():
    print(line_bot_api, handler)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# this is the message handler
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):  # ini nih problemnya
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Apa??')
    )


if __name__ == '__main__':
    app.run()
