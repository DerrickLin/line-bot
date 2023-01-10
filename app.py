from flask import Flask, request, abort
#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import random

#呼叫的檔案內容
from message import *
from weather import *

#======python的函數庫==========
import tempfile, os

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token    
line_bot_api = LineBotApi('dV5OUS7q/NkVp+tfxe/0hquAc+rc4WI3q/+QTBEW4+4V2lc55r1mLayCNZRtUiL6l1GMKobcOM1usLVfJJCRBl/rVfNumZZN8drYoZE8VS3Za90FEEUir76v081PipTS3SrrACwUj8vlOdzkygTftQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('26b0079b4d874f6b35d8e8b8f19d2a4f')
#Channel Access Token 和 Channel Secret 都在所創的linebot資料裡面找到
    

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text  # 使用者輸入的內容
    #主要以 elif 來做字串的判斷
    if '歌' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)  #回傳訊息 
    elif '音樂' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)     
    elif '火鍋' in msg:
        message = hotpot_Carousel()
        line_bot_api.reply_message(event.reply_token, message)
    elif '拉麵' in msg:
        message = ramen_Carousel()
        line_bot_api.reply_message(event.reply_token, message)    
    elif '動畫' in msg:
        message = animation_carousel()
        line_bot_api.reply_message(event.reply_token, message)  
    elif '動漫' in msg:
        message = animation_carousel()
        line_bot_api.reply_message(event.reply_token, message)     
    elif '天氣' in msg:
        message = [TextSendMessage(text = taipei_weather()),   #TextSendMessage 為傳送文字訊息
                   TextSendMessage(text = "我從中央氣象局找的\n不準不要怪我喔\U0001F617")] #\U開頭為emoji的unicode
        line_bot_api.reply_message(event.reply_token, message)     
        
    elif '五十嵐' in msg:
        message = [TextSendMessage(text = "不同地區價格會有差異喔，僅供參考"), 
                   ImageSendMessage(   
                        original_content_url = 'https://twcoupon.com/images/menu/p_50lan.jpg',  
                        preview_image_url = 'https://twcoupon.com/images/menu/p_50lan.jpg')
        ]   # ImageSendMessage 為回傳圖片訊息
        line_bot_api.reply_message(event.reply_token, message) 
        
    elif '50嵐' in msg:
        message = [TextSendMessage(text = "不同地區價格會有差異喔，僅供參考"), 
                   ImageSendMessage(
                        original_content_url = 'https://twcoupon.com/images/menu/p_50lan.jpg',
                        preview_image_url = 'https://twcoupon.com/images/menu/p_50lan.jpg')
        ]    
        line_bot_api.reply_message(event.reply_token, message)   
         
    elif '可不可' in msg:
        message = [TextSendMessage(text = "不同地區價格會有差異喔，僅供參考"), 
                   ImageSendMessage(
                        original_content_url = 'https://blake.com.tw/wp-content/uploads/2021/08/1629098823-bbfa894b35652115e7f09ef1e0093ba0.png',
                        preview_image_url = 'https://blake.com.tw/wp-content/uploads/2021/08/1629098823-bbfa894b35652115e7f09ef1e0093ba0.png')
        ]    
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '五桐號' in msg:
        message = [TextSendMessage(text = "不同地區價格會有差異喔，僅供參考"), 
                   ImageSendMessage(
                        original_content_url = 'https://www.wootea.com/upload/menu_b/ALL_menu_22L01_w7wtwebayv.png',
                        preview_image_url = 'https://www.wootea.com/upload/menu_b/ALL_menu_22L01_w7wtwebayv.png')
        ]    
        line_bot_api.reply_message(event.reply_token, message)         
    
    elif 'coco' in msg:
        message = [TextSendMessage(text = "不同地區價格會有差異喔，僅供參考"), 
                   ImageSendMessage(
                        original_content_url = 'https://achingfoodie.tw/wp-content/uploads/20210110090906_67.jpg',
                        preview_image_url = 'https://achingfoodie.tw/wp-content/uploads/20210110090906_67.jpg')
        ]    
    
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '麻古' in msg:
        message = [TextSendMessage(text = "不同地區價格會有差異喔，僅供參考"), 
                   ImageSendMessage(
                        original_content_url = 'https://twcoupon.com/images/menu/p_maculife_c.jpg',
                        preview_image_url = 'https://twcoupon.com/images/menu/p_maculife_c.jpg')
        ]    
        line_bot_api.reply_message(event.reply_token, message)    
    
    elif '迷客夏' in msg:
        message = [TextSendMessage(text = "不同地區價格會有差異喔，僅供參考"), 
                   ImageSendMessage(
                        original_content_url = 'https://nash.tw/wp-content/uploads/%E6%88%AA%E5%9C%96-2021-07-17-%E4%B8%8B%E5%8D%8811.53.27.png',
                        preview_image_url = 'https://nash.tw/wp-content/uploads/%E6%88%AA%E5%9C%96-2021-07-17-%E4%B8%8B%E5%8D%8811.53.27.png')
        ]    
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '清心' in msg:
        message = [TextSendMessage(text = "不同地區價格會有差異喔，僅供參考"), 
                   ImageSendMessage(
                        original_content_url = 'https://i0.wp.com/savingmagazines.com/wp-content/uploads/2022/01/%E6%B8%85%E5%BF%83%E7%A6%8F%E5%85%A8%E8%8F%9C%E5%96%AE1.jpg',
                        preview_image_url = 'https://i0.wp.com/savingmagazines.com/wp-content/uploads/2022/01/%E6%B8%85%E5%BF%83%E7%A6%8F%E5%85%A8%E8%8F%9C%E5%96%AE1.jpg')
        ]    
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '再睡' in msg:
        message = [TextSendMessage(text = "不同地區價格會有差異喔，僅供參考"), 
                   ImageSendMessage(
                        original_content_url = 'https://menus.tw/wp-content/uploads/2022/08/3.-%E8%8F%9C%E5%96%AE%EF%BC%BF%E8%A1%97%E9%82%8A%E5%BA%97.jpeg',
                        preview_image_url = 'https://menus.tw/wp-content/uploads/2022/08/3.-%E8%8F%9C%E5%96%AE%EF%BC%BF%E8%A1%97%E9%82%8A%E5%BA%97.jpeg')
        ]    
        line_bot_api.reply_message(event.reply_token, message) 
    
    elif '烏弄' in msg:
        message = [TextSendMessage(text = "不同地區價格會有差異喔，僅供參考"), 
                   ImageSendMessage(
                        original_content_url = 'https://i1.achangpro.com/img.huablog.tw/uploads/20220506141511_47.jpg',
                        preview_image_url = 'https://i1.achangpro.com/img.huablog.tw/uploads/20220506141511_47.jpg')
        ]    
        line_bot_api.reply_message(event.reply_token, message)  
    
    elif '龜記' in msg:
        message = [TextSendMessage(text = "不同地區價格會有差異喔，僅供參考"), 
                   ImageSendMessage(
                        original_content_url = 'https://i0.wp.com/savingmagazines.com/wp-content/uploads/2022/02/%E9%BE%9C%E8%A8%98%EF%BC%88%E5%8C%97%E9%83%A8%EF%BC%89%E8%8F%9C%E5%96%AE.jpg',
                        preview_image_url = 'https://i0.wp.com/savingmagazines.com/wp-content/uploads/2022/02/%E9%BE%9C%E8%A8%98%EF%BC%88%E5%8C%97%E9%83%A8%EF%BC%89%E8%8F%9C%E5%96%AE.jpg')
        ]    
        line_bot_api.reply_message(event.reply_token, message)
          
    elif '謝謝' in msg:
        answer = random.randint(0, 3)  #將不同的回覆形式寫進list裡，再利用亂數隨機回覆
        message = [TextSendMessage(text ="不客氣拉^_^"),
                   TextSendMessage(text ="不客氣寶貝"),
                   StickerSendMessage(package_id=8525, sticker_id=16581303),  
                   StickerSendMessage(package_id=6632, sticker_id=11825376)]  #StickerSendMessage 為回傳貼圖訊息
        line_bot_api.reply_message(event.reply_token, message[answer])
        
    elif '早安' in msg:
        answer1 = random.randint(0, 2)
        message = [TextSendMessage(text ="早安寶貝"),
                   TextSendMessage(text ="Good Morning"),
                   TextSendMessage(text ="早安，好想賴床喔zzz")]
        line_bot_api.reply_message(event.reply_token, message[answer1])
    
    elif '午安' in msg:
        answer2 = random.randint(0, 3)
        message = [TextSendMessage(text ="午安寶貝"),
                   TextSendMessage(text ="睡那麼晚，太陽公公曬屁股了"),
                   TextSendMessage(text ="睡那麼晚，昨天晚上去哪了阿?"),
                   TextSendMessage(text = "午安，午餐吃了嗎?")]
        line_bot_api.reply_message(event.reply_token, message[answer2])
          
    elif '晚安' in msg:
        answer3 = random.randint(0, 3)
        message = [TextSendMessage(text = "晚安寶貝\U0001F493"),
                   TextSendMessage(text = "晚安\U0001F634"),
                   StickerSendMessage(package_id=8525, sticker_id=16581309),
                   StickerSendMessage(package_id=6362, sticker_id=11087943)]
        line_bot_api.reply_message(event.reply_token, message[answer3]) 
    
    elif '渴' in msg:
        message = TextSendMessage(text = "可以輸入飲料店店名\U0001F379\n我知道的話會傳菜單給你喔!")                            
        line_bot_api.reply_message(event.reply_token, message) 
        
    elif '飲料' in msg:
        message = TextSendMessage(text = "可以輸入飲料店店名\U0001F379\n我知道的話會傳菜單給你喔!")                            
        line_bot_api.reply_message(event.reply_token, message)        
          
    elif '手搖' in msg:
        message = TextSendMessage(text = "可以輸入手搖飲店名\U0001F379\n我知道的話會傳菜單給你喔!")                            
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '菜單' in msg:
        message = TextSendMessage(text = "可以輸入手搖飲店名\U0001F379\n我知道的話會傳菜單給你喔!")                            
        line_bot_api.reply_message(event.reply_token, message) 
           
    elif '喝' in msg:
        message = TextSendMessage(text = "可以輸入手搖飲店名\U0001F379\n我知道的話會傳菜單給你喔!")                            
        line_bot_api.reply_message(event.reply_token, message)    
        
    elif '吃什麼' in msg:
        message = TextSendMessage(text = "火鍋或拉麵是不錯的選擇")                            
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '餓' in msg:
        message = TextSendMessage(text = "火鍋或拉麵是不錯的選擇")                            
        line_bot_api.reply_message(event.reply_token, message)    
    
    elif '吃東西' in msg:
        message = TextSendMessage(text = "火鍋或拉麵是不錯的選擇")                            
        line_bot_api.reply_message(event.reply_token, message)    
    
    
    #配合午餐吃了嗎的回應   
    elif '吃了' in msg:
        answer6 = random.randint(0, 1)
        message = [TextSendMessage(text = "ok，上課加油喔\U0001F60A"),
                   StickerSendMessage(package_id=8515, sticker_id=16581242)]                           
        line_bot_api.reply_message(event.reply_token, message[answer6])
    
    #配合午餐吃了嗎的回應    
    elif '還沒' in msg:
        message = TextSendMessage(text = "火鍋或拉麵是不錯的選擇")                            
        line_bot_api.reply_message(event.reply_token, message)
        
    elif '累' in msg:
        answer5 = random.randint(0, 2)
        message = [TextSendMessage(text ="辛苦了\U0001F497"),
                   StickerSendMessage(package_id=8525, sticker_id=16581300),
                   StickerSendMessage(package_id=6362, sticker_id=11087933)]
        line_bot_api.reply_message(event.reply_token, message[answer5])   
    
    elif '無聊' in msg:
        message = TextSendMessage(text = "可以看動漫阿，我有幾部可以推薦給你")
        line_bot_api.reply_message(event.reply_token, message)
    
    #沒有回答到關鍵字就回覆以下訊息
    else:
        message = TextSendMessage(text = "哈囉\U00002764~\n可以問我一些簡單的問題\U0001F440\n\U00002705 ex: 推薦的火鍋、拉麵、動漫、歌曲\n\U00002705 如果想喝飲料找不到菜單的話，也能輸入店名\n     我知道的話會傳菜單給你\n\U00002705 可以問我台北天氣如何\n\U00002705 早、午、晚安之類的話")
        line_bot_api.reply_message(event.reply_token, message)


@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
