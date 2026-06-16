import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st

import pandas as pd

import plotly.express as px

st.set_page_config(page_title="Population Dashboard", layout="wide")

st.title(" Population & GDP Analysis Dashboard")

file=st.file_uploader("population.txt", type=["txt"])

if file:
    df=pd.read_csv(file)

    st.subheader("Dataset Overview")

    st.dataframe(df.head())
    
#---Country filter---

    country=st.selectbox("Select Country", df ['Country'].unique())

    country_df = df [df['Country'] == country]
#---Population trend---
    fig1=px.line (country_df, x='Year', y='Population', title=f"Population Growth-{country}")
    st.plotly_chart (fig1, use_container_width=True)

#---GDP trend---

    fig2=px.line (country_df, x='Year', y='GDP', title=f"GDP Growth-{country}")
    st.plotly_chart (fig2, use_container_width=True)

#---latest comparison---
     
    latest_year=df['Year'].max()
    latest_df=df[df['Year']==latest_year]
    fig3=px.bar(latest_df.sort_values(by='Population',ascending=False).head(10),x='Country',y='Population',title=f'Top 10 populated countries in{latest_year}')
    st.plotly_chart(fig3,use_container_width=True)

# --- Top 10 Countries by GDP Share ---
    st.subheader("Global GDP Distribution")

# Latest year data-vathaan ingeyum use panrom
top_10_gdp = latest_df.sort_values(by='GDP', ascending=False).head(10)

fig4 = px.pie(top_10_gdp, values='GDP', names='Country', title=f"Top 10 Countries by GDP Share ({latest_year})",hole=0.4) 
st.plotly_chart(fig4, use_container_width=True)