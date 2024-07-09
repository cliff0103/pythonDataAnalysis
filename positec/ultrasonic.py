# -*- coding:utf-8 -*-
# @FileName  :ultrasonic.py
# @Time      :2024/7/3 9:17
# @Author    :Ray
import os
<<<<<<< HEAD
from positec.show_data_pic import show_pic, get_log, get_ultra_data
from positec.ultra_source_data import get_ultra_source_log, show_pic_691, show_pic_6b1

mcu_name_list = [r'mcu.log.1', r'mcu.log']
planner_name_list = [r'planner.log.1', r'planner.log']


def planner_ultra_data(log_path, start_time, end_time, start_sed=0, end_sed=0):
=======
from matplotlib import pyplot as plt
from show_data_pic import show_pic, get_log, get_ultra_data
from ultra_source_data import get_ultra_source_log, show_pic_691, show_pic_6b1

# log文件和路径
mcu_name_list = [r'mcu.log.1', r'mcu.log']
planner_name_list = [r'planner.log.1', r'planner.log']
file_path73 = r'E:\log\ulsonic\kr800_2024-7-3_16_9_19'
file_path74 = r'E:\log\ulsonic\kr800_2024-7-4_16_4_9'
file_path75 = r'E:\log\ulsonic\kr800_2024-7-5_15_55_46'
file_path78 = r'E:\log\ulsonic\kr800_2024-7-8_14_37_46'


def planner_ultra_data(start_sed=0, end_sed=0):
>>>>>>> 32f8a0f1b3b34bd66b060d382ec71f3e49c711bf
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


<<<<<<< HEAD
def mcu_ultra_source(log_path, start_time, end_time, start_sed=0, end_sed=0):
=======
def mcu_ultra_source(start_sed=0, end_sed=0):
>>>>>>> 32f8a0f1b3b34bd66b060d382ec71f3e49c711bf
    mcu_lines = []
    for name in mcu_name_list:
        file_path = os.path.join(log_path, name)
        with open(file_path, 'r', encoding='utf-8') as f_b:
            mcu_lines.extend(f_b.readlines())

<<<<<<< HEAD
    # 获取时段内mcu log
    all_log = get_log(mcu_lines, start_time, end_time)
    ultra_source_log = get_ultra_source_log(all_log, start_sed, end_sed)

=======
    # 获取时段内planner log
    all_log = get_log(mcu_lines, start_time, end_time)
    print(len(all_log))
    # print(all_log)
    ultra_source_log = get_ultra_source_log(all_log, start_sed, end_sed)
    print(len(ultra_source_log[0]))
    # print(ultra_source_log[0])
>>>>>>> 32f8a0f1b3b34bd66b060d382ec71f3e49c711bf
    show_pic_691(ultra_source_log[0])
    show_pic_6b1(ultra_source_log[1])


<<<<<<< HEAD

=======
# 测试时间
start_time = r'2024-07-07 22:22'
end_time = r'2024-07-08 14:24'
log_path = file_path78

# planner_ultra_data()
mcu_ultra_source(start_sed=8200, end_sed=8400)
plt.show()
>>>>>>> 32f8a0f1b3b34bd66b060d382ec71f3e49c711bf




