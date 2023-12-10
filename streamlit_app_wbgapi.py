#with WB API data

import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import wbgapi as wb

st.set_page_config(page_title = "Economic and Social indicators", page_icon = ":bar_chart:", layout="wide")

st.title(":bar_chart: Romania indicators")

     
df_unemployment =wb.data.DataFrame('SL.UEM.TOTL.NE.ZS', 'ROU', range(1994,2023))
# transpose the data

# Transpose DataFrame while keeping the index as columns
df_unemployment_transposed = df_unemployment.T.reset_index()

# Rename the columns
df_unemployment_transposed.columns = ['year', 'unemployment rate']

# Print the transposed DataFrame

df_unemployment_transposed['year'] = df_unemployment_transposed['year'].str.replace('YR', '')

# Define background color

df = df_unemployment_transposed
color_background = 'rgb(253,241,230)'

fig = go.Figure()

# Add a line trace for GDP
fig.add_trace(go.Scatter(x=df['year'], y=df['unemployment rate'],
                         mode='lines+markers',
                         name='Unemployment_rate (%)'))

# Update layout
fig.update_layout(
    title='Unemployment Evolution Over the Years',
    xaxis_title='Year',
    yaxis_title='Unemployment (%)',
    plot_bgcolor=color_background,
    paper_bgcolor=color_background
)

# Show the plot

st.plotly_chart(fig)
