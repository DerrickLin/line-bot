#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import requests
import json

#利用中央氣象局提供的天氣API抓取資料
def taipei_weather():
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-3E629277-2A65-4E90-8265-DE5CC5E9C14D&locationName=%E8%87%BA%E5%8C%97%E5%B8%82"
    
    list_req = requests.get(url)
    gettext = list_req.content  #把內容抓出來
    data = json.loads(gettext)  #轉成json格式

    # 0點到6點的氣象資料  #一層一層的把資料抓出來
    city1 = data["records"]["location"][0]["locationName"]

    time1 = data["records"]["location"][0]["weatherElement"][0]["time"][0]["startTime"][5:16] + " ~ " + data["records"]["location"][0]["weatherElement"][0]["time"][0]["endTime"][5:16]

    condition1 = "天氣狀況: " + data["records"]["location"][0]["weatherElement"][0]["time"][0]["parameter"]["parameterName"]

    temp1 ="溫度: " + data["records"]["location"][0]["weatherElement"][2]["time"][0]["parameter"]["parameterName"] + "°C ~ " + data["records"]["location"][0]["weatherElement"][4]["time"][0]["parameter"]["parameterName"] + "°C"

    rate1 = "降雨機率: " + data["records"]["location"][0]["weatherElement"][1]["time"][0]["parameter"]["parameterName"] + "%"

    status1 = city1 + "\n" + time1 + "\n" + condition1 + "\n" + temp1 + "\n" + rate1


    #6點到18點的氣象資料
    time2 = data["records"]["location"][0]["weatherElement"][0]["time"][1]["startTime"][5:16] + " ~ " + data["records"]["location"][0]["weatherElement"][0]["time"][1]["endTime"][5:16]

    condition2 = "天氣狀況: " + data["records"]["location"][0]["weatherElement"][0]["time"][1]["parameter"]["parameterName"]

    temp2 ="溫度: " + data["records"]["location"][0]["weatherElement"][2]["time"][1]["parameter"]["parameterName"] + "°C ~ " + data["records"]["location"][0]["weatherElement"][4]["time"][1]["parameter"]["parameterName"] + "°C"

    rate2 = "降雨機率: " + data["records"]["location"][0]["weatherElement"][1]["time"][1]["parameter"]["parameterName"] + "%"

    status2 = time2 + "\n" + condition2 + "\n" + temp2 + "\n" + rate2


    #18點到隔天6點的氣象資料
    time3 = data["records"]["location"][0]["weatherElement"][0]["time"][2]["startTime"][5:16] + " ~ " + data["records"]["location"][0]["weatherElement"][0]["time"][2]["endTime"][5:16]

    condition3 = "天氣狀況: " + data["records"]["location"][0]["weatherElement"][0]["time"][2]["parameter"]["parameterName"]

    temp3 ="溫度: " + data["records"]["location"][0]["weatherElement"][2]["time"][2]["parameter"]["parameterName"] + "°C ~ " + data["records"]["location"][0]["weatherElement"][4]["time"][2]["parameter"]["parameterName"] + "°C"

    rate3 = "降雨機率: " + data["records"]["location"][0]["weatherElement"][1]["time"][2]["parameter"]["parameterName"] + "%"

    status3 = time3 + "\n" + condition3 + "\n" + temp3 + "\n" + rate3

    overall = status1 + "\n\n" + status2 + "\n\n" + status3  # 將三個時段的資料串成一則訊息後回傳
    print(overall)
    return overall
   


