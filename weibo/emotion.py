# -*- coding: utf-8 -*-
from snownlp import SnowNLP


def emotion_value():
    """
    获取情感分数
    :return:
    """
    source = open("./data/weibo/data.txt", "r", encoding='utf-8')
    line = source.readlines()
    sentimentslist = []
    for j in line:
        for i in j.split("。"):
            # print(i)
            try:
                s = SnowNLP(i)
                # print(s.sentiments)
                sentimentslist.append(s.sentiments)
            except:
                pass
    return sentimentslist


def value_change(sentimentslist):
    """
    情感值转换 并统计
    :param sentimentslist:
    :return:
    """
    # 区间转换为[-0.5, 0.5]
    result = list()
    good = 0
    bad = 0
    i = 0
    while i < len(sentimentslist):
        result.append(sentimentslist[i] - 0.5)
        if sentimentslist[i] - 0.5 > 0:
            good += 1
        else:
            bad += 1
        i = i + 1
    return good, bad, result


def main():
    """
    主逻辑实现
    :return:
    """
    sentimentslist = emotion_value()
    
    good, bad, result = value_change(sentimentslist)
    # print(len(result))
    
    return good, bad, result


if __name__ == '__main__':
    main()
