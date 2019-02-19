#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:53:23 2019

@author: tong
"""
import pandas as pd

data = pd.read_csv('/Users/tong/Downloads/globalterrorismdb_0718dist.csv', encoding ='ISO-8859-1')

data.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country', 
                     'provstate':'City','attacktype1_txt':'AttackType','target1':'Target','nkill':'Killed',
                     'nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type',
                     'weaptype1_txt':'Weapon_type', 'motive':'Motive'},inplace=True)

data = data[['Year','Month','Day','Country','City','latitude','longitude','AttackType','Killed','Wounded',
             'Target','Summary','Group','Target_type','Weapon_type','Motive']]

data = data[data.Country== 'United States']

data['Killed'] = data['Killed'].fillna(0)
data['Wounded'] = data['Wounded'].fillna(0)

data['Casualties'] = data['Killed'] + data['Wounded']

data.info()