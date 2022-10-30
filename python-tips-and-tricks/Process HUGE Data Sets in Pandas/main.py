import pandas as pd

counter = 0
metric_results = pd.Series([], dtype="float64")

for chunk in pd.read_csv("huge_dataset.csv", chunksize=1000):
    chunk.columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
    metric_results = pd.concat([metric_results, chunk.E / chunk.G])
    counter += 1
    if counter == 20:
        break

print(metric_results)