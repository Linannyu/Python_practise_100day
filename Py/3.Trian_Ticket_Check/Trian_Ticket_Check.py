import requests
import prettytable as pt # prettytable是一个用来打印表格的库
import json

# 读取json文件
f = open('3.Trian_Ticket_Check/stations.json', encoding='utf-8')
json_data = json.loads(f.read())

# 用户输入出发城市，到达城市，出发日期
from_city = input('请输入出发城市：')
to_city = input('请输入到达城市：')
date = input('请输入出发日期：')


# 发送请求的链接
url = f'https://kyfw.12306.cn/otn/leftTicket/queryG?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={json_data[from_city]}&leftTicketDTO.to_station={json_data[to_city]}&purpose_codes=ADULT'

# User伪装
header = {
    'Cookie': '_uab_collina=178403415099631546313352; JSESSIONID=3B011AEC02C6B04E83C38BE6EF903BEC; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=1373176074.64545.0000; _jc_save_fromDate=2026-07-14; _jc_save_toDate=2026-07-14; _jc_save_wfdc_flag=dc; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; BIGipServerportal=3067347210.17183.0000; _jc_save_fromStation=%u5929%u6D25%2CTJP; _jc_save_toStation=%u5317%u4EAC%2CBJP',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'
}
# 发送请求给12306
res = requests.get(url, headers=header)
res.encoding = 'utf-8'

# 做一个好看的table
tb = pt.PrettyTable()
tb.field_names = ['序号','车次', '出发时间', '到达时间', '耗时', '特等座', '一等座', '二等座', '硬卧', '硬座', '无座', '软卧']
page = 0

# 获取车次信息
for i in res.json()['data']['result']:
    # 用｜分割数据
    index = i.split('|')

    '''
    # 方便查看index
    a = 0
    for j in index:
        print(j , a ,sep = '--')
        a += 1
    break
    '''

    num = index[3] #车次
    start_time = index[8] # 出发时间
    end_time = index[9] # 到达时间
    use_time = index[10] # 耗时
    topGrade = index[32] # 特等座
    first_class = index[31]#一等座
    second_class = index[30] # 二等做
    hard_sleeper = index[28] # 硬卧
    hard_seat = index[29] #硬座
    no_seat = index[26] # 无座
    soft_sleeper = index[23] # 软卧

    # 显示对应的数据（没什么用可以删除）
    dit = {
        '车次': num,
        '出发时间': start_time,
        '到达时间': end_time,
        '耗时': use_time,
        '特等座': topGrade,
        '一等座': first_class,
        '二等座': second_class,
        '硬卧': hard_sleeper,
        '硬座': hard_seat,
        '无座': no_seat,
        '软卧': soft_sleeper
    }
    tb.add_row([page, num, start_time, end_time, use_time, topGrade, first_class, second_class, hard_sleeper, hard_seat, no_seat, soft_sleeper])
    page += 1

print(tb)