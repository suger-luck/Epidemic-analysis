# coding=utf-8
import time
from news import GetBody
from collections import Counter


def read_data():
    """
    读取数据并分隔数据
    :return:
    """
    filepath = "./data/news/news-quting.txt"
    with open(filepath, "r", encoding="utf-8") as f:
        all_words = f.read()
    
    return all_words.split()


def word_count(all_words):
    """
    统计数据
    :param all_words:
    :return:
    """
    c = Counter()
    for x in all_words:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    return c


def save_data(c):
    """
    储存数据
    :param c:
    :return:
    """
    # 存储数据
    name = "./data/news/" + time.strftime("%Y-%m-%d") + "-fc.csv"
    fw = open(name, 'w', encoding='utf-8')
    i = 1
    for (k, v) in c.most_common(len(c)):
        fw.write(str(i) + ',' + str(k) + ',' + str(v) + '\n')
        i = i + 1
    else:
        print("Over write file!")
        fw.close()


def main():
    """
    主逻辑实现
    :return:
    """
    # 获取正文数据
    GetBody.main()
    # 读取数据
    all_words = read_data()
    # 统计数据
    c = word_count(all_words)
    # 存储数据
    save_data(c)


if __name__ == '__main__':
    main()
