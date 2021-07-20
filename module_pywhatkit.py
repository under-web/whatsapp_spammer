import pywhatkit
import time
import re

# отправка на вотсап в определенное время cо сторонней библиотеки pywhatkit

# hour = int(time.ctime()[11:13])
# minut = int(time.ctime()[14:16])
# minut += 1
# print(hour, minut)

lists = []

with open('phone_from_topic.txt', 'r') as file:
    phones = file.readlines()
    for i in phones:
        clear_phone = re.sub(r'\+', '', i)
        result = '+7' + clear_phone[1:].strip()
        lists.append(result)

    set_phone = set(lists)
    for phone in set_phone:
        try:
            hour = int(time.ctime()[11:13])
            minut = int(time.ctime()[14:16])
            minut += 1
            print(phone)
            pywhatkit.sendwhatmsg(str(phone), "HI! How are you?", hour, minut)
        except Exception:
            continue



