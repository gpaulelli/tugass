import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Load the data
df = pd.read_csv('C:/Users/Luxford/Documents/Lesson/MVD/Again.csv', delimiter=';', thousands=',', decimal='.')

def create_bubble_chart(x_col, y_col, radius_col, color_col, radius_scaling, cmap):
    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    sc = ax.scatter(df[x_col], df[y_col], s=df[radius_col]/(100000*radius_scaling), c=df[color_col], cmap=cmap)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title('Bubble Chart')
    return fig

st.title('Bubble Chart')

x_col = st.selectbox('X Axis', list(df.columns), index=list(df.columns).index('GDP per capita'))
y_col = st.selectbox('Y Axis', list(df.columns), index=list(df.columns).index('Life expectancy at birth'))
radius_col = st.selectbox('Radius', list(df.columns), index=list(df.columns).index('Population'))
color_col = st.selectbox('Color', list(df.columns), index=list(df.columns).index('Birth rate'))
radius_scaling = st.slider('Radius Scaling', min_value=0.1, max_value=10.0, value=1.0)

color_map = {'coolwarm': 'Coolwarm', 'viridis': 'Viridis', 'plasma': 'Plasma', 'magma': 'Magma', 'inferno': 'Inferno', 'cividis': 'Cividis'}
color_map_list = list(color_map.keys())
cmap = st.selectbox('Color Map', color_map_list, index=color_map_list.index('coolwarm'))

fig = create_bubble_chart(x_col, y_col, radius_col, color_col, radius_scaling, cmap)
st.pyplot(fig)