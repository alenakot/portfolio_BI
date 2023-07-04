from telethon.sync import TelegramClient   #класс, позволяющий нам подключаться к клиенту мессенджера и работать с ним
import csv
import pandas as pd

from telethon.tl.functions.messages import GetHistoryRequest #метод, позволяющий получить сообщения пользователей из чата и работать с ним
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

def vac_find(text:str, word_serch:list):  # функция для определения вакансия это или нет, и для какого спец-та
    listOfChecks = ["vacancy", "вакансия", "позиция", "ищем"]
    for word_1 in listOfChecks:
        if word_1 in str(text).lower():
            for word in word_serch:
                if str(text).lower().find(word) != -1:
                    return True
    return False

api_id = 21723859
api_hash = '5862483c3bcb6c74e17c2d6a85a7769e'
phone = '79046012412'

client = TelegramClient(phone, api_id, api_hash)
client.start()
client.start()


last_date = None

target_group = 'https://t.me/analysts_hunter'
offset = 0
limit = 10000000
all_users = []

while True:
    result = client(GetParticipantsRequest(
        channel=target_group,
        filter=ChannelParticipantsSearch(''),
        offset=offset,
        limit=limit,
        hash=0
    ))
    users = result.users
    all_users.extend(users)
    if len(users) < limit:
        break
    offset += limit

all_participants = []
all_participants = client.get_participants(target_group)
print("Сохраняем данные в файл...")
with open("members.csv", "w", encoding="UTF-8") as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(["username", "name", "group"])
    for user in all_participants:
        if user.username:
            username = user.username
        else:
            username = ""
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ""
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ""
        name = (first_name + ' ' + last_name).strip()
        writer.writerow([username, name, target_group.title])
print("Парсинг участников группы успешно выполнен.")

offset_id = 0
limit = 1000000
all_messages = []
total_messages = 10000000
total_count_limit = 10000000

print("Начинаем парсинг сообщений...")
for i in range(0,99):
    while True:
        history = client(GetHistoryRequest(
            peer=target_group,
            offset_id=offset_id,
            offset_date=None,
            add_offset= (i+1) * 100,
            limit=10000000,
            max_id=0,
            min_id=0,
            hash=0
        ))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            all_messages.append([message.sender_id, message.message, message.date, message.reply_to_msg_id])
        offset_id = messages[len(messages) - 1].id
        df_message = pd.DataFrame(all_messages, columns=['user_id', 'text', 'date', 'reply'])
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break
    i = i + 1

df_message['length'] = df_message['text'].str.len() #определяем длину сообщения
df_message['jun'] = df_message['text'].apply(lambda x: vac_find(x,["junior", "джуниор"]))
df_message['mid'] = df_message['text'].apply(lambda x: vac_find(x,["middle", "мидл"]))
df_message['sen'] = df_message['text'].apply(lambda x: vac_find(x,["senior", "синьор"]))
df_message['lead'] = df_message['text'].apply(lambda x: vac_find(x,["lead", "лид", "ведущий"]))
print("Сохраняем данные в файл...")
df_message.to_csv('message.csv')
print('Парсинг сообщений группы успешно выполнен.')



