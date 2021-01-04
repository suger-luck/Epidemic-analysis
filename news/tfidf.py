# coding=utf-8
import pandas as pd
import jieba.analyse
from news import GetBody


def read_data():
    """
    读取数据
    :return:
    """
    filepath = './data/news/news-quting.txt'
    f = open(filepath, encoding='utf-8')
    cut_words = f.read()
    
    return cut_words


def tf_idf(cut_words):
    """
    tfidf计算
    :param cut_word:
    :return:
    """
    # 提取主题词 返回的词频其实就是TF-IDF
    keywords = jieba.analyse.extract_tags(cut_words,
                                          topK=50,
                                          withWeight=True,
                                          allowPOS=('a', 'e', 'n', 'nr', 'ns', 'v'))  # 词性 形容词 叹词 名词 动词
    return keywords


def save_data(keywords):
    """
    储存tfidf计算后的数据
    :param keywords:
    :return:
    """
    pd.DataFrame(keywords, columns=['词语', '重要性']).to_excel('./data/news/TF_IDF关键词前50.xlsx')


def main():
    """
    主逻辑设计
    :return:
    """
    # 获取新闻数据
    GetBody.main()
    # 读取数据
    cut_data = read_data()
    # 计算tfidf
    keywords = tf_idf(cut_data)
    # 保存计算后排名在前50条数据
    save_data(keywords)


if __name__ == '__main__':
    main()
