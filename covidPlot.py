import pandas as pd 
import plotly.express as px

df = pd.read_csv('covid_data.csv')
fig = px.scatter(df, x = 'Date', y = 'Cases', color = 'Country', title = 'Covid-19 Cases Scatter Plot')
fig.show()