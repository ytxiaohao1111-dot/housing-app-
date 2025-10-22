import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()


# 1. bigTitle and read
st.title('California Housing Data (1990)')

# read data
df = pd.read_csv('housing.csv')

# 2. Price slider
filter = st.slider('Minimal Median House Price:', 0, 500001, 200000) 

# 3. Sidebar filters
loc_col = 'ocean_proximity' if 'ocean_proximity' in df.columns else None
loc_options = sorted(df[loc_col].dropna().unique()) if loc_col else []
loc_selected = st.sidebar.multiselect('Choose the location type', loc_options, default=loc_options)
income_choice = st.sidebar.radio('Choose income level', ('Low (<=2.5)', 'Medium (>2.5 & <=4.5)', 'High (>4.5)'))

# 4. Map requires latitude & longitude columns; try common names
st.subheader('See more filters in the sidebar')
st.map(df)

# 5. Histogram of median_house_value
plt.subplots(figsize=(12,6))# set figure size
sns.histplot(df['median_house_value'].dropna(), bins=30, kde=False, color='tab:blue', edgecolor='w')# draw histogram
plt.grid(axis='y', alpha=0.6)# add grid lines
st.pyplot(plt)

# 6. Show small sample of filtered data
#st.subheader("Sample of filtered data")
#st.dataframe(filtered.head(50))
