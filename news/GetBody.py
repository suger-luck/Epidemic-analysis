# coding=utf-8
import pandas as pd
import jieba


def get_body():
    """
    分离出新闻的正文并保存
    :return:
    """
    data = pd.read_csv("./data/news/news.csv")
    
    with open("./data/news/news.txt", "w", encoding="utf-8") as f:
        for i in range(len(data["article_text"])):
            f.write(str(data["article_text"][i]))
            f.write("\n")


def cut_body():
    """
    将正文内容进行分词
    :return:
    """
    cut_words = ""
    all_words = ""
    f = open('./data/news/news-fenci.txt', 'w', encoding="utf-8")
    for line in open('./data/news/news.txt', encoding='utf-8'):
        line.strip('\n')
        seg_list = jieba.cut(line, cut_all=False)
        # print(" ".join(seg_list))
        cut_words = (" ".join(seg_list))
        # print("*" * 5)
        # print(cut_words)
        f.write(cut_words)
        all_words += cut_words
    else:
        f.close()


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
    # print("去除停用词前:", num)
    seg_txt = [w for list1 in list_txt for w in list1 if w not in stopwords]
    # print("去除停用词后:", len(seg_txt))
    return seg_txt


def write_txt(seg_txt):
    """
    写入文件
    """
    f = open("./data/news/news-quting.txt", "w", encoding="utf-8")
    for word in seg_txt:
        f.write(word)
        f.write(" ")
    f.close()


def del_stopword():
    """
    将分词后的内容进行去停用词处理
    :return:
    """
    # 读取文件
    txt = read_txt("./data/news/news-fenci.txt")
    # 去掉停用词
    seg_txt = seg_sentence(txt)
    # 写入文件
    write_txt(seg_txt)


def main():
    """
    主逻辑实现
    :return:
    """
    # 获取正文数据
    get_body()
    # 分词
    cut_body()
    # 去停用词
    del_stopword()


if __name__ == '__main__':
    main()
