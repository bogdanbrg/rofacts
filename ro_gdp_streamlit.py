import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import wbgapi as wb

#Get Romanian GDP + other indicators here: https://data.worldbank.org/country/RO

df_gdp =wb.data.DataFrame('NY.GDP.MKTP.CD', 'ROU', range(1990,2023))
# Transpose DataFrame while keeping the index as columns
df_gdp_transposed = df_gdp.T.reset_index()

# Rename the columns
df_gdp_transposed.columns = ['year', 'GDP_amount']

# Print the transposed DataFrame
print(df_gdp_transposed)

#remove "YR"

df_gdp_transposed['year'] = df_gdp_transposed['year'].str.replace('YR', '')
df_gdp_transposed

#convert year to datetime

print(df_gdp_transposed['year'].dtypes)

# Convert the 'year' column to datetime
df_gdp_transposed['year'] = pd.to_datetime(df_gdp_transposed['year'], format='%Y')

# Check the data type after conversion
print(df_gdp_transposed['year'].dtypes)

print(df_gdp_transposed['GDP_amount'].dtypes)

# Define background color
color_background = 'rgb(253,241,230)'

fig = go.Figure()

df_gdp = df_gdp_transposed

# Add a line trace for GDP
fig.add_trace(go.Scatter(x=df_gdp['year'], y=df_gdp['GDP_amount'],
                         mode='lines+markers',
                         name='GDP_amount'))

# Update layout
fig.update_layout(
    title='GDP Evolution Over the Years',
    xaxis_title='Year',
    yaxis_title='GDP Amount ($bn)',
    plot_bgcolor=color_background,
    paper_bgcolor=color_background
)

# Show the plot
fig.show()

