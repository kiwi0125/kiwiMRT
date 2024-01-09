from line_bot_api import *

from events.Msg_template import *
from events.MRTtime import *
from model.mongodb import *
import re
import twstock
import datetime
import schedule
import time

app = Flask(__name__)

#####連接資料庫，去抓使用者的選股######
def cache_users_stock():
    db=constructor_stock()
    nameList = db.list_collection_names()
    users = []
    for i in range(len(nameList)):
        collect = db[nameList[i]]
        cel = list(collect.find({"tag":"stock"}))
        users.append(cel)
    return users


#自己的Channel Access Token(在Messaging API底下)
line_bot_api = LineBotApi("wR6RWNy+d1LEYGfPCD0AbGehrEI+cPTQxChN5KftrpfD7JZbuwKIoj1Ys41AL8+S2tehpIAOJVeZihxBVyZnMi8YPeHpQT9PeMRzc+UfkGwoxcSYIc9H+5yLPh3HSvsR4cagMIIFHybDESjA0+CiewdB04t89/1O/w1cDnyilFU=")
#自己的Channel secret(在Basic Settings底下)
handler = WebhookHandler("5c7720c80fc66096c32f76253778ded8")

#監聽所有來自/callback的Post Request
@app.route("/callback", methods=["POST"])
def callback():
    #get X-Line-Signature header value
    signature = request.headers["X-Line_Signature"]

    #get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)




    #header webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    profile = line_bot_api.get_profile(event.source.user_id)
    # uid = profile.user_id
    # user_name = profile.display_name #使用者名稱
    emsg = event.message.text

    pattern = re.compile(r'(.+)往(.+)')
    # 使用正規表達式進行匹配
    match_result = pattern.match(emsg)
    


    if re.match("橘線班次",emsg):
        message = show_orange()
        line_bot_api.reply_message(event.reply_token,message)

    if re.match("紅線班次",emsg):
        message = show_red()
        line_bot_api.reply_message(event.reply_token,message)

    if match_result:
        start = emsg.split("往")[0]
        direction = emsg.split("往")[1]
        my_MRT = MRT(start, direction)
        message = my_MRT.return_time_result()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(message))

    

