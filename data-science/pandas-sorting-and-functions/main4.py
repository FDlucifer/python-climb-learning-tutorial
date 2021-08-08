import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'SSN': [123, 445, 511, 872],
    'Name': ['Anna', 'John', 'John', 'Mike'],
    'Age': [29, 83, 42, 23],
    'Height': [176, 165, 187, 182],
    'Gender': ['f', 'm', 'm', 'm']
}

df = pd.DataFrame(data)
df.set_index('SSN', inplace=True)

df.sort_index(inplace=True)
print(df)

df.sort_values(by=['Age', 'Name'], inplace=True)
print(df)