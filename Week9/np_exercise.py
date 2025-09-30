import numpy as np

gene_expression1 = np.loadtxt('pandas_exercise/gene_expression1.txt',delimiter=',')
gene_expression2 = np.loadtxt('pandas_exercise/gene_expression2.txt',delimiter=',').transpose()

gene_expression1_norm = gene_expression1-gene_expression1.mean(axis=1).reshape(10,1)
gene_expression2_norm = gene_expression2-gene_expression2.mean(axis=1).reshape(10,1)

normalized_array = np.hstack((gene_expression1_norm,gene_expression2_norm))
print(normalized_array.shape)
np.savetxt('normalized_array.npy',normalized_array,delimiter=',')