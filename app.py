from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi('aZhJY+lMYJLpDsFtv3uRbuNcSbFL13zIlpH0q/WWEJEFKwvQdI/hIGJVq7v5K9WGQbXe0ylOz4NabjH+BeRyJntc+NUaRbc3kWLIXh7kJiSK6EROjhjQxtf+ciazf8qHC8cKOnlCGuZ2Y+JsPh0CfQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3d48cba5c80fcea640abcaffaaecf6ce')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
