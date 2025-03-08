import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv("C:/Users/SATHISH KUMAR/Desktop/HUMAN/final/output_file.csv") 
st.title('Industrial Human Resource Geo-Visualization')
fig = px.bar(df, x='Region', y='Total_Workers', title='Total Workers by Region')
st.plotly_chart(fig)
industry_dist = df['Industry_Group'].value_counts()
fig2 = px.pie(names=industry_dist.index, values=industry_dist.values, title='Industry Group Distribution')
st.plotly_chart(fig2)
fig3 = px.bar(df, x='State', y='Total_Workers', title='Total Workers by State')
st.plotly_chart(fig3)
fig4 = px.bar(df, x='District', y='Total_Workers', title='Total Workers by District')
st.plotly_chart(fig4)
fig5= px.bar(df, x=('Urban_Males','Urban_Females','Rural_Males','Rural_Females'), y='Total_Workers', title='Total Workers by Males-Females')
st.plotly_chart(fig5)