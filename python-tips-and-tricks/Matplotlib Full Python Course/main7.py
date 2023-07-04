# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
income = [55, 56, 62, 61, 72, 72, 73, 75]

income_ticks = list(range(50, 81, 2))

plt.plot(years, income)
plt.title("income of john (in usd)", fontsize=30, fontname="FreeSerif")
plt.xlabel("year")
plt.ylabel("yearly income in usd")
plt.yticks(income_ticks, [f"${x}k" for x in income_ticks])

plt.show()
