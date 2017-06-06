# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from urllib import request
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(370, 341)
        MainWindow.setMaximumHeight(341)
        MainWindow.setMinimumHeight(341)
        MainWindow.setMaximumWidth(370)
        MainWindow.setMinimumWidth(370)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.472636, y1:0.398, x2:1, y2:0, stop:0.426136 rgba(255, 0, 0, 255), stop:1 rgba(167, 0, 0, 255));")
        MainWindow.setWindowTitle("Ask.fm media Downloader")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.uyari = QtWidgets.QMessageBox()
        self.uyari.setIcon(QtWidgets.QMessageBox.Warning)
        self.uyari.setInformativeText("Girdiğiniz link yanlış olabilir.")
        self.uyari.setWindowTitle("- Uyarı -")
        self.uyari.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 311, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.488, y1:0.493, x2:1, y2:0, stop:0.301136 rgba(180, 232, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setText("Ask.fm Kullanıcı Url Adresini Girin")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 40, 311, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("Örn : https://ask.fm/user")
        self.lineEdit.setClearButtonEnabled(True)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 70, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setText("İşlemi Başlat")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeatInterval(200)
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 351, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(255, 235, 255);")
        self.listWidget.setLineWidth(3)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setSortingEnabled(False)
        item = QtWidgets.QListWidgetItem()
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 300, 366, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setFormat("%p%")
        self.progressBar.setValue(0)
        def presBar(d):
            self.progressBar.setValue(d)
            QtGui.QGuiApplication.processEvents()
        def mainloop():
            # creating directories in to the current working directory.
            if os.name == "nt":
                konum = str(os.getcwd())
                resimler = konum + "\medya\\resimler"
                videolar = konum + "\medya\\videolar"
                if not os.path.isdir(resimler):
                    os.makedirs(resimler)
                    os.chmod(resimler, 0o755)
                if not os.path.isdir(videolar):
                    os.makedirs(videolar)
                    os.chmod(videolar, 0o755)
            ana_url = self.lineEdit.text()
            global mesaj_sayisi, url_oku, soup, ek, yuzde
            ek = 1
            url_oku = request.urlopen(ana_url)
            soup = BeautifulSoup(url_oku, 'html.parser')
            mesaj_sayisi = soup.find_all('div', attrs={'class', 'profileTabAnswerCount'}, limit=1)
            mesaj_sayisi = mesaj_sayisi[0].text
            mesaj_sayisi = int(mesaj_sayisi)
            # her yeni html verisinde 25 mesaj bulunduğu için 25 e bölünüyor.
            # every new html data includes 25 new answers, then divide by 25
            if mesaj_sayisi % 25 == 0:
                mesaj_sayisi = mesaj_sayisi / 25
            else:
                mesaj_sayisi = mesaj_sayisi / 25 + 1
            yuzde_oran = 100 / mesaj_sayisi
            yuzde = 0
            yeni_data = 1
            while True:
                resim = soup.find_all('div', attrs={'class', 'streamItem-visualItem'})
                video = soup.find_all('video')
                if str(video) != "[]":
                    for ii in range(0, len(video)):
                        yeni_video = str(video[ii])
                        yeni_video = yeni_video.split('"', 8)
                        video_adi = yeni_video[7].split("video_")
                        if not os.path.isfile(os.sep.join([videolar, video_adi[1]])):
                            open(os.sep.join([videolar, video_adi[1]]), 'w')
                            request.urlretrieve(yeni_video[7], os.sep.join([videolar, video_adi[1]]))
                            metin ="Video kaydedildi --=> " + video_adi[1]
                            item.setText(metin)
                            brush = QtGui.QBrush(QtGui.QColor(32, 132, 255))
                            brush.setStyle(QtCore.Qt.SolidPattern)
                            item.setBackground(brush)
                            item.setFlags(QtCore.Qt.ItemIsEnabled)
                            self.listWidget.addItem(item)
                            QtGui.QGuiApplication.processEvents()
                        ek = ek + 1
                if str(resim) != "[]":
                    for ii in range(0, len(resim)):
                        yeni_resim = str(resim[ii])
                        yeni_resim = yeni_resim.split('"', 18)
                        try:
                            resim_adi = yeni_resim[17].split("/")
                            resim_adi = resim_adi[8]
                            resim_adi = str(ek) + "-" + resim_adi
                            if not os.path.isfile(os.sep.join([resimler, resim_adi])):
                                open(os.sep.join([resimler, resim_adi]), 'w')
                                request.urlretrieve(yeni_resim[17], os.sep.join([resimler, resim_adi]))
                                metin = "Resim kaydedildi ----=> " + resim_adi
                                item.setText(metin)
                                brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                                brush.setStyle(QtCore.Qt.SolidPattern)
                                item.setBackground(brush)
                                item.setFlags(QtCore.Qt.ItemIsEnabled)
                                self.listWidget.addItem(item)
                                QtGui.QGuiApplication.processEvents()
                            ek = ek + 1
                        except:
                            pass
                yuzde = int(yeni_data * yuzde_oran)
                presBar(yuzde)
                try:
                    yeni_link = str(soup.find_all('a', attrs={'class': 'viewMore'}))
                    url = yeni_link.split('"', 6)
                    yeni_link = url[5]
                    yeni_link = yeni_link.split("/", 2)
                    yeni_link = ana_url + "/" + yeni_link[2]
                    QtGui.QGuiApplication.processEvents()
                    url_oku = request.urlopen(yeni_link)
                    QtGui.QGuiApplication.processEvents()
                    soup = BeautifulSoup(url_oku, 'html.parser')
                    yeni_data += 1
                except:
                    print("||| ISLEM TAMAM |||")
                    yuzde = 100
                    presBar(yuzde)
                    break
                QtGui.QGuiApplication.processEvents()
        def kontrol():
            if len(self.lineEdit.text().split("/")) != 4:
                self.uyari.exec_()
            else:
                mainloop()


        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(kontrol)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

