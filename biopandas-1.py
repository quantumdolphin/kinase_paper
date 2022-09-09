from biopandas.pdb import PandasPdb
import pandas as pd
df0 =PandasPdb().read_pdb(r'../test.pdb')
kinases_set = ['CSF1R','DDR1','EGFR','EPHA2','EPHA3','EPHA7','EPHB4','FGFR1','FGFR2',
'FGFR3','FGFR4','FLT1','FLT3','IGF1R','INSR','KDR','KIT','MERTK',
'MET','NTRK1','NTRK2','NTRK3','PGFRA','RET','TIE2']
zipped = zip(list_of_nos,kinases_set)
pdb_range = [* range(1,26,1)] # * is unpacking operator
pdb_dict = dict(zip(pdb_range,pdb_name_list))
############
alpha_carbons = df0.df['ATOM'][(df0.df['ATOM']['atom_name'] == 'CA')]
residue_no_series = alpha_carbons['residue_number']
a = residue_no_series.values
chain_ids = df0.df['ATOM']['chain_id']
divisor = len(set(chain_ids))
jm_temp = ((657 < a) & (a < 724)).sum() #TM_END:657 KINASE_START:724
print(jm_temp)
jm_res = jm_temp/divisor
print(jm_res)
jm_list.append(jm_res)
print('#####')