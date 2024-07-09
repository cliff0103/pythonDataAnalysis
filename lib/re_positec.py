# -*- coding:utf-8 -*-
# @FileName  :re_positec.py
# @Time      :2024/7/5 10:59
# @Author    :Ray
import re
import re


def get_time(str_temp):
    # 编译一个正则表达式模式，用于匹配日期时间格式 YYYY-MM-DD HH:MM:SS,SSS
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})')

    # 在字符串中查找匹配项
    if str_temp:
        match = pattern.search(str_temp)
        if match:
            # 如果找到匹配项，打印出来
            return match.group(0)
        else:
            # 如果没有找到匹配项，打印一条消息
            return False