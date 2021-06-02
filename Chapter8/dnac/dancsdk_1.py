#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from dnacentersdk import api
import datetime
import time
from dnac.dnac_login_info import username, password, base_url

# Create a DNACenterAPI connection object;
# it uses DNA Center sandbox URL, username and password
DNAC = api.DNACenterAPI(username=username,
                        password=password,
                        base_url=base_url)

# Find all devices
DEVICES = DNAC.devices.get_device_list()

# Print select information about the retrieved devices
print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format("Device Name", "|", "Device Type", "|", "Up Time"))

print('-'*95)

for DEVICE in DEVICES.response:
    try:
        print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format(DEVICE.hostname, "|", DEVICE.type, "|", DEVICE.upTime))
    except TypeError:
        pass

print('-'*95)

# 时间戳到datetime对象
timestamp = 1566506489000
dt_object = datetime.datetime.utcfromtimestamp(timestamp/1000)
print(dt_object)

# 时间对象到时间戳
dt_now = datetime.datetime.now()
dt_1_hour_before = dt_now - datetime.timedelta(hours=1)
timestamp_1_hour_before = time.mktime(dt_1_hour_before.timetuple())
print(timestamp_1_hour_before)

# 转换到milliseconds
timestamp_1_hour_before_milliseconds = str(int(timestamp_1_hour_before) * 1000)

# Get the health of all clients
CLIENTS = DNAC.clients.get_overall_client_health(timestamp=timestamp_1_hour_before_milliseconds)

# Print select information about the retrieved client health statistics
print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format("Client Category", "|", "Number of Clients", "|", "Clients Score"))

print('-'*95)

for CLIENT in CLIENTS.response:
    for score in CLIENT.scoreDetail:
        print('{0:25s}{1:1}{2:<45d}{3:1}{4:<15d}'.format(score.scoreCategory.value, "|", score.clientCount, "|", score.scoreValue))
print('-'*95)

