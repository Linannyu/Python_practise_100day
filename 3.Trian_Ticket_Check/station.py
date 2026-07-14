import requests
import re
import json

url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js"

text = requests.get(url, verify=False).text

stations = dict(re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', text))

with open("3.Trian_Ticket_Check/stations.json", "w", encoding="utf-8") as f:
    json.dump(stations, f, ensure_ascii=False, indent=4)

print("共", len(stations), "个车站")
