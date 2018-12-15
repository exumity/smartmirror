# -*- coding: utf-8 -*-
import json
import urllib
import datetime


#coding:utf-8
class WeatherService(object):
    def getDailyWeather(self):
        #locale.setlocale(locale.LC_ALL, "tr_TR")
        response = urllib.urlopen("https://servis.mgm.gov.tr/api/tahminler/gunluk?il=Isparta")
        data = json.load(response)
        

        tarihGun1 = data[0]["tarihGun1"][:10]  # 2018-03-02T00:00:00.000Z burdan 2018-03-02 aldık
        tarihGun2 = data[0]["tarihGun2"][:10]
        tarihGun3 = data[0]["tarihGun3"][:10]
        tarihGun4 = data[0]["tarihGun4"][:10]
        tarihGun5 = data[0]["tarihGun5"][:10]

        tarihGun1 = datetime.datetime.strptime(tarihGun1, '%Y-%m-%d')
        tarihGun2 = datetime.datetime.strptime(tarihGun2, '%Y-%m-%d')
        tarihGun3 = datetime.datetime.strptime(tarihGun3, '%Y-%m-%d')
        tarihGun4 = datetime.datetime.strptime(tarihGun4, '%Y-%m-%d')
        tarihGun5 = datetime.datetime.strptime(tarihGun5, '%Y-%m-%d')
        
        

        tarihGun1 = tarihGun1.strftime('%A')
        tarihGun2 = tarihGun2.strftime('%A')
        tarihGun3 = tarihGun3.strftime('%A')
        tarihGun4 = tarihGun4.strftime('%A')
        tarihGun5 = tarihGun5.strftime('%A')
        
        

        enDusukGun1 = data[0]["enDusukGun1"]
        enDusukGun2 = data[0]["enDusukGun2"]
        enDusukGun3 = data[0]["enDusukGun3"]
        enDusukGun4 = data[0]["enDusukGun4"]
        enDusukGun5 = data[0]["enDusukGun5"]

        enYuksekGun1 = data[0]["enYuksekGun1"]
        enYuksekGun2 = data[0]["enYuksekGun2"]
        enYuksekGun3 = data[0]["enYuksekGun3"]
        enYuksekGun4 = data[0]["enYuksekGun4"]
        enYuksekGun5 = data[0]["enYuksekGun5"]

        hadiseGun1 = data[0]["hadiseGun1"]
        hadiseGun2 = data[0]["hadiseGun2"]
        hadiseGun3 = data[0]["hadiseGun3"]
        hadiseGun4 = data[0]["hadiseGun4"]
        hadiseGun5 = data[0]["hadiseGun5"]


        return (
            tarihGun1,
            tarihGun2,
            tarihGun3,
            tarihGun4,
            tarihGun5,
            enDusukGun1,
            enDusukGun2,
            enDusukGun3,
            enDusukGun4,
            enDusukGun5,
            enYuksekGun1,
            enYuksekGun2,
            enYuksekGun3,
            enYuksekGun4,
            enYuksekGun5,
            hadiseGun1,
            hadiseGun2,
            hadiseGun3,
            hadiseGun4,
            hadiseGun5
        )