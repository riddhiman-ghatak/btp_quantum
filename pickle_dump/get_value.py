import numpy as np
import pandas as pd
import pickle
from scipy.interpolate import splrep, splev


def get_Y1(x):
    with open('spline_Y1.pkl', 'rb') as f:
        tck1 = pickle.load(f)
    return splev(x, tck1)

def get_Y2(x):
    with open('spline_Y2.pkl', 'rb') as f:
        tck2 = pickle.load(f)
    return splev(x, tck2)

def get_Y3(x):
    with open('spline_Y3.pkl', 'rb') as f:
        tck3 = pickle.load(f)
    return splev(x, tck3)

# Example Usage
x_test = 5 

print(get_Y1(x_test))
print(get_Y2(x_test))
print(get_Y3(x_test))