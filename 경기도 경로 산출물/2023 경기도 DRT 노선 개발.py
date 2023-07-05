#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import display, HTML
display(HTML("<style>.container { width:70% !important; }</style>"))


# ! pip install networkx

# In[5]:


import osmnx as ox, networkx as nx
import folium


#  # 1. 하남시

# In[11]:


G1 = ox.graph_from_place('하남시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(G1,127.2235, 37.5225)
dest_node1 = ox.nearest_nodes(G1,127.2047, 37.5381) 

orig_node2 = ox.nearest_nodes(G1,127.2047, 37.5381) 
dest_node2 = ox.nearest_nodes(G1,127.1982, 37.5552) 

orig_node3 = ox.nearest_nodes(G1,127.1982, 37.5552) 
dest_node3 = ox.nearest_nodes(G1,127.1874 ,37.5565) 


route1 =  nx.shortest_path(G1, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(G1, orig_node2, dest_node2, weight='length')
route3 =  nx.shortest_path(G1, orig_node3, dest_node3, weight='length')
route_list = [route1,route2,route3]


#첫 번째 경로
R1 = ox.folium.plot_route_folium(G1, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(G1, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

R3 = ox.folium.plot_route_folium(G1, route3, route_map=R2,
                                 tiles='OpenStreetMap',
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1,#라인 투명도
                                 zoom=0.1) 


marker1 = folium.Marker( [ 37.5225, 127.2235 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker2 = folium.Marker( [ 37.5381, 127.2047 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker3 = folium.Marker( [ 37.5552, 127.1982 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker4 = folium.Marker( [ 37.5565, 127.1874 ], icon = folium.Icon(color='blue')).add_to( R3 )

R3


# # 2. 고양시_01

# In[12]:


고양시 = ox.graph_from_place('고양시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(고양시,126.7838, 37.6426)
dest_node1 = ox.nearest_nodes(고양시,126.7925, 37.6453) 

orig_node2 = ox.nearest_nodes(고양시,126.7925, 37.6453) 
dest_node2 = ox.nearest_nodes(고양시,126.8057, 37.6744) 

orig_node3 = ox.nearest_nodes(고양시,126.8057, 37.6744) 
dest_node3 = ox.nearest_nodes(고양시,126.7686, 37.6948) 


route1 =  nx.shortest_path(고양시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(고양시, orig_node2, dest_node2, weight='length')
route3 =  nx.shortest_path(고양시, orig_node3, dest_node3, weight='length')
route_list = [route1,route2,route3]


R1 = ox.folium.plot_route_folium(고양시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(고양시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

R3 = ox.folium.plot_route_folium(고양시, route3, route_map=R2,
                                 tiles='OpenStreetMap',
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1,#라인 투명도
                                 zoom=0.1) 

marker1 = folium.Marker( [ 37.6426, 126.7838 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker2 = folium.Marker( [ 37.6453, 126.7925 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker3 = folium.Marker( [ 37.6744, 126.8057 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker4 = folium.Marker( [ 37.6948, 126.7686 ], icon = folium.Icon(color='blue')).add_to( R3 )

R3


# # 3. 과천시

# In[21]:


과천시 = ox.graph_from_place('과천시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(과천시,126.9944, 37.4252)
dest_node1 = ox.nearest_nodes(과천시,127.00207887675619, 37.428800934998876) 

orig_node2 = ox.nearest_nodes(과천시,127.00207887675619, 37.428800934998876) 
dest_node2 = ox.nearest_nodes(과천시,126.9966, 37.4357) 

orig_node3 = ox.nearest_nodes(과천시,126.9966, 37.4357) 
dest_node3 = ox.nearest_nodes(과천시,126.9921, 37.4324) 


route1 =  nx.shortest_path(과천시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(과천시, orig_node2, dest_node2, weight='length')
route3 =  nx.shortest_path(과천시, orig_node3, dest_node3, weight='length')
route_list = [route1,route2,route3]


R1 = ox.folium.plot_route_folium(과천시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(과천시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

R3 = ox.folium.plot_route_folium(과천시, route3, route_map=R2,
                                 tiles='OpenStreetMap',
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1,#라인 투명도
                                 zoom=0.1) 


marker1 = folium.Marker( [ 37.4252, 126.9944 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker2 = folium.Marker( [ 37.4288, 127.0025 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker3 = folium.Marker( [ 37.4357, 126.9972 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker4 = folium.Marker( [ 37.4324, 126.9921 ], icon = folium.Icon(color='blue')).add_to( R3 )

R3


# # 4. 구리시

# In[24]:


구리시 = ox.graph_from_place('구리시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(구리시,127.1401, 37.5934)
dest_node1 = ox.nearest_nodes(구리시,127.1343, 37.5973) 

orig_node2 = ox.nearest_nodes(구리시,127.1343, 37.5973) 
dest_node2 = ox.nearest_nodes(구리시,127.1385, 37.6003) 

orig_node3 = ox.nearest_nodes(과천시,127.1385, 37.6003) 
dest_node3 = ox.nearest_nodes(과천시,127.1423, 37.6038) 


route1 =  nx.shortest_path(구리시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(구리시, orig_node2, dest_node2, weight='length')
route_list = [route1,route2]


R1 = ox.folium.plot_route_folium(구리시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(구리시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도


marker1 = folium.Marker( [ 37.5934, 127.1401 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker2 = folium.Marker( [ 37.5973, 127.1343 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker3 = folium.Marker( [ 37.6003, 127.1385 ], icon = folium.Icon(color='blue')).add_to( R2 )

R2


# # 5. 남양주시

# In[25]:


남양주시 = ox.graph_from_place('남양주시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(남양주시,127.1441, 37.6477)
dest_node1 = ox.nearest_nodes(남양주시,127.1551, 37.6050) 

orig_node2 = ox.nearest_nodes(남양주시,127.1551, 37.6050) 
dest_node2 = ox.nearest_nodes(남양주시,127.2063, 37.6330) 

orig_node3 = ox.nearest_nodes(남양주시,127.2063, 37.6330) 
dest_node3 = ox.nearest_nodes(남양주시,127.2396, 37.6597) 


route1 =  nx.shortest_path(남양주시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(남양주시, orig_node2, dest_node2, weight='length')
route3 =  nx.shortest_path(남양주시, orig_node3, dest_node3, weight='length')
route_list = [route1,route2,route3]


R1 = ox.folium.plot_route_folium(남양주시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(남양주시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

R3 = ox.folium.plot_route_folium(남양주시, route3, route_map=R2,
                                 tiles='OpenStreetMap',
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1,#라인 투명도
                                 zoom=0.1) 

marker1 = folium.Marker( [ 37.6477, 127.1441 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker2 = folium.Marker( [ 37.6050, 127.1551 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker3 = folium.Marker( [ 37.6330, 127.2063 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker4 = folium.Marker( [ 37.6597, 127.2396 ], icon = folium.Icon(color='blue')).add_to( R3 )


R3


# # 6. 수원시

# In[29]:


수원시 = ox.graph_from_place('수원시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(수원시,126.9572, 37.2608)
dest_node1 = ox.nearest_nodes(수원시,127.0304, 37.2798) 

orig_node2 = ox.nearest_nodes(수원시,127.0304, 37.2798) 
dest_node2 = ox.nearest_nodes(수원시,126.9917, 37.2929) 

route1 =  nx.shortest_path(수원시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(수원시, orig_node2, dest_node2, weight='length')
route_list = [route1,route2]


R1 = ox.folium.plot_route_folium(수원시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(수원시, route2, route_map=R1,
                                  tiles='OpenStreetMap', #베이스맵
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

marker1 = folium.Marker( [ 37.2608, 126.9572 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker2 = folium.Marker( [ 37.2798, 127.0304 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker3 = folium.Marker( [ 37.2929, 126.9917 ], icon = folium.Icon(color='blue')).add_to( R2 )

R2


# # 7. 시흥

# In[34]:


시흥시 = ox.graph_from_place('시흥시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(시흥시,126.7974, 37.4465)
dest_node1 = ox.nearest_nodes(시흥시,126.7851, 37.4383) 

route1 =  nx.shortest_path(시흥시, orig_node1, dest_node1, weight='length')

R1 = ox.folium.plot_route_folium(시흥시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

marker1 = folium.Marker( [ 37.4465, 126.7974 ], icon = folium.Icon(color='blue')).add_to( R1 )
marker2 = folium.Marker( [ 37.4383, 126.7846 ], icon = folium.Icon(color='blue')).add_to( R1 )



R1


# # 8. 안산

# In[35]:


안산시 = ox.graph_from_place('안산시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(안산시,126.8551, 37.2862)
dest_node1 = ox.nearest_nodes(안산시,126.84449030304268,37.318406499973136) 

orig_node2 = ox.nearest_nodes(안산시,126.84449030304268,37.318406499973136) 
dest_node2 = ox.nearest_nodes(안산시,126.8462, 37.2999) 

orig_node3 = ox.nearest_nodes(안산시,126.8462, 37.2999) 
dest_node3 = ox.nearest_nodes(안산시,126.8113, 37.3039) 


route1 =  nx.shortest_path(안산시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(안산시, orig_node2, dest_node2, weight='length')
route3 =  nx.shortest_path(안산시, orig_node3, dest_node3, weight='length')
route_list = [route1,route2,route3]


R1 = ox.folium.plot_route_folium(안산시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(안산시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

R3 = ox.folium.plot_route_folium(안산시, route3, route_map=R2,
                                 tiles='OpenStreetMap',
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1,#라인 투명도
                                 zoom=0.1) 

marker1 = folium.Marker( [ 37.2862, 126.8551 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker2 = folium.Marker( [ 37.3184, 126.8444 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker3 = folium.Marker( [ 37.2999, 126.8462 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker4 = folium.Marker( [ 37.3039, 126.8113 ], icon = folium.Icon(color='blue')).add_to( R3 )

R3


# # 9. 여주

# In[36]:


여주시 = ox.graph_from_place('여주시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(여주시,127.6379, 37.2039)
dest_node1 = ox.nearest_nodes(여주시,127.6558, 37.2836) 

orig_node2 = ox.nearest_nodes(여주시,127.6558, 37.2836) 
dest_node2 = ox.nearest_nodes(여주시,127.6369, 37.2978) 

route1 =  nx.shortest_path(여주시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(여주시, orig_node2, dest_node2, weight='length')
route_list = [route1,route2]


R1 = ox.folium.plot_route_folium(여주시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(여주시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

marker1 = folium.Marker( [ 37.2039, 127.6379 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker2 = folium.Marker( [ 37.2836, 127.6558 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker3 = folium.Marker( [ 37.2978, 127.6369 ], icon = folium.Icon(color='blue')).add_to( R2 )

R2


# # 10. 용인

# In[37]:


용인시 = ox.graph_from_place('용인시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(용인시,127.2186, 37.2595)
dest_node1 = ox.nearest_nodes(용인시,127.2129, 37.2374) 

orig_node2 = ox.nearest_nodes(용인시,127.2129, 37.2374) 
dest_node2 = ox.nearest_nodes(용인시,127.1266, 37.2707) 

orig_node3 = ox.nearest_nodes(용인시,127.1266, 37.2707) 
dest_node3 = ox.nearest_nodes(용인시,127.1110, 37.2890) 

orig_node3 = ox.nearest_nodes(용인시,127.1110, 37.2890) 
dest_node3 = ox.nearest_nodes(용인시,127.0934, 37.3318) 

orig_node4 = ox.nearest_nodes(용인시,127.0934, 37.3318) 
dest_node4 = ox.nearest_nodes(용인시,127.1056, 37.3154) 

orig_node5 = ox.nearest_nodes(용인시,127.1056, 37.3154) 
dest_node5 = ox.nearest_nodes(용인시,127.0934, 37.3318) 

orig_node6 = ox.nearest_nodes(용인시,127.0934, 37.3318) 
dest_node6 = ox.nearest_nodes(용인시,127.1094, 37.2443) 

route1 =  nx.shortest_path(용인시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(용인시, orig_node2, dest_node2, weight='length')
route3 =  nx.shortest_path(용인시, orig_node3, dest_node3, weight='length')
route4 =  nx.shortest_path(용인시, orig_node4, dest_node1, weight='length')
route5 =  nx.shortest_path(용인시, orig_node5, dest_node2, weight='length')
route6 =  nx.shortest_path(용인시, orig_node6, dest_node3, weight='length')
route_list = [route1,route2,route3,route4,route5,route6]

R1 = ox.folium.plot_route_folium(용인시, route1, route_map=None,   
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(용인시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

R3 = ox.folium.plot_route_folium(용인시, route3, route_map=R2,
                                 tiles='OpenStreetMap',
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1,#라인 투명도
                                 zoom=0.1) 

R4 = ox.folium.plot_route_folium(용인시, route4, route_map=R3,   
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R5 = ox.folium.plot_route_folium(용인시, route5, route_map=R4,
                                 tiles='OpenStreetMap',
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

# R6 = ox.folium.plot_route_folium(용인시, route6, route_map=R5,
#                                  tiles='OpenStreetMap',
#                                  color='#232B99', 
#                                  weight=10, 
#                                  opacity=1,
#                                  zoom=0.1) 

R5


# # 11. 의정부

# In[39]:


의정부 = ox.graph_from_place('의정부시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(의정부,127.0965, 37.7458)
dest_node1 = ox.nearest_nodes(의정부,127.08656092276149, 37.74363916828183) 

orig_node2 = ox.nearest_nodes(의정부,127.08656092276149, 37.74363916828183) 
dest_node2 = ox.nearest_nodes(의정부,127.0507, 37.7452) 

orig_node3 = ox.nearest_nodes(의정부,127.0507, 37.7452) 
dest_node3 = ox.nearest_nodes(의정부,127.0526, 37.7374) 


route1 =  nx.shortest_path(의정부, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(의정부, orig_node2, dest_node2, weight='length')
route3 =  nx.shortest_path(의정부, orig_node3, dest_node3, weight='length')
route_list = [route1,route2,route3]


R1 = ox.folium.plot_route_folium(의정부, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(의정부, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

R3 = ox.folium.plot_route_folium(의정부, route3, route_map=R2,
                                 tiles='OpenStreetMap',
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1,#라인 투명도
                                 zoom=0.1) 

marker1 = folium.Marker( [ 37.7458, 127.0965 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker2 = folium.Marker( [ 37.74363916828183, 127.08656092276149 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker3 = folium.Marker( [ 37.7452, 127.0507 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker4 = folium.Marker( [ 37.7374, 127.0526 ], icon = folium.Icon(color='blue')).add_to( R3 )


R3


# # 12. 이천

# In[40]:


이천시 = ox.graph_from_place('이천시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(이천시,127.4442, 37.2789)
dest_node1 = ox.nearest_nodes(이천시,127.4582, 37.2611) 

orig_node2 = ox.nearest_nodes(이천시,127.4582, 37.2611) 
dest_node2 = ox.nearest_nodes(이천시,127.4537, 37.2089) 

route1 =  nx.shortest_path(이천시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(이천시, orig_node2, dest_node2, weight='length')
route_list = [route1,route2]


R1 = ox.folium.plot_route_folium(이천시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(이천시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

marker1 = folium.Marker( [ 37.2789, 127.4442 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker2 = folium.Marker( [ 37.2611, 127.4582 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker3 = folium.Marker( [ 37.2089, 127.4537 ], icon = folium.Icon(color='blue')).add_to( R2 )

R2


# # 13. 파주

# In[42]:


파주시 = ox.graph_from_place('파주시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(파주시,126.77865821714742, 37.755973047311706)
dest_node1 = ox.nearest_nodes(파주시,126.76730384513105, 37.753545599249705) 

orig_node2 = ox.nearest_nodes(파주시,126.76730384513105, 37.753545599249705) 
dest_node2 = ox.nearest_nodes(파주시,126.7549, 37.7096) 

route1 =  nx.shortest_path(파주시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(파주시, orig_node2, dest_node2, weight='length')
route_list = [route1,route2]


R1 = ox.folium.plot_route_folium(파주시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(파주시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

marker1 = folium.Marker( [ 37.755973047311706, 126.77865821714742 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker2 = folium.Marker( [ 37.753545599249705, 126.76730384513105 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker3 = folium.Marker( [ 37.7096, 126.7549 ], icon = folium.Icon(color='blue')).add_to( R2 )

R2


# # 14. 평택

# In[43]:


평택시 = ox.graph_from_place('평택시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(평택시,127.1051, 36.9878)
dest_node1 = ox.nearest_nodes(평택시,127.1130, 36.9963) 

orig_node2 = ox.nearest_nodes(평택시,127.1130, 36.9963) 
dest_node2 = ox.nearest_nodes(평택시,127.0866, 36.9918) 

route1 =  nx.shortest_path(평택시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(평택시, orig_node2, dest_node2, weight='length')
route_list = [route1,route2]


R1 = ox.folium.plot_route_folium(평택시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(평택시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

marker1 = folium.Marker( [ 36.9878, 127.1051 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker2 = folium.Marker( [ 36.9963, 127.1130 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker3 = folium.Marker( [ 36.9918, 127.0866 ], icon = folium.Icon(color='blue')).add_to( R2 )

R2


# # 15. 광주

# In[46]:


광주시 = ox.graph_from_place('광주시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(광주시,127.2509, 37.4162)
dest_node1 = ox.nearest_nodes(광주시,127.2577, 37.4110) 

orig_node2 = ox.nearest_nodes(광주시,127.2577, 37.4110) 
dest_node2 = ox.nearest_nodes(광주시,127.3354, 37.3557) 

orig_node3 = ox.nearest_nodes(광주시,127.3354, 37.3557) 
dest_node3 = ox.nearest_nodes(광주시,127.3459, 37.3503) 


route1 =  nx.shortest_path(광주시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(광주시, orig_node2, dest_node2, weight='length')
route3 =  nx.shortest_path(광주시, orig_node3, dest_node3, weight='length')
route_list = [route1,route2,route3]


R1 = ox.folium.plot_route_folium(광주시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(광주시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

R3 = ox.folium.plot_route_folium(광주시, route3, route_map=R2,
                                 tiles='OpenStreetMap',
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1,#라인 투명도
                                 zoom=0.1) 

marker1 = folium.Marker( [ 37.4162, 127.2509 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker2 = folium.Marker( [ 37.4110, 127.2577 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker3 = folium.Marker( [ 37.3557, 127.3354 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker4 = folium.Marker( [ 37.3503, 127.3459 ], icon = folium.Icon(color='blue')).add_to( R3 )

R3


# # 16. 군포

# In[47]:


군포시 = ox.graph_from_place('군포시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(군포시,126.9284, 37.3661)
dest_node1 = ox.nearest_nodes(군포시,126.9316, 37.3577) 

orig_node2 = ox.nearest_nodes(군포시,126.9316, 37.3577) 
dest_node2 = ox.nearest_nodes(군포시,126.9337, 37.3548)

orig_node3 = ox.nearest_nodes(군포시,126.9337, 37.3548) 
dest_node3 = ox.nearest_nodes(군포시,126.9425, 37.3465)


route1 =  nx.shortest_path(군포시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(군포시, orig_node2, dest_node2, weight='length')
route3 =  nx.shortest_path(군포시, orig_node3, dest_node3, weight='length')
route_list = [route1,route2,route3]


R1 = ox.folium.plot_route_folium(군포시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(군포시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

R3 = ox.folium.plot_route_folium(군포시, route3, route_map=R2,
                                 tiles='OpenStreetMap',
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1,#라인 투명도
                                 zoom=0.1) 

marker1 = folium.Marker( [ 37.3661, 126.9284 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker2 = folium.Marker( [ 37.3577, 126.9316 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker3 = folium.Marker( [ 37.3548, 126.9337 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker4 = folium.Marker( [ 37.3465, 126.9425 ], icon = folium.Icon(color='blue')).add_to( R3 )

R3


# # 17. 동두천

# In[49]:


동두천시 = ox.graph_from_place('동두천시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(동두천시,127.0469, 37.9068)
dest_node1 = ox.nearest_nodes(동두천시,127.0581, 37.9040) 

orig_node2 = ox.nearest_nodes(동두천시,127.0581, 37.9040) 
dest_node2 = ox.nearest_nodes(동두천시,127.0575, 37.9149)

route1 =  nx.shortest_path(동두천시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(동두천시, orig_node2, dest_node2, weight='length')
route_list = [route1,route2]


R1 = ox.folium.plot_route_folium(동두천시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(동두천시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

marker1 = folium.Marker( [ 37.9068, 127.0469 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker2 = folium.Marker( [ 37.9040, 127.0581 ], icon = folium.Icon(color='blue')).add_to( R2 )
marker3 = folium.Marker( [ 37.9149, 127.0575 ], icon = folium.Icon(color='blue')).add_to( R2 )

R2


# # 18. 의왕

# In[51]:


의왕시 = ox.graph_from_place('의왕시,경기도, 대한민국', network_type='drive', simplify=False) 

orig_node1 = ox.nearest_nodes(의왕시,126.9735, 37.3488)
dest_node1 = ox.nearest_nodes(의왕시,126.9709, 37.3533) 

orig_node2 = ox.nearest_nodes(의왕시,126.9709, 37.3533) 
dest_node2 = ox.nearest_nodes(의왕시,126.9660, 37.3591)

orig_node3 = ox.nearest_nodes(의왕시,126.9660, 37.3591) 
dest_node3 = ox.nearest_nodes(의왕시,126.9864, 37.4003)


route1 =  nx.shortest_path(의왕시, orig_node1, dest_node1, weight='length')
route2 =  nx.shortest_path(의왕시, orig_node2, dest_node2, weight='length')
route3 =  nx.shortest_path(의왕시, orig_node3, dest_node3, weight='length')
route_list = [route1,route2,route3]


R1 = ox.folium.plot_route_folium(의왕시, route1, route_map=None,   #초기 route_map은 None으로 설정해주어야함 
                                 tiles='OpenStreetMap', #베이스맵
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1) #라인 투명도

R2 = ox.folium.plot_route_folium(의왕시, route2, route_map=R1,
                                 tiles='OpenStreetMap',
                                 color='#910FAB', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1)#라인 투명도

R3 = ox.folium.plot_route_folium(의왕시, route3, route_map=R2,
                                 tiles='OpenStreetMap',
                                 color='#232B99', #엣지 색깔
                                 weight=10, #엣지 굵기
                                 opacity=1,#라인 투명도
                                 zoom=0.1) 

marker1 = folium.Marker( [ 37.3488, 126.9735 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker2 = folium.Marker( [ 37.3533, 126.9709 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker3 = folium.Marker( [ 37.3591, 126.9660 ], icon = folium.Icon(color='blue')).add_to( R3 )
marker4 = folium.Marker( [ 37.4003, 126.9864 ], icon = folium.Icon(color='blue')).add_to( R3 )


R3

