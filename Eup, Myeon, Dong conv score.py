#!/usr/bin/env python
# coding: utf-8




from IPython.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))





import pandas as pd
import geopandas as gpd
import folium 
import json
import pyproj
from pyproj import Proj, transform,Transformer
from shapely.geometry import Point
from shapely.ops import transform
from functools import partial





#shp 파일에서 불러오기

sd_busan = gpd.read_file('./SD/ctp_rvn_02.shp', encoding='euc-kr')
sd_busan = sd_busan[sd_busan.CTP_KOR_NM.str.contains('부산')].geometry[1]

sd_busan





#epsg 변경
project = pyproj.Transformer.from_proj('EPSG:5179', 'EPSG:4326', always_xy=True).transform
sd_busan = transform(project, sd_busan)




# 읍면동 단위 이동편의성, 생활편의성, 주거편의성 높은 지역 표시

#folium map
lat = sd_busan.centroid.y
lng = sd_busan.centroid.x
location = [lat-0.04, lng]

print(lat,lng)




emd_busan_gdf = pd.read_csv('emd_busan_gdf.csv')





#기준치
th_liv_emd = emd_busan_gdf.living_conv_score_norm.quantile(q=0.9)
th_mov_emd = emd_busan_gdf.move_conv_score_norm.quantile(q=0.9)





m = folium.Map(
    location=location,
    zoom_start=10, 
    tiles= "CartoDB positron", 
)




#부산지역
geo_poly = folium.GeoJson(data=sd_busan, style_function=lambda x: {'fillColor': 'yellow', 'fillOpacity': 0.01})
geo_poly.add_to(m)




emd_busan_gdf['geometry'] = gpd.GeoSeries.from_wkt(emd_busan_gdf['geometry'])




#동별 구분
for polygon in emd_busan_gdf.geometry:
    geo = gpd.GeoSeries(polygon)
    polygon_json = geo.to_json()
    geo_poly = folium.GeoJson(data=polygon_json, style_function=lambda x: {'fillColor': 'yellow',
                                                                           'fillOpacity': 0,
                                                                           'color':'black',
                                                                           'opacity' : 0.3
                                                                          })
    geo_poly.add_to(m)   
    
m    





# 이동편의성만 높은 경우 - 파란색
intersect_poly_lst_move = emd_busan_gdf.loc[(emd_busan_gdf.living_conv_score_norm < th_liv_emd) & (emd_busan_gdf.move_conv_score_norm >= th_mov_emd), ['geometry']]['geometry']
geo_json_lst = []
for polygon in intersect_poly_lst_move:
    geo = gpd.GeoSeries(polygon)
    polygon_json = geo.to_json()
    geo_poly = folium.GeoJson(data=polygon_json, style_function=lambda x: {'fillColor': 'blue', 'fillOpacity': 0.4})
    geo_poly.add_to(m)   





# 생활편의성만 높은 경우 - 빨간색
intersect_poly_lst_liv = emd_busan_gdf.loc[(emd_busan_gdf.living_conv_score_norm >= th_liv_emd) & (emd_busan_gdf.move_conv_score_norm < th_mov_emd), ['geometry']]['geometry']
geo_json_lst = []
for polygon in intersect_poly_lst_liv:
    geo = gpd.GeoSeries(polygon)
    polygon_json = geo.to_json()
    geo_poly = folium.GeoJson(data=polygon_json, style_function=lambda x: {'fillColor': 'red', 'fillOpacity': 0.4})
    geo_poly.add_to(m)   





# 두 편의성 다 높은 경우 - 보라색
intersect_poly_lst_both = emd_busan_gdf.loc[(emd_busan_gdf.living_conv_score_norm >= th_liv_emd) & (emd_busan_gdf.move_conv_score_norm >= th_mov_emd), ['geometry']]['geometry']
geo_json_lst = []
for polygon in intersect_poly_lst_both:
    geo = gpd.GeoSeries(polygon)
    polygon_json = geo.to_json()
    geo_poly = folium.GeoJson(data=polygon_json, style_function=lambda x: {'fillColor': 'purple', 'fillOpacity': 0.6})
    geo_poly.add_to(m)   

m






