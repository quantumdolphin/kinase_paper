df1 = pd.read_csv('CSF1R-resno_based_counts.csv')
df1.insert(2, "protein", "CSF1R")
# list1 contains list of residues present in the reprenstative pdb structure of csflr
protein_filter_1 = df1['resno'].isin(list_1)
df1_1 = df1[protein_filter_1]