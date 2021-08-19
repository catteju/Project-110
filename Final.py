import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as s
import random
import pandas as pd

df = pd.read_csv("Data.csv")
data = df["readingTime"].tolist()

fig = ff.create_distplot([data],["readingTime"], show_hist= False)
fig.show()

populationMean = s.mean(data)
print("Population Mean", populationMean)
populationStd = s.stdev(data)
print("Standard Deviation Of Population Mean", populationStd)

def randomSamples(counter):
    dataSet = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data))
        value = data[randomIndex]
        dataSet.append(value)
    mean = s.mean(dataSet)
    return mean

def showFigure(meanList):
    df = meanList
    fig1 = ff.create_distplot([df],["readingTime"], show_hist= False)
    fig1.show()

def main():
    meanList = []
    for i in range(0,100):
        setOfMeans = randomSamples(30)
        meanList.append(setOfMeans)
    showFigure(meanList)
    print("Sampling Mean",s.mean(meanList))
    data2 = s.stdev(meanList)
    print("Standard Deviation Of Smapling Distribution", data2)

main()