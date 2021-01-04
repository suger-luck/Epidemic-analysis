# coding=utf-8
import time
import logging
import numpy as np
import pandas as pd
import seaborn as sns
import pyLDAvis.sklearn
import matplotlib.pyplot as plt
from wordcloud import WordCloud as WC
from PySide2.QtCore import QFile
import matplotlib.dates as mdates
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from PySide2.QtUiTools import QUiLoader
from pyecharts.globals import SymbolType
from tencent import province, data_all, city
from weibo import data_count, emotion, keyword
from news import tfidf, CountWord, LDA
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
from PySide2.QtWidgets import QApplication, QMessageBox, QVBoxLayout, QVBoxLayout, QLabel


class main_ui:
    def __init__(self):
        # 从文件中加载定义的ui
        qfile_stats = QFile("ui/rz_end_test.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()
        
        # 从定义的Ui动态的创建相应的窗口对象
        # 注意： 控件的返回值是一个窗体的对象
        # 例如 self.ui.button  self.ui.textEdit
        self.ui = QUiLoader().load(qfile_stats)
        
        # 图标显示区域
        self.fig = plt.Figure()
        self.canvas = FC(self.fig)
        # self.ui.show_lable.to(self.ui)
        layout = QVBoxLayout(self.ui.show_lable)
        layout.addWidget(self.canvas)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # 腾讯网数据显示按钮绑定事件
        self.ui.province.clicked.connect(self.tencent_province_data)
        self.ui.data_all.clicked.connect(self.tencent_all_data)
        self.ui.city.clicked.connect(self.tencent_city)
        
        # 微博数据显示按钮绑定事件
        self.ui.weibo_cloud.clicked.connect(self.weibo_cloud)
        self.ui.data_emotion.clicked.connect(self.weibo_emotion)
        self.ui.word_rank.clicked.connect(self.weibo_keyword)
        
        # 中国社会组织公共服务平台
        self.ui.tfidf.clicked.connect(self.news_tfidf)
        self.ui.news_cloud.clicked.connect(self.news_wordcloud)
        self.ui.LDA.clicked.connect(self.news_lda)
    
    def tencent_province_data(self):
        """
        绘制腾讯网所有省份数据
        :return: None
        """
        try:
            # 爬虫获取
            province.main()
            
            n = "./data/tencent/" + time.strftime("%Y-%m-%d") + "-all-4db.csv"
            data = pd.read_csv(n)
            
            self.fig.clf()  # 清除之前的画图
            ax = self.fig.add_subplot(111)
            # 设置绘图风格及字体
            sns.set_style("whitegrid", {'font.sans-serif': ['simhei', 'Arial']})
            
            # 绘制柱状图
            g = sns.barplot(x="province", y="data", hue="tpye", data=data, ax=ax,
                            palette=sns.color_palette("hls", 8))
            
            # 设置Axes的标题
            ax.set_title('全国疫情' + time.strftime("%Y-%m-%d") + '情况')
            ax.set_xlabel('province_name')
            ax.set_ylabel('Number')
            
            # 设置坐标轴文字方向
            ax.set_xticklabels(ax.get_xticklabels(), rotation=-60)
            
            # 设置坐标轴刻度的字体大小
            ax.tick_params(axis='x', labelsize=8)
            ax.tick_params(axis='y', labelsize=8)
            
            self.canvas.draw()  # TODO:这里开始绘制
        
        except Exception as e:
            print(e)
    
    def tencent_all_data(self):
        """
        腾讯网总的疫情数据
        :return: None
        """
        try:
            # 获取数据
            date_list, confirm_list, suspect_list, dead_list, heal_list = data_all.main()
            self.fig.clf()  # 清除之前的画图
            ax = self.fig.add_subplot(111)
            # ax.cla()
            
            ax.set_title('2020-nCoV疫情曲线')
            
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
            plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
            
            ax.plot(date_list, confirm_list, 'r-', label='确诊')
            ax.plot(date_list, confirm_list, 'rs')
            ax.plot(date_list, suspect_list, 'b-', label='疑似')
            ax.plot(date_list, suspect_list, 'b*')
            ax.plot(date_list, dead_list, 'y-', label='死亡')
            ax.plot(date_list, dead_list, 'y+')
            ax.plot(date_list, heal_list, 'g-', label='治愈')
            ax.plot(date_list, heal_list, 'gd')
            # print(date_list)
            
            ax.set_xlabel('date')
            ax.set_ylabel('Number')
            
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))  # 格式化时间轴标注
            plt.gcf().autofmt_xdate()  # 优化标注（自动倾斜）
            plt.grid(linestyle=':')  # 显示网格
            ax.legend()  # 显示图例
            self.canvas.draw()
        
        except Exception as e:
            print(e)
    
    def tencent_city(self):
        """
        腾讯网 某省各市数据
        :return: None
        """
        try:
            
            # 爬取数据
            city.main()
            # 读取数据
            n = "./data/tencent/" + time.strftime("%Y-%m-%d") + " city-4db.csv"
            data = pd.read_csv(n)
            
            self.fig.clf()  # 清除之前的画图
            ax = self.fig.add_subplot(111)
            
            # 设置绘图风格及字体
            sns.set_style("whitegrid", {'font.sans-serif': ['simhei', 'Arial']})
            
            # 绘制柱状图
            g = sns.barplot(x="province", y="data", hue="type", data=data, ax=ax,
                            palette=sns.color_palette("hls", 8))
            
            title = "湖北" + time.strftime("%Y-%m-%d") + "各市总疫情数据"
            # 设置Axes的标题
            ax.set_title(title)
            ax.set_xlabel('city_name')
            ax.set_ylabel('Number')
            
            # 设置坐标轴文字方向
            ax.set_xticklabels(ax.get_xticklabels(), rotation=-60)
            
            # 设置坐标轴刻度的字体大小
            ax.tick_params(axis='x', labelsize=8)
            ax.tick_params(axis='y', labelsize=8)
            
            self.canvas.draw()  # TODO:这里开始绘制
        except Exception as e:
            print(e)
    
    def weibo_cloud(self):
        """
        微博分词  词云
        :return:
        """
        try:
            # 获取微博数据
            data_count.main()
            # 读取数据文件
            with open("./data/weibo/data-quting.txt", "r", encoding="utf-8") as f:
                wl_space_split = f.read()
            
            # print(wl_space_split)
            
            self.fig.clf()  # 清除之前的画图
            ax = self.fig.add_subplot(111)
            # 设置中文字体
            font = r'C:\Windows\Fonts\simfang.ttf'
            # print("123456798")
            # 对分词后的文本生成词云
            my_wordcloud = WC(collocations=False, font_path=font, width=3000, height=2000,background_color="white").generate(wl_space_split)
            
            # 显示词云图
            ax.imshow(my_wordcloud)
            # 是否显示x轴、y轴下标
            ax.axis("off")
            self.canvas.draw()  # TODO:这里开始绘制
        
        except Exception as e:
            print(e)
    
    def weibo_emotion(self):
        """
        微博情感值
        :return:
        """
        try:
            good, bad, result = emotion.main()
            
            self.fig.clf()  # 清除之前的画图
            ax = self.fig.add_subplot(111)
            ax.plot(np.arange(0, 2017, 1), result, 'k-')
            ax.set_xlabel('Number')
            ax.set_ylabel('Sentiment')
            ax.set_title('Analysis of Sentiments')
            self.canvas.draw()  # TODO:这里开始绘制
            
            data = "好情绪条数:" + str(good) + " 坏情绪条数:" + str(bad)
            QMessageBox.about(
                self.ui,
                "情绪数目统计",
                data
            )
        except Exception as e:
            print(e)
    
    def weibo_keyword(self):
        """
        关键词排行
        :return:
        """
        try:
            data = keyword.main()
            self.fig.clf()  # 清除之前的画图
            ax = self.fig.add_subplot(111)
            ax.axis([0, 10, 0, 10])
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
            plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
            ax.text(3, 3, data, style='italic', color='red', fontsize=15)
            ax.axis('off')
            self.canvas.draw()  # TODO:这里开始绘制
        except Exception as e:
            print(e)
    
    def news_tfidf(self):
        """
        中国社会组织公共服务平台上新闻的tfidf关键词
        :return:
        """
        try:
            # 数据处理
            tfidf.main()
            # 读取数据
            filepath = "./data/news/TF_IDF关键词前50.xlsx"
            ss = pd.read_excel(filepath)
            
            self.fig.clf()  # 清除之前的画图
            ax = self.fig.add_subplot(111)
            
            plt.rcParams["font.sans-serif"] = "SimHei"
            ax.set_title('TF-IDF Ranking')
            ax.barh(range(len(ss.重要性[:25][::-1])), ss.重要性[:25][::-1])
            ax.set_yticks(np.arange(len(ss.重要性[:25][::-1])))
            font = FontProperties(fname=r'c:\windows\fonts\simsun.ttc')
            ax.set_yticklabels(ss.词语[:25][::-1], fontproperties=font)
            ax.set_xlabel('Importance')
            self.canvas.draw()  # TODO:这里开始绘制
        except Exception as e:
            print(e)
    
    def news_wordcloud(self):
        """
        词云显示
        :return:
        """
        try:
            # 数据处理
            CountWord.main()
            
            filepath = "./data/news/" + time.strftime("%Y-%m-%d") + "-fc.csv"
            data = pd.read_csv(filepath, names=["num", "name", "count"])
            print(data["name"])
            
            # 生成数据 word = [('A',10), ('B',9), ('C',8)] 列表+Tuple
            words = list()
            for i in range(1000):
                (k, v) = data["name"][i], int(data["count"][i])
                words.append((k, v))
            
            # 渲染图
            def wordcloud_base() -> WordCloud:
                c = (
                    WordCloud()
                        .add("", words, word_size_range=[20, 100], shape=SymbolType.ROUND_RECT)
                        .set_global_opts(title_opts=opts.TitleOpts(title='全国新型冠状病毒疫情词云图'))
                )
                return c
            
            # print(words)
            # 生成图
            wordcloud_base().render('./data/news/疫情词云图.html')
            data = "词云生成成功，请前往data/news文件夹中查看疫情词云图网页"
            self.fig.clf()  # 清除之前的画图
            ax = self.fig.add_subplot(111)
            ax.axis([0, 10, 0, 10])
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
            plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
            ax.text(0,5, data, style='italic', color='red', fontsize=15)
            ax.axis('off')
            self.canvas.draw()  # TODO:这里开始绘制
        except Exception as e:
            print(e)
    
    def news_lda(self):
        """
        显示lda关键词
        :return:
        """
        
        try:
            lda, tf, tf_vectorizer = LDA.main()
            # print(lda)
            # print("*" * 10)
            data = pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)
            # print(data)
            # 保存在本地
            pyLDAvis.save_html(data, './data/news/news_lda.html')
            # 显示图形
            pyLDAvis.show(data)
        except Exception as e:
            print(e)


def main():
    """
    app 启动
    :return: None
    """
    # 日志配置
    logging.basicConfig(level=logging.INFO,
                        filename='./debug.log',
                        filemode='a',  # 可以写a追加
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    app = QApplication([])
    MainUi = main_ui()
    MainUi.ui.show()
    app.exec_()


if __name__ == '__main__':
    main()
