from linebot import LineBotApi, WebhookHandler
from flask import Flask
line_bot_api = LineBotApi(
    'h5VFTqs4ZYn8avvBF6zjwtXEN+6FOVrFZT9e1+I3tiixnFDL5P12NTTG7ecCk4+s7wqWYu/kaCgQ8QGQ7Da'
    '/FLmvPHSbiDefh0DUCF8WZCOrFkfoluPEAwW2QzncxmvV9r4rvzX3A/+0mMhAWF2HCwdB04t89/1O/w1cDnyilFU=')  # Channel Access token

handler = WebhookHandler('dd88efa191a94a468d9016ce81533745')

app = Flask(__name__)
