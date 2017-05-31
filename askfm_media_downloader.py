# -*- coding: utf-8 -*-
# CENGİZ ÜÇGÜL

from bs4 import BeautifulSoup
import urllib.request
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
ana_url = "https://ask.fm/star_icons"

global url_oku
global soup
global ek
url_oku = urllib.request.urlopen(ana_url)
soup = BeautifulSoup(url_oku, 'html.parser')
ek = 1
while True:
    resim = soup.find_all('div',attrs={'class','streamItem-visualItem'})
    video = soup.find_all('video')

    if str(video) != "[]":
        for ii in range(0,len(video)):
            yeni_video = str(video[ii])
            yeni_video = yeni_video.split('"',8)
            video_adi = yeni_video[7].split("video_")
            if not os.path.isfile(os.sep.join([videolar,video_adi[1]])):
                open(os.sep.join([videolar, video_adi[1]]), 'w')
                dosya = urllib.request.urlretrieve(yeni_video[7], os.sep.join([videolar, video_adi[1]]))
                print("Video kaydedildi ----=> ", video_adi[1])
            ek = ek + 1
    if str(resim) != "[]":

        for ii in range(0,len(resim)):
            yeni_resim = str(resim[ii])
            yeni_resim = yeni_resim.split('"',18)
            try:
                resim_adi = yeni_resim[17].split("/")
                resim_adi = resim_adi[8]
                resim_adi = str(ek) + "-" + resim_adi
                if not os.path.isfile(os.sep.join([resimler, resim_adi])):
                    open(os.sep.join([resimler, resim_adi]), 'w')
                    dosya = urllib.request.urlretrieve(yeni_resim[17], os.sep.join([resimler, resim_adi]))
                    print("Resim kaydedildi ----=> ", resim_adi)
                ek = ek + 1
            except:
                pass

    try:
        yeni_link = str(soup.find_all('a', attrs={'class': 'viewMore'}))
        url = yeni_link.split('"', 6)
        yeni_link = url[5]
        yeni_link = yeni_link.split("/", 2)
        yeni_link = ana_url + "/" + yeni_link[2]
        url_oku = urllib.request.urlopen(yeni_link)
        soup = BeautifulSoup(url_oku, 'html.parser')
    except:
        print("||| ISLEM TAMAM |||")
        break