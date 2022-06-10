# pip install plotext numpy

import plotext
import numpy as np

student_ages = np.random.normal(14,5,100)
worker_ages = np.random.normal(40,20,100)
guru_ages = np.random.normal(80,10,100)

plotext.hist(student_ages, bins=40, label="Student")
plotext.hist(worker_ages, bins=40, label="Worker")
plotext.hist(guru_ages, bins=40, label="Guru")
plotext.show()