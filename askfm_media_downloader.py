# -*- coding: utf-8 -*-
# CENGİZ ÜÇGÜL

from bs4 import BeautifulSoup
from urllib import request
import os

# creating directories in to the current working directory.
if os.name=="nt":
    konum = str(os.getcwd())
    resimler = konum + "\medya\\resimler"
    videolar = konum + "\medya\\videolar"
    if not os.path.isdir(resimler):
        os.makedirs(resimler)
        os.chmod(resimler, 0o755)
    if not os.path.isdir(videolar):
        os.makedirs(videolar)
        os.chmod(videolar, 0o755)

# simple url for specified account like this
ana_url = "https://ask.fm/bala_balance"

global mesaj_sayisi,url_oku,soup,ek,yuzde

ek = 1
url_oku = request.urlopen(ana_url)
soup = BeautifulSoup(url_oku, 'html.parser')
mesaj_sayisi = soup.find_all('div',attrs={'class','profileTabAnswerCount'},limit=1)
mesaj_sayisi = mesaj_sayisi[0].text
mesaj_sayisi = int(mesaj_sayisi)

# her yeni html verisinde 25 mesaj bulunduğu için 25 e bölünüyor.
# every new html data includes 25 new answers, then divide by 25
if mesaj_sayisi%25 == 0:
    mesaj_sayisi= mesaj_sayisi / 25
else:
    mesaj_sayisi = mesaj_sayisi / 25 + 1
yuzde_oran = 100 / mesaj_sayisi
yuzde=0
yeni_data = 1
while True:
    resim = soup.find_all('div',attrs={'class','streamItem-visualItem'})
    video = soup.find_all('video')
    if str(video) != "[]":
        for ii in range(0,len(video)):
            yeni_video = str(video[ii])
            yeni_video = yeni_video.split('"',8)
            video_adi = yeni_video[7].split("/")
            if not os.path.isfile(os.sep.join([videolar,video_adi[-1]])):
                open(os.sep.join([videolar, video_adi[-1]]), 'w')
                dosya = request.urlretrieve(yeni_video[7], os.sep.join([videolar, video_adi[-1]]))
                print("Video kaydedildi ----=> ", video_adi[-1])
            ek = ek + 1
    if str(resim) != "[]":
        for ii in range(0,len(resim)):
            yeni_resim = str(resim[ii])
            kontrol = yeni_resim.split('"',4)
            if kontrol[3] == "ImageOpen":
                try:
                    yeni_resim = yeni_resim.split('"', 18)
                    resim_adi = yeni_resim[17].split("/")
                    resim_adi = resim_adi[-1]
                    resim_adi = str(ek) + "-" + resim_adi
                    if not os.path.isfile(os.sep.join([resimler, resim_adi])):
                        open(os.sep.join([resimler, resim_adi]), 'w')
                        dosya = request.urlretrieve(yeni_resim[17], os.sep.join([resimler, resim_adi]))
                        print("Resim kaydedildi ----=> ", resim_adi)
                    ek = ek + 1
                except:
                    pass
    yuzde = int(yeni_data * yuzde_oran)
    print(yuzde)
    try:
        yeni_link = str(soup.find_all('a', attrs={'class': 'viewMore'}))
        url = yeni_link.split('"', 6)
        yeni_link = url[5]
        yeni_link = yeni_link.split("/", 2)
        yeni_link = ana_url + "/" + yeni_link[2]
        url_oku = request.urlopen(yeni_link)
        soup = BeautifulSoup(url_oku, 'html.parser')
        yeni_data += 1
    except:
        print("||| ISLEM TAMAM |||")
        yuzde = 100
        break
