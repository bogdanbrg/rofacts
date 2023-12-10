import streamlit as st
from streamlit_gsheets import GSheetsConnection
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


st.set_page_config(page_title = "Rofacts", page_icon = ":bar_chart:", layout="wide")

st.title(":bar_chart: Romania indicators")

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()


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