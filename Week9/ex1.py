import pandas as pd

BE_ids_df = pd.read_csv('pandas_exercise/BE_ids.txt',sep='\t',skiprows=2,index_col=0)
BE_ids_df['Country'] = 'Belgium'
DK_ids_df = pd.read_csv('pandas_exercise/DK_ids.txt',sep='\t',skiprows=2,index_col=0)
DK_ids_df['Country'] = 'Denmark'
DE_ids_df = pd.read_csv('pandas_exercise/DE_ids.txt',sep='\t',skiprows=2,index_col=0)
DE_ids_df['Country'] = 'Germany'
UK_ids_df = pd.read_csv('pandas_exercise/UK_ids.txt',sep=',',skiprows=3,index_col=0)
UK_ids_df['Country'] = 'UK'
USA_ids_df = pd.read_csv('pandas_exercise/USA_ids.txt',sep=',',skiprows=3,index_col=0)
USA_ids_df['Country'] = 'USA'

final_df = pd.concat([BE_ids_df,DK_ids_df,DE_ids_df,UK_ids_df,USA_ids_df])

print(final_df.groupby('Origin').count())

print(len(final_df[final_df['Origin']=='Clinical']))