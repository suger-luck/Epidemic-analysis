# coding=utf-8
import pandas as pd
import weibo.data_count as data_count
import time


def main():
    data_count.main()
    filepath = "./data/weibo/" + time.strftime("%Y-%m-%d") + "-fc.csv"
    data = pd.read_csv(filepath, names=["name", "count"])
    data = str(data[:10])
    return data


if __name__ == '__main__':
    main()
