# pip install kaggle

import kaggle

kaggle.api.authenticate()

print(kaggle.api.dataset_list_files("shubhambathwal/flight-price-predicton").files)

kaggle.api.dataset_download_files(
    "shubhambathwal/flight-price-predicton", path=".", unzip=True
)

kaggle.api.dataset_metadata("shubhambathwal/flight-price-predicton", path=".")

datasets = kaggle.api.dataset_list(search="flight price")
print(datasets)
