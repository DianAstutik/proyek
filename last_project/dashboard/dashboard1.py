import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st 
import sys
import pathlib


code_dir = pathlib.Path(__file__).parent.resolve()
files_location = code_dir / ".." / "dashboard" / "df.csv"  
files_location = files_location.resolve()  

#dataframe
dt = pd.read_csv(files_location)

#sidebar
with st.sidebar:
    st.write(
        """
        Nama : Ni Putu Dian Astutik\n
        Email : dianastutik03@gmail.com\n
        ID Dicoding : dian_astutik
        """
    )

st.header("Proyek Analisis Data: Air Quality Dataset")

st.subheader("Air Quality Trend")
fig, ax  = plt.subplots(figsize=(16,8))
ax.plot(
    dt.groupby(by="year")["CO"].mean().sort_index(ascending=True),
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.set_title("Beijing Air Quality (CO)", loc="center", fontsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.subheader("Carbondioxide/hour")
fig, ax  = plt.subplots(figsize=(16,8))
ax.plot(
    dt.groupby(by="hour")["CO"].mean().sort_index(ascending=True),
    marker='o', 
    linewidth=2,
    color="#990000"
)
ax.set_title("Beijing Air Quality (CO/hour)", loc="center", fontsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.subheader("Beijing District with Average Carbondioxide")
fig, ax  = plt.subplots(figsize=(16,8))
colors_ = ["#660000", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", 
           "#D3D3D3", "#D3D3D3", "#D3D3D3"]
ax.barh(
    dt.groupby("station")["CO"].mean().sort_values().index,
    dt.groupby("station")["CO"].mean().sort_values(),
    color = colors_
)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title("Average Beijing Air Quality (CO/station)", loc="center", fontsize=20)
ax.tick_params(axis ='y', labelsize=15)
st.pyplot(fig)
