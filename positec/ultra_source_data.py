# -*- coding:utf-8 -*-
# @FileName  :ultra_source_data.py
# @Time      :2024/7/8 9:49
# @Author    :Ray
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from show_data_pic import replace_char, ultra_sensor_list

# 指定字体路径和大小
font = FontProperties(fname=r'D:\pycharmProject\pythonProject\font\simsun.ttc', size=14)


# 从时间段内的数据获取原始数据
def get_ultra_source_log(data_list, start_sed=0, end_sed=0):
    sum_691 = 0
    sum_6b1 = 0
    sum_sub_691 = 0
    sum_sub_6b1 = 0
    source_691 = []
    source_6b1 = []
    source_list_691 = []
    source_list_6b1 = []
    for data in data_list:
        if len(data.split(';')) > 1:
            if 'Ultrasonic' in data and '0x691' in data:
                source_691.append(data)
            elif 'Ultrasonic' in data and '0x6B1' in data:
                source_6b1.append(data)
        else:
            continue

    if end_sed == 0:
        end_sed = len(source_691)

    for ultra in source_691:
        # 解析超声数据
        line_list = []
        for x in replace_char(ultra.split(';')[1]).split(','):
            if x.isdigit():
                line_list.append(int(x))
            else:
                break
        if end_sed > sum_691 > start_sed and len(line_list) == 7:
            source_list_691.append(line_list)
            sum_sub_691 += 1
            print(sum_sub_691, ultra)
        sum_691 += 1

    for ultra in source_6b1:
        # 解析超声数据
        line_list = []
        for x in replace_char(ultra.split(';')[1]).split(','):
            if x.isdigit():
                line_list.append(int(x))
            else:
                break
        # line_list = [int(x) for x in replace_char(ultra.split(';')[1]).split(',')]
        if end_sed > sum_6b1 > start_sed and len(line_list) == 6:
            source_list_6b1.append(line_list)
            sum_sub_6b1 += 1
            print(sum_sub_6b1, ultra)
        sum_6b1 += 1
    ultra_691 = [[250 if arr[i] == 0 else arr[i] * 2 for arr in source_list_691] for i in range(7)]
    # ultra_691 = []
    # for i in range(7):
    #     temp_arr = []
    #     for arr in source_list_691:
    #         if arr[i] == 0:
    #             arr[i] = 250
    #         else:
    #             arr[i] *= 2
    #         temp_arr.append(arr[i])
    #     ultra_691.append(temp_arr)
    ultra_6b1 = [[250 if arr[i] == 0 else arr[i] * 2 for arr in source_list_6b1] for i in range(6)]
    return ultra_691, ultra_6b1


def show_pic_691(data_list):
    x = list(range(len(data_list[0])))
    for index, new_list in enumerate(data_list):
        plt.figure(index)
        plt.plot(x, new_list)
        plt.title(ultra_sensor_list[index] + "超声波", fontproperties=font)


def show_pic_6b1(data_list):
    x = list(range(len(data_list[0])))
    for index, new_list in enumerate(data_list):
        plt.figure(index+7)
        plt.plot(x, new_list)
        plt.title(ultra_sensor_list[index+7] + "超声波", fontproperties=font)

