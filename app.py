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
    uid = profile.user_id
    user_name = profile.display_name #使用者名稱
    emsg = event.message.text
    shi_zone = ["宜蘭市","竹北市","苗栗市","頭份市","彰化市","員林市","南投市","斗六市","太保市","朴子市","屏東市","台東市","臺東市","花蓮市","馬公市"]
    #如果使用者傳出的訊息有XXX往XXX，在match_result就會有東西
    pattern = re.compile(r'(.+)往(.+)')
    match_result = pattern.match(emsg)
    
    if re.match("使用說明",emsg):

        emoji = [
            {"index" : 0,
             "productId" : "5ac21a18040ab15980c9b43e",
             "emojiId" : "085"},
             {"index" : 1,
             "productId" : "5ac21a18040ab15980c9b43e",
             "emojiId" : "085"},
             {"index" : 2,
             "productId" : "5ac21a18040ab15980c9b43e",
             "emojiId" : "085"},
             {"index" : 3,
             "productId" : "5ac21a18040ab15980c9b43e",
             "emojiId" : "085"}

        ]
        text_message = """捷運相關功能$請直接按下選單
提供查詢班次服務

儲存點相關功能
$新增儲存點：請輸入以下格式
@新增儲存點
地址
摘要

$查看儲存點：請輸入以下格式
@查看儲存點
XX縣/市/鄉/鎮/市/區

$刪除儲存點：請輸入以下格式(3種範例)
@刪除儲存點3
@刪除儲存點
高雄市
@刪除儲存點
三民區

$清除儲存點：請輸入以下訊息
@清除儲存點
"""
        message = TextSendMessage(text = text_message, emojis = emoji)
        line_bot_api.reply_message(event.reply_token,message)

    if re.match("高雄捷運",emsg):
        message = show_MRT()
        line_bot_api.reply_message(event.reply_token,message)

    if re.match("我的儲存點",emsg):
        pass

    if re.match("高雄捷運圖",emsg):
        image_message = ImageSendMessage(
            original_content_url = "https://i.imgur.com/XwjjdSi.jpg"
        )
        line_bot_api.reply_message(event.reply_token, image_message)

    #送出站別的選單(橘線)
    if re.match("橘線班次",emsg):
        message = show_orange()
        line_bot_api.reply_message(event.reply_token,message)

    #送出站別的選單(紅線)
    if re.match("紅線班次",emsg):
        message = show_red()
        line_bot_api.reply_message(event.reply_token,message)

    #如果收到的訊息是XXX往XXX，就送出時刻表的訊息給使用者
    if match_result:
        start = emsg.split("往")[0]
        direction = emsg.split("往")[1]
        my_MRT = MRT(start, direction)
        message = my_MRT.return_time_result()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(message))


    if emsg.startswith("@"):
        site = site_record()
        target_function = emsg[1:6] # @XX儲存點

        #####針對特定欄位的資料庫操作，需要把城市或區域抓出來
        if len(emsg.split("\n")) > 1:    
            is_city = any(emsg.split("\n")[1].endswith(d) for d in ["縣","市"]) and emsg.split("\n")[1] not in shi_zone
            city = emsg.split("\n")[1]
            is_zone = any(emsg.split("\n")[1].endswith(d) for d in ["鄉","鎮","區"]) or emsg.split("\n")[1] in shi_zone
            zone = emsg.split("\n")[1]
        
        if re.match("新增儲存點", target_function):
            address = emsg.split("\n")[1]
            abstract = emsg.split("\n")[2]
            message = site.add_todo(user_name, uid, address, abstract)
            

        elif re.match("查看儲存點", target_function):
            if len(emsg.split("\n")) == 1:
                message = site.display_all(uid)
            elif is_city:
                message = site.display_city(uid, city)
            elif is_zone:
                message = site.display_zone(uid, zone)
            

        elif re.match("刪除儲存點", target_function):
            if len(emsg.split("\n")) == 1:
                number = int(emsg[6:])
                message = site.delete_number(uid, number)
            elif is_city:
                message = site.delete_city(uid, city)
            elif is_zone:
                message = site.delete_zone(uid, zone)
            

        elif re.match("清空儲存點", target_function):
            message = site.delete_all(uid)
            
        line_bot_api.push_message(uid,TextSendMessage(message))




    

