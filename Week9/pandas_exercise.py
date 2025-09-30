import pandas as pd
import numpy as np

BE_ids_df = pd.read_csv('pandas_exercise/BE_ids.txt',sep='\t',skiprows=2,index_col=0)
BE_ids_df['country'] = 'Belgium'
DK_ids_df = pd.read_csv('pandas_exercise/DK_ids.txt',sep='\t',skiprows=2,index_col=0)
DK_ids_df['country'] = 'Denmark'
DE_ids_df = pd.read_csv('pandas_exercise/DE_ids.txt',sep='\t',skiprows=2,index_col=0)
DE_ids_df['country'] = 'Germany'
UK_ids_df = pd.read_csv('pandas_exercise/UK_ids.txt',sep=',',skiprows=3,index_col=0)
UK_ids_df['country'] = 'UK'
USA_ids_df = pd.read_csv('pandas_exercise/USA_ids.txt',sep=',',skiprows=3,index_col=0)
USA_ids_df['country'] = 'USA'

ids_df = pd.concat([BE_ids_df,DK_ids_df,DE_ids_df,UK_ids_df,USA_ids_df])

No_clinical = len(ids_df[ids_df['Origin']=='Clinical'])
No_surveillance = len(ids_df[ids_df['Origin']=='Surveillance'])

BElab_results_df = pd.read_csv('pandas_exercise/BElab_results.txt',sep='\t',skiprows=1)
BElab_results_df['country'] = 'Belgium'
DElab_results_df = pd.read_csv('pandas_exercise/DElab_results.txt',sep='\t',skiprows=1)
DElab_results_df['country'] = 'Germany'
DKlab_results_df = pd.read_csv('pandas_exercise/DKlab_results.txt',sep='\t',skiprows=1)
DKlab_results_df['country'] = 'Denmark'
UKlab_results_df = pd.read_csv('pandas_exercise/UKlab_results.txt',sep=',',skiprows=1)
UKlab_results_df['country'] = 'UK'

for key in UKlab_results_df.keys():
    if key == 'sample_ID' or 'country':
        continue
    UKlab_results_df[key] = pd.to_numeric(UKlab_results_df[key].str.replace('MIC: ','').str.replace('<',''))

USAlab_results_df = pd.read_csv('pandas_exercise/USAlab_results.txt',sep=',',skiprows=1,)
USAlab_results_df['country'] = 'USA'

for key in USAlab_results_df.keys():
    if key == 'sample_ID' or 'country':
        continue
    USAlab_results_df[key] = pd.to_numeric(USAlab_results_df[key].str.replace('MIC: ',''))

results_df = pd.concat([BElab_results_df,DElab_results_df,DKlab_results_df,UKlab_results_df,USAlab_results_df])

BEbioinf_results_df = pd.read_csv('pandas_exercise/BEbioinf_results.txt',sep='\t',skiprows=1)
BEbioinf_results_df['country'] = 'Belgium'
DKbioinf_results_df = pd.read_csv('pandas_exercise/DKbioinf_results.txt',sep='\t',skiprows=1)
DKbioinf_results_df['country'] = 'Denmark'
DEbioinf_results_df = pd.read_csv('pandas_exercise/DEbioinf_results.txt',sep='\t',skiprows=1)
DEbioinf_results_df['country'] = 'Germany'
UKbioinf_results_df = pd.read_csv('pandas_exercise/UKbioinf_results.txt',sep=',',skiprows=2)
UKbioinf_results_df['country'] = 'UK'
USAbioinf_results_df = pd.read_csv('pandas_exercise/USAbioinf_results.txt',sep=',',skiprows=2)
USAbioinf_results_df['country'] = 'USA'

bioinf_results_df = pd.concat([BEbioinf_results_df,DEbioinf_results_df,DKbioinf_results_df,UKbioinf_results_df,USAbioinf_results_df])

complete_df = ids_df.merge(results_df,on=['sample_ID','country']).merge(bioinf_results_df,on=['reads_ID','country'],suffixes=(None,'_bioinfo'))

NaN_columns = complete_df.columns[complete_df[complete_df['country'] == 'USA'].isna().all()].tolist()

i = 0
while i < len(NaN_columns):
    if '_bioinfo' in NaN_columns[i]:
        NaN_columns.pop(i)
    else:
        i += 1 

complete_df[complete_df['country'] == 'USA'][ids_df.columns.tolist() + NaN_columns].to_csv('resfinder_project.tsv',sep = '\t',index=False)
