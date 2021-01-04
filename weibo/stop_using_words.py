import pandas as pd


def read_txt(filepath):
    """
    读取源文件
    """
    file = open(filepath, 'r', encoding='utf-8')
    result = list()
    for c in file.readlines():
        c_array = c.split(" ")
        result.append(c_array)
    return result


def seg_sentence(list_txt):
    """
    取出停用词
    """
    f = open("./data/baidu_stopwords.txt", 'r', encoding='utf-8')
    stopwords = f.read()
    num = 0
    for i in list_txt:
        num += len(i)
    # print("去除停用词前:",num)
    seg_txt = [w for list1 in list_txt for w in list1 if w not in stopwords]
    # print("去除停用词后:",len(seg_txt))
    return seg_txt


def write_txt(seg_txt):
    """
    写入文件
    """
    f = open("./data/weibo/data-quting.txt", "w", encoding="utf-8")
    for word in seg_txt:
        f.write(word)
        f.write(" ")
    f.close()


def main(filepath):
    """
    主逻辑
    """
    txt = read_txt(filepath)
    seg_txt = seg_sentence(txt)
    write_txt(seg_txt)
    return seg_txt


if __name__ == '__main__':
    main("./data/weibo/data-fenci.txt")
