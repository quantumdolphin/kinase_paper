from biopandas.pdb import PandasPdb
import pandas as pd
##########
df1 =PandasPdb().read_pdb(r'../structures-01-sep-22/CSF1R-3krj.pdb')
alpha_carbons = df0.df['ATOM'][(df0.df['ATOM']['atom_name'] == 'CA')]
residue_no_series = alpha_carbons['residue_number']
a = residue_no_series.values
###########
import pickle
pickle_off = open ('resno_1.pkl', "rb")
resno_1 = pickle.load(pickle_off)
