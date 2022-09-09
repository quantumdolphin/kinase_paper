import os
import copy
import re
import pandas as pd
###############
def extract_resno(x):
    res = re.findall(r'\d+', x)
    resno = ' '.join(res)
    return resno
#############
def mutation(x):
    mut = x[-1]
    return mut
##############
def org(x):
    org = x[2]
    return org
###########
all = os.listdir()
for i in all:
    if i.endswith('.tsv'):
        print(i)
############
fname = input('please enter name of tsv file : ')
outfile = input('please enter name of output file : ')
#############
df = pd.read_csv(fname,sep='\t')
filter1 = (df['Type'] == 'Substitution - Missense')
df1 = df.loc[filter1] 
df2 = copy.deepcopy(df1)
#########
df2['resno'] = df2['AA Mutation'].apply(extract_resno)
df2['mut_res'] = df2['AA Mutation'].apply(mutation)
df2['org_res'] = df2['AA Mutation'].apply(org)
##########
df3 = df2[['Legacy Mutation ID', 'resno','org_res','mut_res','Count']]
output1 = outfile +'.csv'
df3.to_csv(output1,index=None)
######
output2 = outfile + 'resno_based_counts.csv'
df3.groupby(['resno'])['Count'].sum().to_csv(output2)