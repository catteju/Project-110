import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as s
import random
import pandas as pd

df = pd.read_csv("Data.csv")
data = df["readingScore"].tolist()

mean = sum(data)/len(data)
median = s.median(data)
mode = s.mode(data)
std = s.stdev(data)

first_std_start, first_std_end = mean - std, mean + std 
second_std_start, second_std_end = mean - (2*std), mean + (2*std)
third_std_start, third_std_end = mean - (3*std), mean + (3*std)

fig = ff.create_distplot([data],["readingScore"], show_hist= False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,2], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_std_start, first_std_start], y = [0,2], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [first_std_end, first_std_end], y = [0,2], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [second_std_start, second_std_start], y = [0,2], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [second_std_end, second_std_end], y = [0,2], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [third_std_start, third_std_start], y = [0,2], mode = "lines", name = "STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x = [third_std_end, third_std_end], y = [0,2], mode = "lines", name = "STANDARD DEVIATION 3"))

fig.show()

std1 = [result for result in data if result > first_std_start and result < first_std_end]
std2 = [result for result in data if result > second_std_start and result < second_std_end]
std3 = [result for result in data if result > third_std_start and result < third_std_end]
per1 = (len(std1) * 100.0) / len(data)
per2 = (len(std2) * 100.0) / len(data)
per3 = (len(std3) * 100.0) / len(data)


print("MEAN ", mean)
print("MEDIAN ", median)
print("MODE ", mode)
print("STANDARD DEVIATION", std)
print("PERCENTAGE OF DATA WITHIN FIRST STANDARD DEVIATION", per1) 
print("PERCENTAGE OF DATA WITHIN SECOND STANDARD DEVIATION", per2) 
print("PERCENTAGE OF DATA WITHIN THIRD STANDARD DEVIATION", per3) 