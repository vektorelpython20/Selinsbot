import pandas as pd
veri =  pd.read_csv(r"Pandas\turkey_covid19_all.csv")
import matplotlib.pyplot as plt
plt.plot(veri.Confirmed,veri.index)
plt.show()
