import pandas as pd
import matplotlib.pyplot as plt

series = pd.Series(['A', 'B', 'C', 'D'], index=[10, 'i am a string', 30, 40])
series.name = "MySeries"

print(series)