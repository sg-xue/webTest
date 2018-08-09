#!/usr/bin/env python
# coding=utf8


class ShortMsg:
    def __init__(self, num, operator, province, tel, content, receive_time):
        self.id = num
        self.operator = operator
        self.province = province
        self.tel = tel
        self.content = content
        self.receive_time = receive_time
