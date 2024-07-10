# -*- coding:utf-8 -*-
# @FileName  :ultrasonic.py
# @Time      :2024/7/3 9:17
# @Author    :Ray
import os
from positec.show_data_pic import show_pic, get_log, get_ultra_data
from positec.ultra_source_data import get_ultra_source_log, show_pic_691, show_pic_6b1

# log文件和路径
mcu_name_list = [r'mcu.log.1', r'mcu.log']
planner_name_list = [r'planner.log.1', r'planner.log']


def planner_ultra_data(log_path, start_time, end_time, start_sed=0, end_sed=0):
    planner_lines = []
    for name in planner_name_list:
        file_path = os.path.join(log_path, name)
        with open(file_path, 'r', encoding='utf-8') as f_b:
            planner_lines.extend(f_b.readlines())

    # 获取时段内planner log
    all_log = get_log(planner_lines, start_time, end_time)
    ultra_log = get_ultra_data(all_log, start_sed, end_sed)
    show_pic(ultra_log)
    print(len(all_log))


def mcu_ultra_source(log_path, start_time, end_time, start_sed=0, end_sed=0):
    mcu_lines = []
    for name in mcu_name_list:
        file_path = os.path.join(log_path, name)
        with open(file_path, 'r', encoding='utf-8') as f_b:
            mcu_lines.extend(f_b.readlines())

    # 获取时段内planner log
    all_log = get_log(mcu_lines, start_time, end_time)
    ultra_source_log = get_ultra_source_log(all_log, start_sed, end_sed)
    show_pic_691(ultra_source_log[0])
    show_pic_6b1(ultra_source_log[1])






