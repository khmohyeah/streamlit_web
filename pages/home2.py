import folium

# 위도
latitude = 37.394946
# 경도
longitude = 127.111104

myMap = folium.Map(location=[latitude, longitude], zoom_start=12                   , width=750, height=500)

folium.Marker([latitude, longitude],
  popup="판교역",
  tooltip="판교역 입구",
  color='tomato',
  radius = 50, 
  icon=folium.Icon(color='red', icon='star')).add_to(myMap)

folium.CircleMarker([latitude, longitude],
  radius=100,
  color='blue',
  fill_color='skyblue').add_to(myMap)

myMap
