'''
map_dashboard.py
'''
import streamlit as st
import streamlit_folium as sf
import folium
import pandas as pd
import geopandas as gpd
# these constants should help you get the map to look better
# you need to figure out where to use them
CUSE = (43.0481, -76.1474)  # center of map
ZOOM = 14                   # zoom level
VMIN = 1000                 # min value for color scale
VMAX = 5000                 # max value for color scale

map = folium.Map(location = CUSE, zoom_start = ZOOM)
df = pd.read_csv("./cache/top_locations_mappable.csv")
geo_df = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df.lon, df.lat))
geo_df.explore(m = map, marker_type = "circle", marker_kwds = {"radius" : 10, "fill" : True}, vmin = VMIN, vmax = VMAX, column = "amount", cmap = "magma", legend = True)
sf.folium_static(map)