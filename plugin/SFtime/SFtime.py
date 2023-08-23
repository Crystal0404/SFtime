from pycqBot import cqBot, cqHttpApi
from pycqBot.object import Plugin
from pycqBot.data import *
import requests
from bs4 import BeautifulSoup
import time as t


class SFtime(Plugin):
    def __init__(self, bot: cqBot, cqapi: cqHttpApi, plugin_config):
        super().__init__(bot, cqapi, plugin_config)
        self.group_dict = plugin_config
        bot.command(self.time, 'time', {
            'type': 'all'
        })

    def time(self, cdata, message: Message):
        group_id = message.event.data['group_id']
        if group_id in self.plugin_config:
            url = self.group_dict[group_id]['url']
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'
            }
            wd = requests.get(url, headers=header)
            wd.encoding = 'utf-8'
            text = wd.text
            soup = BeautifulSoup(text, 'lxml')
            time = soup.select('.text-row .text')[3]
            time_add = ''
            time_list = []
            for i in time:
                try:
                    i = str(int(i))
                    time_add += i
                except:
                    if time_add != '':
                        time_list.append(int(time_add))
                    time_add = ''






# if __name__ == '__main__':
#     url = 'https://book.sfacg.com/Novel/619932'
#     header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'
#     }
#     wd = requests.get(url, headers=header)
#     wd.encoding = 'utf-8'
#     text = wd.text
#     soup = BeautifulSoup(text, 'lxml')
#     time = soup.select('.text-row .text')[3]
#     time_add = ''
#     time_list = []
#     for i in str(time):
#         try:
#             i = str(int(i))
#             time_add += i
#         except:
#             if time_add != '':
#                 time_list.append(int(time_add))
#             time_add = ''
#     print(time_list)
