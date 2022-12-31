# pip install plotnine matplotlib pandas

import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
from plotnine.data import diamonds

df = diamonds

p = (
    ggplot(df)
    + aes(x="price", y="carat")
    + geom_line()
)

p.draw()
plt.show()