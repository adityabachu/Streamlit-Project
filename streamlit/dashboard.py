import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

data = pd.read_csv("Screentime.csv")
st.title("Screen Time Analysis")
st.header("Data :")
st.dataframe(data.head())

st.header("Descriptive statistics of the data :")
st.dataframe(data.describe())

st.header("Let's look at the amount of usage of apps :")

figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Usage", 
                color="App", 
                title="Usage")

st.plotly_chart(figure)

st.header("Now let’s have a look at the number of notifications from the apps :")

figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Notifications", 
                color="App", 
                title="Notifications")

st.plotly_chart(figure)

st.header("Now let’s have a look at the number of times the apps opened :")

figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Times opened", 
                color="App",
                title="Times Opened")

st.plotly_chart(figure)

