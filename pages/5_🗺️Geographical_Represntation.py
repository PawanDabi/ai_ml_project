
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Geographical Map",
    page_icon="https://cdn-icons-png.flaticon.com/512/3090/3090011.png",
    layout="wide",
    initial_sidebar_state="expanded"
)
hide_menu = """
    <style>
    #MainMenu{
        visibility:hidden;
    }
    footer{
        visibility:hidden;
    }
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
st.sidebar.markdown(" ")
st.markdown("""
    <h1 style='text-align: center;'>Map:
        <span style='color: red;'>Geographical Representation</span>
        </h1>""",
    unsafe_allow_html=True
)
st.markdown("---")
st.sidebar.markdown("")
file_path = "update_1_geograph.csv"
data = pd.read_csv(file_path, usecols=['Latitude', 'Longitude', 'State Name'])
map_center = [data['Latitude'].mean(), data['Longitude'].mean()]
world_map = folium.Map(location=map_center, zoom_start=2)
for _, row in data.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['State Name'],  # Show state name on click
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(world_map)

st_data = st_folium(world_map, width=1000, height=500)
