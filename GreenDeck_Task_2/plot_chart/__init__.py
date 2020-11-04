import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def plot_chart(a,b,s_id):
    df= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{s_id}/export?format=csv")
    l=[]
    l.append(a)
    l.append(b)
    #print(type(l))
    x1=df[l[0]]
    x1=list(x1)
    #print("X1= ",type(x1))
    y1=df[l[1]]
    y1=list(y1)
    #print("Y1= ",type(y1))
    x=[]
    y=[]
    
    for i in x1:
        x.append(i)
    for j in y1:
        y.append(j)
    #print(x,y)
    #print("X Type = ",type(x))
    plt.plot(x,y,'g')
    plt.show()
    
