# -*- coding: utf-8 -*-
import time, json, requests


def get_data():
    # 抓取腾讯疫情实时json数据
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' % int(time.time() * 1000)
    return json.loads(requests.get(url=url).json()['data'])


def handle_data(num):
    """
    数据的预处理
    :param num:
    :return:total_data,total_dead_data,total_new_data,total_suspect_data, total_heal_data
    """
    # 解析确诊数据
    total_data = {}
    for item in num:
        if item['name'] not in total_data:
            total_data.update({item['name']: 0})
        for city_data in item['children']:
            total_data[item['name']] += int(city_data['total']['confirm'])
    # print(total_data)
    # {'湖北': 48206, '广东': 1241, '河南': 1169, '浙江': 1145, '湖南': 968, ...,  '澳门': 10, '西藏': 1}
    
    # 解析疑似数据
    total_suspect_data = {}
    for item in num:
        if item['name'] not in total_suspect_data:
            total_suspect_data.update({item['name']: 0})
        for city_data in item['children']:
            total_suspect_data[item['name']] += int(city_data['total']['suspect'])
    # print(total_suspect_data)
    
    # 解析死亡数据
    total_dead_data = {}
    for item in num:
        if item['name'] not in total_dead_data:
            total_dead_data.update({item['name']: 0})
        for city_data in item['children']:
            total_dead_data[item['name']] += int(city_data['total']['dead'])
    # print(total_dead_data)
    
    # 解析治愈数据
    total_heal_data = {}
    for item in num:
        if item['name'] not in total_heal_data:
            total_heal_data.update({item['name']: 0})
        for city_data in item['children']:
            total_heal_data[item['name']] += int(city_data['total']['heal'])
    # print(total_heal_data)
    
    # 解析新增确诊数据
    total_new_data = {}
    for item in num:
        if item['name'] not in total_new_data:
            total_new_data.update({item['name']: 0})
        for city_data in item['children']:
            total_new_data[item['name']] += int(city_data['today']['confirm'])  # today
    # print(total_new_data)
    return total_data, total_dead_data, total_new_data, total_suspect_data, total_heal_data


def save_data(total_data, total_dead_data, total_new_data, total_suspect_data, total_heal_data):
    """
    保存数据
    :param total_data:
    :param total_dead_data:
    :param total_new_data:
    :param total_suspect_data:
    :param total_heal_data:
    :return: None
    """
    names = list(total_data.keys())  # 省份名称
    num1 = list(total_data.values())  # 确诊数据
    num2 = list(total_suspect_data.values())  # 疑似数据(全为0)
    num3 = list(total_dead_data.values())  # 死亡数据
    num4 = list(total_heal_data.values())  # 治愈数据
    num5 = list(total_new_data.values())  # 新增确诊病例
    
    # 获取当前日期命名(2020-11-25-all.csv)
    n = "./data/tencent/" + time.strftime("%Y-%m-%d") + "-all-4db.csv"
    fw = open(n, 'w', encoding='utf-8')
    fw.write('province,tpye,data\n')
    i = 0
    while i < len(names):
        fw.write(names[i] + ',confirm,' + str(num1[i]) + '\n')
        fw.write(names[i] + ',dead,' + str(num3[i]) + '\n')
        fw.write(names[i] + ',heal,' + str(num4[i]) + '\n')
        fw.write(names[i] + ',new_confirm,' + str(num5[i]) + '\n')
        i = i + 1
    else:
        print("Over write file!")
        fw.close()
    return None


def main():
    """
    主逻辑实现
    :return: None
    """
    # 获取数据
    data = get_data()
    num = data['areaTree'][0]['children']
    # 解析数据
    total_data, total_dead_data, total_new_data, total_suspect_data, total_heal_data = handle_data(num)
    # 储存数据
    save_data(total_data, total_dead_data, total_new_data, total_suspect_data, total_heal_data)
    
    return None


if __name__ == '__main__':
    main()
