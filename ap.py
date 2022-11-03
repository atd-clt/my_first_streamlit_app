import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.title ("Abey T. Dessie - DSBA 5122")
st.header('Homework 1')

st.subheader('Question 1')

x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0, 100, 1)

# Create a random array of data that we will use for our y values
y_data = np.random.uniform(low=0.1, high=0.9, size=(100,))

df = pd.DataFrame({'x': x_axis,'y': y_data})

st.write(df)

st.subheader('Question 2')

scatter = alt.Chart(df).mark_point().encode(x='x',y='y')
st.altair_chart(scatter, use_container_width=True)

st.subheader('Question 3')

scatter = alt.Chart(df, title="Scatter Plot Demonstration").mark_point().encode(x='x',y='y', color='y', size = 'x').configure_axis(
    labelFontSize=16,titleFontSize=16).configure_title(fontSize=28).configure(background='#DDEEFF')
st.altair_chart(scatter, use_container_width=True)

st.markdown("""
The 5 changes I made were:
- Change 1: Added a title to the scatterplot   
- Change 2: Adjusted color to correspond to y-axis values 
- Change 3: Adjusted size to correspond to y-axis values
- Change 4: Adjusted font size for axis labels & chart title  
- Change 5: Adjusted background color of scatter plot
""")

st.subheader('Question 4 - HW Example')

source = pd.read_json('imdb.json')
st.write(source)

bar = alt.Chart(source).mark_bar(color='#03cffc').encode(
    alt.X("IMDB_Rating:Q", bin=True, title="IMDB Rating"),
    alt.Y('count()',title="Records")
)

st.altair_chart(bar, use_container_width=True)
