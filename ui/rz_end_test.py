# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rz_end_test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1058, 823)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 1001, 751))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.layoutWidget)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(929, 40))
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(20)
        self.title.setFont(font)

        self.verticalLayout_6.addWidget(self.title)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Tencent = QLabel(self.layoutWidget)
        self.Tencent.setObjectName(u"Tencent")
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(12)
        self.Tencent.setFont(font1)
        self.Tencent.setStyleSheet(u"background-color:rgb(170, 255, 255)")

        self.horizontalLayout.addWidget(self.Tencent)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.city = QPushButton(self.layoutWidget)
        self.city.setObjectName(u"city")
        self.city.setMaximumSize(QSize(140, 90))
        self.city.setFont(font1)
        self.city.setAutoRepeatDelay(0)
        self.city.setAutoRepeatInterval(0)
        self.city.setAutoDefault(False)

        self.verticalLayout.addWidget(self.city)

        self.province = QPushButton(self.layoutWidget)
        self.province.setObjectName(u"province")
        self.province.setEnabled(True)
        self.province.setMaximumSize(QSize(140, 90))
        self.province.setFont(font1)

        self.verticalLayout.addWidget(self.province)

        self.data_all = QPushButton(self.layoutWidget)
        self.data_all.setObjectName(u"data_all")
        self.data_all.setMaximumSize(QSize(140, 81))
        self.data_all.setFont(font1)

        self.verticalLayout.addWidget(self.data_all)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.News = QLabel(self.layoutWidget)
        self.News.setObjectName(u"News")
        self.News.setFont(font1)
        self.News.setStyleSheet(u"background-color: rgb(255, 255, 0)")

        self.horizontalLayout_2.addWidget(self.News)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.LDA = QPushButton(self.layoutWidget)
        self.LDA.setObjectName(u"LDA")
        self.LDA.setMaximumSize(QSize(140, 90))
        self.LDA.setFont(font1)
        self.LDA.setAutoRepeatDelay(0)
        self.LDA.setAutoRepeatInterval(0)
        self.LDA.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.LDA)

        self.news_cloud = QPushButton(self.layoutWidget)
        self.news_cloud.setObjectName(u"news_cloud")
        self.news_cloud.setEnabled(True)
        self.news_cloud.setMaximumSize(QSize(140, 90))
        self.news_cloud.setFont(font1)

        self.verticalLayout_3.addWidget(self.news_cloud)

        self.tfidf = QPushButton(self.layoutWidget)
        self.tfidf.setObjectName(u"tfidf")
        self.tfidf.setMaximumSize(QSize(140, 81))
        self.tfidf.setFont(font1)

        self.verticalLayout_3.addWidget(self.tfidf)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Weibo = QLabel(self.layoutWidget)
        self.Weibo.setObjectName(u"Weibo")
        self.Weibo.setFont(font1)
        self.Weibo.setStyleSheet(u"background-color: rgb(255, 85, 255)")

        self.horizontalLayout_3.addWidget(self.Weibo)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.word_rank = QPushButton(self.layoutWidget)
        self.word_rank.setObjectName(u"word_rank")
        self.word_rank.setMaximumSize(QSize(140, 81))
        self.word_rank.setFont(font1)

        self.verticalLayout_4.addWidget(self.word_rank)

        self.weibo_cloud = QPushButton(self.layoutWidget)
        self.weibo_cloud.setObjectName(u"weibo_cloud")
        self.weibo_cloud.setMaximumSize(QSize(140, 81))
        self.weibo_cloud.setFont(font1)
        self.weibo_cloud.setAutoRepeatDelay(0)
        self.weibo_cloud.setAutoRepeatInterval(0)
        self.weibo_cloud.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.weibo_cloud)

        self.data_emotion = QPushButton(self.layoutWidget)
        self.data_emotion.setObjectName(u"data_emotion")
        self.data_emotion.setEnabled(True)
        self.data_emotion.setMaximumSize(QSize(140, 81))
        self.data_emotion.setFont(font1)

        self.verticalLayout_4.addWidget(self.data_emotion)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.show_title = QLabel(self.layoutWidget)
        self.show_title.setObjectName(u"show_title")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_title.sizePolicy().hasHeightForWidth())
        self.show_title.setSizePolicy(sizePolicy)
        self.show_title.setMaximumSize(QSize(578, 20))
        font2 = QFont()
        font2.setFamily(u"\u9ed1\u4f53")
        font2.setPointSize(14)
        self.show_title.setFont(font2)

        self.verticalLayout_2.addWidget(self.show_title)

        self.show_lable = QLabel(self.layoutWidget)
        self.show_lable.setObjectName(u"show_lable")
        sizePolicy.setHeightForWidth(self.show_lable.sizePolicy().hasHeightForWidth())
        self.show_lable.setSizePolicy(sizePolicy)
        self.show_lable.setMaximumSize(QSize(578, 600))

        self.verticalLayout_2.addWidget(self.show_lable)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_6.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1058, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u75ab\u60c5\u671f\u95f4\u7684\u6570\u636e\u5206\u6790\u4e0e\u60c5\u611f\u5206\u6790\u5668", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"                   \u75ab\u60c5\u671f\u95f4\u7684\u6570\u636e\u5206\u6790\u4e0e\u60c5\u611f\u5206\u6790\u5668", None))
        self.Tencent.setText(QCoreApplication.translate("MainWindow", u"       \u817e\u8baf\u7f51\u6570\u636e       ", None))
        self.city.setText(QCoreApplication.translate("MainWindow", u"\u6e56\u5317\u7701\u5404\u5e02\u6570\u636e", None))
        self.province.setText(QCoreApplication.translate("MainWindow", u"\u5404\u7701\u4e4b\u95f4\u75ab\u60c5\u5bf9\u6bd4", None))
        self.data_all.setText(QCoreApplication.translate("MainWindow", u"\u5168\u56fd\u75ab\u60c5\u53d1\u5c55\u8d8b\u52bf", None))
        self.News.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u56fd\u793e\u4f1a\u7ec4\u7ec7\u516c\u5171\u670d\u52a1\u5e73\u53f0", None))
        self.LDA.setText(QCoreApplication.translate("MainWindow", u"LDA\u4e3b\u9898\u8bcd", None))
        self.news_cloud.setText(QCoreApplication.translate("MainWindow", u"\u8bcd\u4e91\u5206\u6790", None))
        self.tfidf.setText(QCoreApplication.translate("MainWindow", u"TF-IDF\u5173\u952e\u8bcd", None))
        self.Weibo.setText(QCoreApplication.translate("MainWindow", u"          \u5fae\u535a          ", None))
        self.word_rank.setText(QCoreApplication.translate("MainWindow", u"\u5173\u952e\u8bcd\u6392\u540d", None))
        self.weibo_cloud.setText(QCoreApplication.translate("MainWindow", u"\u8bcd\u4e91\u5206\u6790", None))
        self.data_emotion.setText(QCoreApplication.translate("MainWindow", u"\u60c5\u611f\u503c\u5206\u6790", None))
        self.show_title.setText(QCoreApplication.translate("MainWindow", u"                       \u6570\u636e\u5c55\u793a\u533a\u57df", None))
        self.show_lable.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"                \u60c5\u611f\u503c\u5206\u6790\u4e2d\u60c5\u611f\u6570\u503c\u57280\u4ee5\u4e0a\u7684\u4e3a\u597d\u60c5\u7eea", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

