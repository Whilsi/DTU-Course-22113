import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

df = pd.read_csv('pathogen_abundance.tab',sep='\t')

fig,ax=plt.subplots(figsize=(10,5))
sns.barplot(data=df.sort_values('#clr_value').tail(n=15),x='#clr_value',y='#name')
ax.set_position([0.3,0.1,0.65,0.8])
plt.xlabel('CLR')
plt.ylabel('Species')
plt.title('Species with highest CLR values (n=15)')
plt.show()