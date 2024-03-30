import pandas as pd
import matplotlib.pyplot as plt

series = pd.Series([10, 'i am a string', 30, 40], ['A', 'B', 'C', 'D'])

s1 = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
s2 = pd.Series([7, 5, 1, 2], ['c', 'b', 'a', 'd'])

def mysquare(x):
    return x ** 2

s2.sort_values(inplace=True)
print(s2)