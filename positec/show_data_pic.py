# -*- coding:utf-8 -*-
# @FileName  :show_data_pic.py
# @Time      :2024/7/5 11:02
# @Author    :Ray
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from lib.re_positec import get_time

# 指定字体路径和大小
font = FontProperties(fname=r'D:\pycharmProject\pythonProject\font\simsun.ttc', size=14)


ultra_sensor = {
    "0": "后右",
    "1": "后中",
    "2": "后右",
    "3": "前左",
    "4": "前左中",
    "5": "前右中",
    "6": "前右",
    "7": "右侧前",
    "8": "右侧中",
    "9": "右侧后",
    "10": "左侧后",
    "11": "左侧中",
    "12": "左侧前"
}
<<<<<<< HEAD
ultra_sensor_list = ["691后右", "691后中", "691后左", "691前左", "691前左中", "691前右中", "691前右",
                     "6B1右侧前", "6B1右侧中", "6B1右侧后", "6B1左侧后", "6B1左侧中", "6B1左侧前"]
=======
ultra_sensor_list = ["后右", "后中", "后左", "前左", "前左中", "前右中", "前右",
                     "右侧前", "右侧中", "右侧后", "左侧后", "左侧中", "左侧前"]
>>>>>>> 32f8a0f1b3b34bd66b060d382ec71f3e49c711bf


# 替换不必要的字符
def replace_char(str_temp):
    replacements = {
        "[": "",
        "]": "",
        " ": "",
        "\n": ""
    }
    for src, target in replacements.items():
        str_temp = str_temp.replace(src, target)
    return str_temp


# 获取时间段内的数据
def get_log(lines, start_time, end_time):
    data_log = []
    for line in lines:
        time_line = get_time(line)
        if time_line:
            if start_time and end_time and time_line:
                if end_time > time_line[:len(start_time)] > start_time:
                    data_log.append(line)
            elif start_time and (not end_time):
                if time_line > start_time:
                    data_log.append(line)
            else:
                print("请输入需要log的起止时间或日期")
    return data_log


# 超声数据
def get_ultra_data(data_list, start_sed=0, end_sed=0):
    sum = 0
    sum_sub = 0
    ultra_data = []
    ultra_list = []
    for data in data_list:
        if 'ultrasonic[13]' in data:
            ultra_data.append(data)

    if end_sed == 0:
        end_sed = len(ultra_data)

    for ultra in ultra_data:
        # 解析超声数据
        line_list = [int(x) for x in replace_char(ultra.split('=')[1]).split(',')]
        if end_sed > sum > start_sed:
            ultra_list.append(line_list)
            sum_sub += 1
            print(sum_sub, ultra)
        sum += 1
    return [[arr[i] for arr in ultra_list] for i in range(13)]


def show_pic(data_list):
    x = list(range(len(data_list[0])))
    for index, new_list in enumerate(data_list):
        plt.figure(index)
        plt.plot(x, new_list)
<<<<<<< HEAD
        plt.xlabel("Time(50ms)")
        plt.ylabel("Distance(cm)")
=======
>>>>>>> 32f8a0f1b3b34bd66b060d382ec71f3e49c711bf
        plt.title(ultra_sensor_list[index] + "超声波", fontproperties=font)
