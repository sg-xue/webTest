#!/usr/bin/env python
# coding=utf8

import requests
import time
from shortMsg import ShortMsg


def getMsg(search_tel):
    url = "http://apis-mgmt-test.dianhua.cn/smsCollect/"
    apikey = "yuloreeiauXtRkjH88RHit5kpvwK12np"
    country = 86
    uid = "qatest"
    ver = "1.0"
    app = "sms"
    v = "1"
    to = search_tel #"18007305146 15903551769"
    arguments = {"apikey":apikey, "country":country, "uid":uid, "ver":ver, "app":app, "v":v, "to":to}
    try:
        rep = requests.get(url=url, params=arguments)
        if rep.status_code == 200 and rep.content.find("msg"):
            # print rep.text
            sms_num = len(rep.json()["data"])
            print "%s messages in total." % sms_num
            if sms_num > 0:
                msg_list = []
                for i in range(sms_num):
                    operator = rep.json()["data"][i]["carr_name"]
                    province = rep.json()["data"][i]["province"] + rep.json()["data"][i]["city"]
                    tel = rep.json()["data"][i]["tel"]
                    content = rep.json()["data"][i]["msg"]
                    receive_time = rep.json()["data"][i]["time"]
                    short_msg = ShortMsg(i, operator, province, tel, content, receive_time)
                    msg_list.append(short_msg)
                    # print "the objent is :", short_msg.__dict__
                return msg_list
            else:
                return -1
        else:
            return "no message find"
    except requests.exceptions.ConnectionError:
        print('ConnectionError -- please wait 3 seconds')
        time.sleep(3)
    except requests.exceptions.Timeout:
        print('TimeoutError -- please wait 3 seconds')
        time.sleep(3)
    except requests.exceptions.HTTPError:
        print('HTTPError -- please wait 3 seconds')
        time.sleep(3)
    except:
        print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
        time.sleep(3)


if __name__ == '__main__':
    getMsg()
