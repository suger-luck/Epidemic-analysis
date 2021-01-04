# coding=utf-8
import requests
import pandas as pd
from datetime import datetime


# 抓取腾讯疫情实时json数据
def catch_daily():
    url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,cityStatis,nowConfirmStatis,provinceCompare'
    
    # print(url)
    
    data = requests.get(url=url).json()["data"]["chinaDayList"]
    # print(data)
    
    data.sort(key=lambda x: x['date'])
    data.sort(key=lambda x:x['y'])
    
    date_list = list()  # 日期
    confirm_list = list()  # 确诊
    suspect_list = list()  # 疑似
    dead_list = list()  # 死亡
    heal_list = list()  # 治愈
    # print(data)
    for item in data:
        month, day = item['date'].split('.')
        year = item["y"]
        date_list.append(datetime.strptime('%s-%s-%s' % (year,month, day), '%Y-%m-%d'))
        confirm_list.append(int(item['confirm']))
        suspect_list.append(int(item['suspect']))
        dead_list.append(int(item['dead']))
        heal_list.append(int(item['heal']))
    
    return date_list, confirm_list, suspect_list, dead_list, heal_list


# 保存每日的数据
def save_data(date_list, confirm_list, suspect_list, dead_list, heal_list):
    data = pd.DataFrame({
        "data": date_list,
        "confirm": confirm_list,
        "suspect": suspect_list,
        "dead": dead_list,
        "heal": heal_list,
    })
    
    data.to_csv("./data/tencent/daily_data.csv", index=False, sep=",")


def main():
    """
    主逻辑实现
    :return:date_list, confirm_list, suspect_list, dead_list, heal_list
    """
    # 获取数据
    date_list, confirm_list, suspect_list, dead_list, heal_list = catch_daily()
    # 储存数据
    save_data(date_list, confirm_list, suspect_list, dead_list, heal_list)
    return date_list, confirm_list, suspect_list, dead_list, heal_list


if __name__ == '__main__':
    main()
