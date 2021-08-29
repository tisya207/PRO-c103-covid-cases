import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')
fig= px.scatter(df, x='date', y='cases', color='country', title='covid-19 cases', size_max=30)
fig.show()