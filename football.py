import numpy as np 
import pandas as pd 
import os
import streamlit as st
fields = pd.read_csv('football-match-winners.csv')

# Streamlit app title
st.title('Class Participation - 1')

# Display the dataset
st.write('## Raw Data')
st.dataframe(fields)

# Basic statistics about the dataset
st.write('## Summary Statistics')
st.write(fields.describe())

# Bar chart using value counts of a column
selected_column = st.selectbox('Select a column for value counts:', fields.columns)
value_counts = fields['Experience'].value_counts()
st.bar_chart(value_counts)

# Line chart example
st.write('## Line Chart Example')
st.line_chart(value_counts)

# Show a sample of the data
st.write('## Sample Data')
sample_size = st.slider('Select sample size:', 1, len(fields), 5)
st.write(fields.sample(sample_size))