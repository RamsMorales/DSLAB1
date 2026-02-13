import streamlit as st
import plotly.express as px
import pandas as pd


df = pd.read_csv("data/oct25-2024.csv")


tab1,tab2,tab3 = st.tabs(["Quick Views","Raw Data","EDA"])

with tab1:
    st.subheader("Histograms")
    st.divider()

    feature = st.selectbox("Which feature would you like to view? ",[x for x in df.columns if x not in ["Latitude","Longitude","Date","Time"]])

    #st.caption(feature)
    fig1 = px.box(x=df[feature])
    st.plotly_chart(fig1)

