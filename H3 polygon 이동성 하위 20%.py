#!/usr/bin/env python
# coding: utf-8

# In[20]:


from IPython.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))


# In[22]:


import pandas as pd
import geopandas as gpd
import folium 
import json
import pyproj
from pyproj import Proj, transform,Transformer
from shapely.geometry import Point
from shapely.ops import transform
from functools import partial


# In[36]:


#shp 파일에서 불러오기

sd_busan = gpd.read_file('./SD/ctp_rvn.shp', encoding='euc-kr')
sd_busan = sd_busan[sd_busan.CTP_KOR_NM.str.contains('부산')].geometry[1]


# In[37]:


#epsg 변경
project = pyproj.Transformer.from_proj('EPSG:5179', 'EPSG:4326', always_xy=True).transform
sd_busan = transform(project, sd_busan)


# In[38]:


# folium map
lat = sd_busan.centroid.y
lng = sd_busan.centroid.x
location = [lat-0.04, lng]


# In[39]:


# 기본맵
m = folium.Map(
    location=location,
    zoom_start=10, 
    tiles= "CartoDB positron", #"Stamen Terrain  CartoDB positron
)


# In[40]:


# 부산지역
geo_poly = folium.GeoJson(data=sd_busan, style_function=lambda x: {'fillColor': 'yellow', 'fillOpacity': 0.01,
                                                                   'color':'black','opacity':0.3})
geo_poly.add_to(m)

m


# In[41]:


# # 기준치 : 점수 분포 20분위

h3_conv_score = pd.read_csv('h3_conv_score.csv')


# In[42]:


# 기준치
th_mov_h3 = h3_conv_score.move_conv_score_norm.quantile(q=0.2)


# In[43]:


h3_conv_score['geometry'] = gpd.GeoSeries.from_wkt(h3_conv_score['geometry'])


# In[44]:


# 이동편의성 하위 20%
intersect_poly_lst_move = h3_conv_score.loc[(h3_conv_score.move_conv_score_norm < th_mov_h3), ['geometry']]['geometry']


# In[45]:


for polygon in intersect_poly_lst_move:
    geo = gpd.GeoSeries(polygon)
    polygon_json = geo.to_json()
    geo_poly = folium.GeoJson(data=polygon_json, style_function=lambda x: {'fillColor': 'purple',
                                                                           'fillOpacity': 0.4,
                                                                           'color':'black',
                                                                           'opacity':0.3})
    geo_poly.add_to(m)
    
m


# In[14]:


# 이동편의성 하위 20%의 중심점 출력
intersect_poly_lst_move = h3_conv_score.loc[(h3_conv_score.move_conv_score_norm < th_mov_h3), ['geometry']]['geometry']
intersect_poly_lst_move 


# In[ ]:




