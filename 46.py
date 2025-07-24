import numpy as np
import matplotlib.pyplot as pp
import pandas as pd

f1_pan = pd.read_csv("data.csv")
months = f1_pan['Month']
rainfl = f1_pan['Rainfall_mm']

pp.figure(figsize=(15,5))
pp.bar(months, rainfl)
pp.show()