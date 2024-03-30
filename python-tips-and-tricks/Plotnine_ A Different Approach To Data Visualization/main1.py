# pip install plotnine matplotlib pandas

import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
from plotnine.data import diamonds

df = pd.DataFrame({
    "x": [1,2,3,4,5,6,7,8,9],
    "y": [1,2,1.5,3,2.5,3.5,2.5,3.5,4],
    "group": ["A", "A", "A", "B", "B", "B", "C", "C", "C"]
})

p = (
    ggplot(df) +
    aes(x="x", y="y") +
    geom_point() +
    facet_wrap("group")
)

p.draw()
plt.show()