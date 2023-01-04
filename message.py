#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import random

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
#隨機推薦歌手
def buttons_message():
    answer4 = random.randint(0, 5) # 亂數隨機推薦
    if answer4 == 0:
        message = [TextSendMessage(text = "我最近常聽她的歌，看你要不要聽聽看\U0001F447"), TemplateSendMessage(
            alt_text='推薦zutomayo給你～',
            template=ButtonsTemplate(
                thumbnail_image_url="https://www.moshimoshi-nippon.jp/wp/wp-content/uploads/2022/09/88a0c40e7e75e1cf1df3888c8fbdb5b3.jpeg",
                title="永遠是深夜有多好",
                text="ずっと真夜中でいいのに",
                actions=[
                    URITemplateAction( #導向連結的按鈕
                        label="聽聽看她的音樂\U0001F3B6",
                        uri="https://www.youtube.com/channel/UCcd-GOvl9DdyPVHQxy58bOw"
                    )
                ]
            )
        )]
        return message
    
    elif answer4 == 1:
        message = [TextSendMessage(text = "我最近常聽他的歌\U0001F447\n踊り子超級好聽"), TemplateSendMessage(
            alt_text='推薦Vaundy給你～',
            template=ButtonsTemplate(
                thumbnail_image_url="https://imgur.dcard.tw/HimlT3Oh.jpg",
                title="Vaundy",
                text="只有22歲的全能創作歌手",
                actions=[
                    URITemplateAction(
                        label="聽聽看他的音樂\U0001F3B6",
                        uri="https://www.youtube.com/channel/UC1FQWQ3y3-e8l1pCtWhJt5A"
                    )
                ]
            )
        )]
        return message
    
    elif answer4 == 2:
        message = [TextSendMessage(text = "我最近常聽她的歌，推推\U0001F447"), TemplateSendMessage(
            alt_text='推薦Aimer給你～',
            template=ButtonsTemplate(
                thumbnail_image_url="https://img.toy-people.com/member/16725015788.jpg",
                title="Aimer",
                text="推薦Ref:rain和kataomoi\n兩首都好聽",
                actions=[
                    URITemplateAction(
                        label="聽聽看她的音樂\U0001F3B6",
                        uri="https://www.youtube.com/channel/UCR1zT1s524Hbc85bdvno_8w"
                    )
                ]
            )
        )]
        return message
    
    elif answer4 == 3:
        message = [TextSendMessage(text = "我最近常聽她的歌，我同學也超愛\U0001F447"), TemplateSendMessage(
            alt_text='推薦愛繆給你～',
            template=ButtonsTemplate(
                thumbnail_image_url="https://www.moshimoshi-nippon.jp/wp/wp-content/uploads/2018/12/f26ee12f453e2e6d7a0e93776b143989.jpg",
                title="愛謬(あいみょん)",
                text="推薦マリーゴールド",
                actions=[
                    URITemplateAction(
                        label="聽聽看她的音樂\U0001F3B6",
                        uri="https://www.youtube.com/channel/UCQVhrypJhw1HxuRV4gX6hoQ"
                    )
                ]
            )
        )]
        return message
    
    elif answer4 == 4:
        message = [TextSendMessage(text = "我最近常聽的歌手\U0001F447"), TemplateSendMessage(
            alt_text='推薦ヨルシカ給你～',
            template=ButtonsTemplate(
                thumbnail_image_url = "https://upload.wikimedia.org/wikipedia/commons/2/27/Yorushika_Logo.jpg",
                title = "ヨルシカ(Yorushika)",
                text = "全部都好聽，聽就對了",
                actions=[
                    URITemplateAction(
                        label="聽聽看她的音樂\U0001F3B6",
                        uri="https://www.youtube.com/channel/UCRIgIJQWuBJ0Cv_VlU3USNA"
                    )
                ]
            )
        )]
        return message
    
    elif answer4 == 5:
        message = [TextSendMessage(text = "是我最近常聽的歌手\U0001F447"), TemplateSendMessage(
            alt_text='推薦King Gnu給你～',
            template=ButtonsTemplate(
                thumbnail_image_url = "https://memeon.sgp1.digitaloceanspaces.com/wp-content/uploads/2022/11/King-Gnu.jpeg",
                title = "King Gnu",
                text = "一途跟逆夢都好聽\n(絕對不是因為喜歡咒術迴戰?)",
                actions=[
                    URITemplateAction(
                        label = "聽聽看他們的音樂\U0001F3B6",
                        uri = "https://www.youtube.com/channel/UCkB8HnJSDSJ2hkLQFUc-YrQ"
                    )
                ]
            )
        )]
        return message
    
    

#旋轉木馬按鈕訊息介面:推薦火鍋    CarouselTemplate可以產生橫向Button訊息，一個template最多放10個column
def hotpot_Carousel():
    message = TemplateSendMessage(
        alt_text = '推薦的火鍋店家~',
        template = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url = 'https://broth-master.com/wp-content/uploads/2021/05/%E9%9B%9E%E6%B9%AF%E5%A4%A7%E5%8F%94-Logo2.png',
                    title = '雞湯大叔',
                    text = '推薦白蘭地雞湯頭',
                    actions=[
                        URITemplateAction(        #導向連結內容
                            label = '點此查看菜單及訂位',
                            uri = 'https://broth-master.com/'
                        ),
                        MessageTemplateAction(    #MessageTemplateAction 點擊回覆文字訊息
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(   #PostbackTemplateAction點擊後回傳至後台
                            label = '*******************',
                            data = '這是ID=1'
                        )    
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://www.godguo.com.tw/images/logo.png',
                    title = '尬鍋台式潮鍋',
                    text = '自助吧很讚',
                    actions=[
                        URITemplateAction(
                            label = '點此查看菜單及訂位',
                            uri = 'https://www.godguo.com.tw/'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=2'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://meatboss.com.tw/uploads/9ac95b53-ab75-4f2c-9c28-4d4e393c102a-logo.png',
                    title = '肉老大頂級肉品涮涮鍋',
                    text = '肉盤份量大，可以吃很飽',
                    actions=[
                        URITemplateAction(
                            label = '點此查看菜單及訂位',
                            uri = 'https://inline.app/booking/-LB4HBd5MTQ6s-1o-WGC?language=zh-tw'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=3'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://inline.imgix.net/branch/-Lax5xrWRFYPhSt66KBB:inline-live-2a466-null-d7158692-e440-40dc-8f5d-3b1c4559bec7_%E7%AF%89%E9%96%930.jpg',
                    title = '築間幸福鍋物',
                    text = '推推，好吃',
                    actions=[
                        URITemplateAction(
                            label = '點此查看菜單及訂位',
                            uri = 'https://www.jhujian.com.tw/'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=4'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://inline.imgix.net/branch/-L6kXHn5uYdWzFcWoxuo:inline-live-2a466--L6kXHn6WGofgBdzYVeU-108a9630-0bc7-4e51-aa2b-49bf7a0e7555_Pink%20and%20Red%20Beauty%20Influencer%20Asymmetrical%20Overlays%20Facebook%20Cover-2.png',
                    title = '好食多涮涮鍋',
                    text = '肉質不錯，好吃',
                    actions=[
                        URITemplateAction(
                            label = '點此查看菜單及訂位',
                            uri = 'https://inline.app/booking/-L6kXHn5uYdWzFcWoxuo:inline-live-2a466?language=zh-tw'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=5'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://www.wagyushabu.com.tw/img/logo.png',
                    title = '和牛涮日式鍋物放題',
                    text = '和牛壽司讚讚',
                    actions=[
                        URITemplateAction(
                            label = '點此查看菜單及訂位',
                            uri = 'https://www.wagyushabu.com.tw/'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=6'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://orangeshabushabu.com/site/images/og_img_s.png',
                    title = '橘色涮涮屋',
                    text = '服務很棒，但價位偏高',
                    actions=[
                        URITemplateAction(
                            label = '點此查看菜單及訂位',
                            uri = 'https://orangeshabushabu.com/zh-TW'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=7'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://wowfoods.wowprime.com/images/logo/123.png',
                    title = '青花驕',
                    text = '主打麻辣鍋，鴨血很好吃',
                    actions=[
                        URITemplateAction(
                            label = '點此查看菜單及訂位',
                            uri = 'https://www.chinhuajiao.com/'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=8'
                        )
                    ]
                )
            ]
        )
    )
    return message


#拉麵推薦，圖片在網頁版跑不出來，line 手機app可以
def ramen_Carousel():
    message = [TextSendMessage(text = "拉麵超人推薦給我的，你參考看看"), TemplateSendMessage(
        alt_text = '推薦的拉麵店家~',
        template = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url = 'https://imgur.dcard.tw/4oMFzivl.jpg',
                    title = '拉麵公子',
                    text = '鄰近地點：台北市中山區/中山女高、大潤發中崙店',
                    actions=[
                        URITemplateAction(
                            label = '點此查看官方FB',
                            uri = 'https://www.facebook.com/TheRamenBoy/'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=1'
                        )    
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://imgur.dcard.tw/XjccL9Gl.jpg',
                    title = '五之神製作所',
                    text = '鄰近地點：台北市信義區/ 北捷市政府站',
                    actions=[
                        URITemplateAction(
                            label = '點此查看官方FB',
                            uri = 'https://www.facebook.com/gonokamitw/'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=2'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://imgur.dcard.tw/OpbJfGxl.jpg',
                    title = '鬼金棒',
                    text = '鄰近地點：台北市中山區/中山市場',
                    actions=[
                        URITemplateAction(
                            label = '點此查看官方FB',
                            uri = 'https://www.facebook.com/kikanbotw/'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=3'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://imgur.dcard.tw/7EsJglWl.jpg',
                    title = '數寄屋 辻葉',
                    text = '鄰近地點：台北市大安區/ 師大夜市',
                    actions=[
                        URITemplateAction(
                            label = '點此查看官方FB',
                            uri = 'https://www.facebook.com/%E6%95%B8%E5%AF%84%E5%B1%8B-%E8%BE%BB%E8%91%89-%E3%82%86%E3%81%9A%E5%A1%A9%E9%B7%84%E7%99%BD%E6%B9%AF%E3%82%89%E3%83%BC%E3%82%81%E3%82%93%E5%B0%88%E9%96%80%E5%BA%97-103699351541666/?paipv=0&eav=AfbKLdohmgcwKzTw_o75TmAu0ucc0Szeoyk5jIelUmotKAaa9zZifgiFZnYYmfT_nxc&_rdr'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=4'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://imgur.dcard.tw/h46oviml.jpg',
                    title = '烹星',
                    text = '台北市中山區/勝王、23喜劇俱樂部',
                    actions=[
                        URITemplateAction(
                            label = '點此查看官方FB',
                            uri = 'https://www.facebook.com/katsuramenniboshi/'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=5'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://imgur.dcard.tw/cHYIWGcl.jpg',
                    title = '塩琉',
                    text = '鄰近地點：台北市中正區/ 228公園',
                    actions=[
                        URITemplateAction(
                            label = '點此查看官方FB',
                            uri = 'https://www.facebook.com/profile.php?id=100067648249112&paipv=0&eav=AfZa8F7hD39rzMhL8ufoFkvmWvu8yNdQziw7PWgzcuDqEdnkQDOXtu-zIARGBjeJ9XQ'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=6'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://imgur.dcard.tw/6BNjewzl.jpg',
                    title = '伊禾白湯',
                    text = '鄰近地點：台北市信義區/北捷世貿站\n一個餐期只有20碗，要提早去排隊喔',
                    actions=[
                        URITemplateAction(
                            label = '點此查看官方FB',
                            uri = 'https://www.facebook.com/people/%E4%BC%8A%E7%A6%BE%E7%99%BD%E6%B9%AF/100083276285760/'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=7'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://imgur.dcard.tw/B5zEfKbl.jpg',
                    title = '旨燕',
                    text = '鄰近地點：台北市中正區/ 中山堂',
                    actions=[
                        URITemplateAction(
                            label = '點此查看官方FB',
                            uri = 'https://www.facebook.com/Ramen.TSUBAME/'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=8'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://imgur.dcard.tw/POuEAXtl.jpg',
                    title = '崇灯拉麵',
                    text = '鄰近地點：台北市大安區/基隆路橋',
                    actions=[
                        URITemplateAction(
                            label = '點此查看官方FB',
                            uri = 'https://www.facebook.com/%E5%B4%87%E7%81%AF%E6%8B%89%E9%BA%B5-335912981043955/'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=9'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://imgur.dcard.tw/2cDot3tl.jpg',
                    title = '醇一拉麵',
                    text = '鄰近地點：台北市大安區/ 仁愛敦南圓環',
                    actions=[
                        URITemplateAction(
                            label = '點此查看官方IG',
                            uri = 'https://www.instagram.com/chun.ramenshop/?igshid=dsltaxgfncrc'
                        ),
                        MessageTemplateAction(
                            label = '都推薦給你了還不跟我說謝謝',
                            text = '謝謝'
                        ),
                        PostbackTemplateAction(
                            label = '*******************',
                            data = '這是ID=10'
                        )
                    ]
                )
            ]
        )
    )]
    return message




#(圖片旋轉木馬):推薦動畫   ImageCarouselTemplate只有圖片，但點擊label可以導到動畫瘋觀看
def animation_carousel():
    message = [TextSendMessage(text = "以下是我私心推薦的動畫名單\U00003299"), TemplateSendMessage(
        alt_text = '我的動畫推薦名單',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://p2.bahamut.com.tw/B/ACG/c/50/0000115950.JPG",
                    action=URITemplateAction(
                        label="孤獨搖滾",
                        uri="https://ani.gamer.com.tw/animeVideo.php?sn=31599"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://p2.bahamut.com.tw/B/ACG/c/72/0000098172.JPG",
                    action=URITemplateAction(
                        label="強風吹拂",
                        uri="https://ani.gamer.com.tw/animeVideo.php?sn=11446"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://p2.bahamut.com.tw/B/ACG/c/79/0000112279.JPG",
                    action=URITemplateAction(
                        label="前輩有夠煩",
                        uri="https://ani.gamer.com.tw/animeVideo.php?sn=25496"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://p2.bahamut.com.tw/B/ACG/c/37/0000110437.JPG",
                    action=URITemplateAction(
                        label="86－不存在的戰區",
                        uri="https://ani.gamer.com.tw/animeVideo.php?sn=22245"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://p2.bahamut.com.tw/B/ACG/c/50/0000092450.JPG",
                    action=URITemplateAction(
                        label="比宇宙更遠的地方",
                        uri="https://ani.gamer.com.tw/animeVideo.php?sn=16507"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://p2.bahamut.com.tw/B/ACG/c/78/0000102378.JPG",
                    action=URITemplateAction(
                        label="達爾文遊戲",
                        uri="https://ani.gamer.com.tw/animeVideo.php?sn=14445"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://p2.bahamut.com.tw/B/ACG/c/68/0000115368.JPG",
                    action=URITemplateAction(
                        label="奇巧計程車",
                        uri="https://ani.gamer.com.tw/animeVideo.php?sn=22238"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://p2.bahamut.com.tw/B/ACG/c/38/0000068438.JPG",
                    action=URITemplateAction(
                        label="四月是你的謊言",
                        uri="https://ani.gamer.com.tw/animeVideo.php?sn=22163"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://p2.bahamut.com.tw/B/ACG/c/67/0000080767.JPG",
                    action=URITemplateAction(
                        label="路人超能 100",
                        uri="https://ani.gamer.com.tw/animeVideo.php?sn=5863"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://p2.bahamut.com.tw/B/ACG/c/55/0000116555.JPG",
                    action=URITemplateAction(
                        label="明日同學的水手服",
                        uri="https://ani.gamer.com.tw/animeVideo.php?sn=27381"
                    )
                )
            ]
        )
    )]
    return message

