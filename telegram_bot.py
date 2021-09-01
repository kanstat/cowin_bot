# getupdated function, send msgs,grab user text,get chat id,return text.
import requests


api_key = "Replace this with your api key"
base_url = f"https://api.telegram.org/bot{api_key}/"


def get_updates(offset=None):
    full_url = f"{base_url}getUpdates?offset={offset}&timeout=5"
    r = requests.get(full_url)
    received_data = r.json()
    return received_data


def get_chat_id():
    receive_id_data = get_updates()
    userId = receive_id_data["result"][-1]["message"]["chat"]["id"]
    return userId


def send_msgs(chat_id, msg):
    full_url = f"{base_url}sendMessage?chat_id={chat_id}&text={msg}"
    r = requests.get(full_url)
    rec_data = r.json()
    return rec_data


def grab_user_text():
    receivedData = get_updates()
    userText = receivedData["result"][-1]["message"]["text"]
    return userText


# Id = None
# while(True):

#     print(Id)
#     update_newdata = get_updates(offset=Id)
#     update_newdata = update_newdata["result"]
#     if update_newdata:
#         for i in update_newdata:
#             Id = i["update_id"]
#             print(Id, "loop wala")
#             try:
#                 User_text = i["message"]["text"]
#             except:
#                 User_text = None
#             chatId = i["message"]["chat"]["id"]
#             send_msgs(chatId, "arey pagal hai ye bot")
#         Id = Id+1
ID = None
while(True):
    total_result = get_updates(offset=ID)
    total_result = total_result['result']
    if total_result:
        for item in total_result:
            item_updateid = item['update_id']
            item_chatid = item['message']['chat']['id']
            item_usertext = item['message']['text']
            ID = item_updateid
            print(item_updateid)
            print(item_chatid)
            print(item_usertext)
            print(f'loop{ID}')
        ID = ID+1
        print(f'id={ID}\n')
