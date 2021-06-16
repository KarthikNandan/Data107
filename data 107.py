import pandas as pd
import csv
import plotly.graph_objects as go
import plotly
df = pd.read_csv("C:/Users/Somisetty Karthik/Dropbox/My PC (LAPTOP-PJB0FTAK)/Downloads/data107.csv")
student_df = df.loc[df['student_id'] == "TRL_xsl"]
print(student_df.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(
    x = student_df.groupby("level")["attempt"].mean(),
    y = ['Level 1','Level 2', 'Level 3', 'Level 4'],
    orientation = 'h'
))
plotly.offline.plot(fig)