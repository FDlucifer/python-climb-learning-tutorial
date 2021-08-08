import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'SSN': [123, 445, 511, 872],
    'Name': ['Anna', 'Bob', 'John', 'Mike'],
    'Age': [29, 43, 82, 23],
    'Height': [176, 165, 187, 182],
    'Gender': ['f', 'm', 'm', 'm']
}

df = pd.DataFrame(data)
df.set_index('SSN', inplace=True)

for key, value in df.iteritems():
    print("{}: {}".format(key, value))