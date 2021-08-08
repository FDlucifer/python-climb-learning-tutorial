import pandas as pd
import matplotlib.pyplot as plt

s1 = pd.Series([1,2,3,4,7,5,2,1], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

s1.to_csv('myseries.csv')