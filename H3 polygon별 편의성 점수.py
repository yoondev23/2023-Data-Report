#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import folium 
import geopandas as gpd
import json
import pyproj
from pyproj import Proj, transform,Transformer
from shapely.geometry import Point
from shapely.ops import transform
from functools import partial




#shp 파일에서 불러오기

sd_busan = gpd.read_file('./SD/ctp_rvn.shp', encoding='euc-kr')
sd_busan = sd_busan[sd_busan.CTP_KOR_NM.str.contains('부산')].geometry[1]





#epsg 변경
project = pyproj.Transformer.from_proj('EPSG:5179', 'EPSG:4326', always_xy=True).transform
 
sd_busan = transform(project, sd_busan)


# H3 polygon별 편의성 점수

# folium map
lat = sd_busan.centroid.y
lng = sd_busan.centroid.x
location = [lat-0.04, lng]


# 기본맵
m = folium.Map(
    location=location,
    zoom_start=10, 
    tiles= "CartoDB positron", #"Stamen Terrain  CartoDB positron
)





# 부산지역
geo_poly = folium.GeoJson(data=sd_busan, style_function=lambda x: {'fillColor': 'yellow', 'fillOpacity': 0.01})
geo_poly.add_to(m)


# # 기준치 점수

h3_conv_score = pd.read_csv('h3_conv_score.csv')

# 기준치
th_liv_h3 = h3_conv_score.living_conv_score_norm.quantile(q=0.8)
th_mov_h3 = h3_conv_score.move_conv_score_norm.quantile(q=0.8)
th_house_h3 = 0.8




h3_conv_score.head(5)



h3_conv_score['geometry'] = gpd.GeoSeries.from_wkt(h3_conv_score['geometry'])


intersect_poly_lst_move = h3_conv_score.loc[(h3_conv_score.living_conv_score_norm < th_liv_h3) & (h3_conv_score.move_conv_score_norm >= th_mov_h3), ['geometry']]['geometry']
intersect_poly_lst_move





# 이동편의성만 높은 경우

for polygon in intersect_poly_lst_move:
    geo = gpd.GeoSeries(polygon)
    polygon_json = geo.to_json()
    geo_poly = folium.GeoJson(data=polygon_json, style_function=lambda x: {'fillColor': 'blue', 'fillOpacity': 0.4})
    geo_poly.add_to(m)  





# 생활편의성만 높은 경우

intersect_poly_lst_liv = h3_conv_score.loc[(h3_conv_score.living_conv_score_norm >= th_liv_h3) & (h3_conv_score.move_conv_score_norm < th_mov_h3), ['geometry']]['geometry']
geo_json_lst = []

for polygon in intersect_poly_lst_liv:
    geo = gpd.GeoSeries(polygon)
    polygon_json = geo.to_json()
    geo_poly = folium.GeoJson(data=polygon_json, style_function=lambda x: {'fillColor': 'red', 'fillOpacity': 0.3})
    geo_poly.add_to(m)   





# 두 편의성 다 높은 경우

intersect_poly_lst_both = h3_conv_score.loc[(h3_conv_score.living_conv_score_norm >= th_liv_h3) & (h3_conv_score.move_conv_score_norm >= th_mov_h3), ['geometry']]['geometry']
geo_json_lst = []

for polygon in intersect_poly_lst_both:
    geo = gpd.GeoSeries(polygon)
    polygon_json = geo.to_json()
    geo_poly = folium.GeoJson(data=polygon_json, style_function=lambda x: {'fillColor': 'purple', 'fillOpacity': 0.6})
    geo_poly.add_to(m)   





# 주거편의성 높은 경우

intersect_poly_lst_house = h3_conv_score.loc[(h3_conv_score.house_conv_score_norm_final > 0.8)]['geometry']
geo_json_lst = []

for polygon in intersect_poly_lst_house:
    geo = gpd.GeoSeries(polygon)
    polygon_json = geo.to_json()
    geo_poly = folium.GeoJson(data=polygon_json, style_function=lambda x: {'fillColor': 'white', 'fillOpacity': 0.8})
    geo_poly.add_to(m)   





folium.LatLngPopup().add_to(m)
m






