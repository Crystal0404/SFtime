from pycqBot import cqBot, cqHttpApi
from pycqBot.object import Plugin
from pycqBot.data import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import math
from time import sleep


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
            name = self.group_dict[group_id]['name']
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
            for i in str(time):
                try:
                    i = str(int(i))
                    time_add += i
                except:
                    if time_add != '':
                        time_list.append(int(time_add))
                    time_add = ''
            time_now = datetime.now().timestamp()
            time_book = datetime(time_list[0], time_list[1], time_list[2],
                                 time_list[3], time_list[4], time_list[5]).timestamp()
            time = math.floor(time_now - time_book)
            d = math.floor(time / 86400)
            h = math.floor((time - (86400 * d)) / 3600)
            min = math.floor((time - (86400 * d) - (3600 * h)) / 60)
            s = time - (d * 86400) - (h * 3600) - (min * 60)
            dict = {'天': d, '小时': h, '分钟': min, '秒': s}
            text = ''
            for i in dict:
                if dict[i] != 0:
                    text += (str(dict[i]) + i)
            send_text = '距离{0}上次更新已经过去了{1}'.format(name, text)
            self.cqapi.send_group_msg(group_id, send_text)
            sleep(1)
            send_text = '上次更新时间为{0}'.format(str(soup.select('.text-row .text')[3])[22:-7])
            self.cqapi.send_group_msg(group_id, send_text)
            sleep(1)
            if d > 0:
                send_text = '{0},你已经超过24小时没更新了,生产队的驴都不敢这么歇'.format(name)
                self.cqapi.send_group_msg(group_id, send_text)
