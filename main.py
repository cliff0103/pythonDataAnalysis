# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2024/7/9 10:20
# @Author    :Ray
from matplotlib import pyplot as plt
from positec.ultrasonic import mcu_ultra_source, planner_ultra_data

# log文件和路径
file_path73 = r'E:\log\ulsonic\kr800_2024-7-3_16_9_19'
file_path74 = r'E:\log\ulsonic\kr800_2024-7-4_16_4_9'
file_path75 = r'E:\log\ulsonic\kr800_2024-7-5_15_55_46'
file_path78 = r'E:\log\ulsonic\kr800_2024-7-8_14_37_46'
# 动态测试时间
# start_time = r'2024-07-05 14:22'
# end_time = r'2024-07-05 14:24'
# 静态测试时间
start_time = r'2024-07-07 01:22'
end_time = r'2024-07-07 01:24'
log_path = file_path78

# planner_ultra_data(log_path, start_time, end_time)
mcu_ultra_source(log_path, start_time, end_time)
plt.show()