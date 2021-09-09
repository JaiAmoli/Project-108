import csv 
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv")
figure = ff.create_distplot([df["Avg Rating"].tolist()],["AverageRating"])
figure.show()