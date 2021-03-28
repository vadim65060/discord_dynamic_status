import random
import time
import os
import requests
import json
import discord
from concurrent.futures import ThreadPoolExecutor
import sys
import codecs

config_path = 'config.json'
TOKEN = ""
STATUS_TIME = 3
dynamic_status_text = "тест"
dynamic_status_len = 12
dynamic_status_emoji = ""
change_time = 1
log_status = 'not set'
work_mode = 0
end_program = False
default_emoji = ""
default_status = ""
multi_status_text_list = []
multi_status_emoji_list = []

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

try:
    with codecs.open(config_path, 'r', 'UTF-8') as file:
        config = json.loads(file.read())
        STATUS_TIME = float(config['STATUS_TIME'])
        TOKEN = config['DISCORD_TOKEN']
        dynamic_status_text = config['dynamic_status_text']
        dynamic_status_len = config['dynamic_status_len']
        dynamic_status_emoji = config['dynamic_status_emoji']
        default_status = config["default_status"]
        default_emoji = config["default_emoji"]
        multi_status_text_list = config["multi_status_text_list"]
        multi_status_emoji_list = config["multi_status_emoji_list"]
        log_status = config['show current status']
        work_mode = config['work mode']
except Exception as exception:
    raise exception


def dynamic_status():
    status_len = dynamic_status_len
    status_text = dynamic_status_text + ' ' * status_len
    current_status = ' ' * status_len
    while 1:
        for i in status_text:
            if end_program:
                status_reset()
                return
            current_status = current_status[1:status_len]
            current_status += i
            print_status(current_status.replace(" ", "."), dynamic_status_emoji)
            time.sleep(STATUS_TIME)


def multi_status():
    statuslist = multi_status_text_list  # ["Я...", "1000-7", "ГУЛЬ!!!!!!!!"]
    emoji = multi_status_emoji_list  # ["🕵️", "🧠", "😈"]
    while 1:
        if end_program:
            status_reset()
            return
        for i in range(0, len(statuslist)):
            print_status(statuslist[i], emoji[i])
            time.sleep(STATUS_TIME)


def goul_status():
    global change_time, message
    first = True
    m = 1000
    while True:
        if end_program:
            status_reset()
            return
        if m <= -1:
            m = 1000
            first = True
        if first != True:
            m = m - 7
            change_time = STATUS_TIME
            message = m
        if m == 1000 or first == True:
            message = "Я гуль"
            first = False
            change_time = 3
        print_status(str(m + 7) + "-7=" + str(message))
        time.sleep(change_time)


def status_reset():
    print_status()


def print_status(status=default_status, emoji=default_emoji):
    status_data = json.dumps(
        {
            "custom_status":
                {
                    "text": status,
                    "emoji_name": emoji
                }
        }
    )
    r = requests.patch("https://discordapp.com/api/v8/users/@me/settings",
                       headers={"Authorization": TOKEN, "Content-Type": "application/json"}, data=status_data)
    if log_status == 'y':
        print(status)


while log_status != 'y' and log_status != 'n':
    log_status = input("show current status? y/n: ")
while work_mode < 1 or work_mode > 4:
    mod_list = ["1 - бегущая строка", "2 - замена нескольких строк", "3 - гуль", "4 - сброс"]
    for i in mod_list:
        print(i)
    work_mode = int(input())
pool = ThreadPoolExecutor(3)
if work_mode == 1:
    future = pool.submit(dynamic_status)
elif work_mode == 2:
    future = pool.submit(multi_status)
elif work_mode == 3:
    future = pool.submit(goul_status)
else:
    status_reset()
    sys.exit()
print("launched")
while 1:
    do_exit = input()
    if do_exit == 'end':
        status_reset()
        end_program = True
        sys.exit()
