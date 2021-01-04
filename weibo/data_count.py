# coding=utf-8
import time
from collections import Counter
import weibo.stop_using_words as suw
from weibo import CutWords


def count(all_words):
    """
    统计词频
    :return:
    """
    # print(all_words)
    # 词频统计
    c = Counter()
    for x in all_words:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    return c


def save_data(c):
    """
    保存数据
    :return:
    """
    # 存储数据
    name = "./data/weibo/" + time.strftime("%Y-%m-%d") + "-fc.csv"
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
    # 执行分词程序
    CutWords.main()
    filepath = "./data/weibo/data-fenci.txt"
    # 去停用词
    all_words = suw.main(filepath)
    # 词频统计
    c = count(all_words)
    # 保存统计后的词频
    save_data(c)


if __name__ == '__main__':
    main()
