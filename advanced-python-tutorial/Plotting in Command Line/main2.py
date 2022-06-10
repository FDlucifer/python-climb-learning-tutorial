# pip install plotext numpy

import plotext
import numpy as np

languages = ["Python", "Java", "C", "Go", "JavaScript"]
votes = [140, 48, 112, 65, 101]

plotext.title("Bar Chart")
plotext.bar(languages, votes)
plotext.show()