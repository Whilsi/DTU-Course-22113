import pandas as pd
import numpy as np
from scipy.stats import linregress

data = pd.read_csv('gene_combined.txt',sep='\t',header=None,names=['x','y'])
genes = set(data.index)

best_gene = None
best_r_val = 0

for gene in genes:
    slope,inter,r_val,p_val,err = linregress(data.loc[gene]['x'],data.loc[gene]['y'])
    print(gene,r_val)
    if abs(r_val) > abs(best_r_val):
        best_r_val = r_val
        best_gene = gene

print(best_gene)