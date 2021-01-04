# coding=utf-8
import jieba


def Cut_words():
    """
    分词
    :return:
    """
    cut_words = ""
    all_words = ""
    f = open('./data/weibo/data-fenci.txt', 'w', encoding="utf-8")
    for line in open('./data/weibo/data.txt', encoding='utf-8'):
        line.strip('\n')
        seg_list = jieba.cut(line, cut_all=False)
        # print(" ".join(seg_list))
        cut_words = (" ".join(seg_list))
        # print(cut_words)
        f.write(cut_words)
        all_words += cut_words
    else:
        f.close()


def main():
    """
    主逻辑实现
    :return:
    """
    Cut_words()


if __name__ == '__main__':
    main()
