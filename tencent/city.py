# coding=utf-8
import time, json, requests


def get_data():
    """
    爬取数据
    :return: city
    """
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' % int(time.time() * 1000)
    # print(url)
    data = json.loads(requests.get(url=url).json()['data'])
    # print(data)
    # print(data.keys())
    
    # 统计省份信息(34个省份 湖北 广东 河南 浙江 湖南 安徽....)
    num = data['areaTree'][0]['children']
    # print(len(num))
    
    # 获取某省下标
    k = 0
    for item in num:
        # print(item['name'], end=" ")  # 不换行
        if item['name'] in "湖北":
            # print("")
            # print(item['name'], k)
            break
        k = k + 1
    # print("")  # 换行
    
    # 显示湖北省数据
    city = num[k]['children']
    # for item in city:
    #     print(item)
    # else:
    #     print("\n")
    
    return city


def handle_data(city):
    """
    数据预处理  解析数据
    :param city:
    :return:total_heal_data, total_suspect_data, total_new_data, total_dead_data, total_data
    """
    # 解析确诊数据
    total_data = {}
    for item in city:
        if item['name'] not in total_data:
            total_data.update({item['name']: 0})
        total_data[item['name']] = item['total']['confirm']
    # print('确诊人数')
    # print(total_data)
    
    # 解析疑似数据
    total_suspect_data = {}
    for item in city:
        if item['name'] not in total_suspect_data:
            total_suspect_data.update({item['name']: 0})
        total_suspect_data[item['name']] = item['total']['suspect']
    # print('疑似人数')
    # print(total_suspect_data)
    
    # 解析死亡数据
    total_dead_data = {}
    for item in city:
        if item['name'] not in total_dead_data:
            total_dead_data.update({item['name']: 0})
        total_dead_data[item['name']] = item['total']['dead']
    # print('死亡人数')
    # print(total_dead_data)
    
    # 解析治愈数据
    total_heal_data = {}
    for item in city:
        if item['name'] not in total_heal_data:
            total_heal_data.update({item['name']: 0})
        total_heal_data[item['name']] = item['total']['heal']
    # print('治愈人数')
    # print(total_heal_data)
    
    # 解析新增确诊数据
    total_new_data = {}
    for item in city:
        if item['name'] not in total_new_data:
            total_new_data.update({item['name']: 0})
        total_new_data[item['name']] = item['today']['confirm']  # today
    # print('新增确诊人数')
    # print(total_new_data)
    
    return total_heal_data, total_suspect_data, total_new_data, total_dead_data, total_data


def save_data(total_heal_data, total_suspect_data, total_new_data, total_dead_data, total_data):
    """
    储存数据
    :param total_heal_data:
    :param total_suspect_data:
    :param total_new_data:
    :param total_dead_data:
    :param total_data:
    :return: None
    """
    names = list(total_data.keys())  # 省份名称
    num1 = list(total_data.values())  # 确诊数据
    num2 = list(total_suspect_data.values())  # 疑似数据(全为0)
    num3 = list(total_dead_data.values())  # 死亡数据
    num4 = list(total_heal_data.values())  # 治愈数据
    num5 = list(total_new_data.values())  # 新增确诊病例
    # print(names)
    # print(num1)
    # print(num2)
    # print(num3)
    # print(num4)
    # print(num5)
    
    # 获取当前日期命名(2020-02-13 city.csv)
    n = "./data/tencent/" + time.strftime("%Y-%m-%d") + " city-4db.csv"
    fw = open(n, 'w', encoding='utf-8')
    fw.write('province,type,data\n')
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


def main():
    """
    爬取某省下各市的数据
    :return:
    """
    # 获取数据
    city = get_data()
    # 处理数据
    total_heal_data, total_suspect_data, total_new_data, total_dead_data, total_data = handle_data(city)
    # 保存数据
    save_data(total_heal_data, total_suspect_data, total_new_data, total_dead_data, total_data)


if __name__ == '__main__':
    main()
