#with WB API data

import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import wbgapi as wb

st.set_page_config(page_title = "Economic and Social indicators", page_icon = ":bar_chart:", layout="wide")

st.title(":bar_chart: Romania indicators merge sau nu?")

# Get unemployment data from wb    
df_unemployment =wb.data.DataFrame('SL.UEM.TOTL.NE.ZS', 'ROU', range(1994,2023))

# Transpose DataFrame while keeping the index as columns
df_unemployment_transposed = df_unemployment.T.reset_index()

# Rename the columns
df_unemployment_transposed.columns = ['year', 'unemployment rate']

# Transpose DataFrame

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


##############################Get Romanian GDP + other indicators here: https://data.worldbank.org/country/RO

df_gdp =wb.data.DataFrame('NY.GDP.MKTP.CD', 'ROU', range(1990,2023))
# Transpose DataFrame while keeping the index as columns
df_gdp_transposed = df_gdp.T.reset_index()

# Rename the columns
df_gdp_transposed.columns = ['year', 'GDP_amount']


#remove "YR"

df_gdp_transposed['year'] = df_gdp_transposed['year'].str.replace('YR', '')


# Convert the 'year' column to datetime
df_gdp_transposed['year'] = pd.to_datetime(df_gdp_transposed['year'], format='%Y')


# Define background color
color_background = 'rgb(253,241,230)'

fig_gdp = go.Figure()

df_gdp = df_gdp_transposed

# Add a line trace for GDP
fig_gdp.add_trace(go.Scatter(x=df_gdp['year'], y=df_gdp['GDP_amount'],
                         mode='lines+markers',
                         name='GDP_amount'))

# Update layout
fig_gdp.update_layout(
    title='GDP Evolution Over the Years',
    xaxis_title='Year',
    yaxis_title='GDP Amount ($bn)',
    plot_bgcolor=color_background,
    paper_bgcolor=color_background
)

############## INFLATION #################


df_inflation =wb.data.DataFrame('FP.CPI.TOTL.ZG', 'ROU', range(1991,2023))

# transpose the data

# Transpose DataFrame while keeping the index as columns
df_inflation_transposed = df_inflation.T.reset_index()

# Rename the columns
df_inflation_transposed.columns = ['year', 'inflation %']

df_inflation_transposed['year'] = df_inflation_transposed['year'].str.replace('YR', '')


# Define background color

df_inflation = df_inflation_transposed
color_background = 'rgb(253,241,230)'

fig_inflation = go.Figure()

# Add a line trace for GDP
fig_inflation.add_trace(go.Scatter(x=df_inflation['year'], y=df_inflation['inflation %'],
                         mode='lines+markers',
                         name='inflation (%)'))

# Update layout
fig_inflation.update_layout(
    title='Inflation Evolution Over the Years',
    xaxis_title='Year',
    yaxis_title='Inflation (%)',
    plot_bgcolor=color_background,
    paper_bgcolor=color_background
)

# Show the plot

#st.plotly_chart(fig_gdp)

col1,col2 = st.columns(2, gap = "small")

with col1:
    st.plotly_chart(fig_gdp)
    st.plotly_chart(fig)
    
with col2:
    st.plotly_chart(fig_inflation)




