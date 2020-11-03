import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# https://docs.google.com/spreadsheets/d/
# 1jbcRvatx1DmtxWWwC7dcEwSyYOAxD0iFICGN33JoUSk
# /edit?usp=sharing

#sheet_id = '1jbcRvatx1DmtxWWwC7dcEwSyYOAxD0iFICGN33JoUSk'

#df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
x=[]
y=[]
l=[]
_id=[]

def sheet_id(s_id):
    _id.append(s_id)
	df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{s_id}/export?format=csv")
	return df


def sec_col(a,b):
    l.append(a)
    l.append(b)
    print(type(l))
    x1=df[l[0]]
    y1=df[l[1]]
    for i in x1:
        x.append(i)
    for i in y1:
        y.append(i)


def plot_chart(x,y):
    print(x,y)
    plt.plot(x,y,'g')
    plt.show()

