
df1 = pd.read_csv('kin-driver-missense-activating.csv')
################
def clean_row(uniprot_id):
    full_list = uniprot_id.split('_')
    cleaned_id = (full_list[0])
    return(cleaned_id)
###############
def label_kinases(x):
    
    if x == 'CSF1R':
        return(1)
     
    elif x =='DDR1':
        return(2)
    elif x =='EGFR':
        return(3)
    elif x =='EPHA2':
        return(4)
    elif x =='EPHA3':
        return(5)
    elif x =='EPHA7':
        return(6)
    elif x =='EPHB4':
        return(7)
    elif x =='FGFR1':
        return(8)
    elif x =='FGFR2':
        return(9)
    elif x =='FGFR3':
        return(10)
    elif x =='FGFR4':
        return(11)
    elif x =='FLT1':
        return(12)
    elif x =='FLT3':
        return(13)
    elif x =='IGF1R':
        return(14)
    elif x =='INSR':
        return(15)
    elif x =='KDR':
        return(16)
    elif x =='KIT':
        return(17)
    elif x =='MERTK':
        return(18)
    elif x =='MET':
        return(19)
    elif x =='NTRK1':
        return(20)
    elif x =='NTRK2':
        return(21)
    elif x =='NTRK3':
        return(22)
    elif x =='PGFRA':
        return(23)
    elif x =='RET':
        return(24)
    elif x =='TIE2':
        return(25)
##############
def mark_driver_mut(x):
    if x in driver_list:
        return('Y')
    else:
        return('N')
################
protein_list = ['CSF1R','DDR1','EGFR','EPHA2','EPHA3','EPHA7','EPHB4','FGFR1',
'FGFR2','FGFR3','FGFR4','FLT1','FLT3','IGF1R','INSR','KDR','KIT','MERTK',
'MET','NTRK1','NTRK2','NTRK3','PGFRA','RET','TIE2']
####################
df1['protein'] = df1['uniprot_id'].apply(clean_row)
protein_filter = df1['protein'].isin(protein_list)
df2 = df1[protein_filter]
cols = ['uniprot_id','protein','mutation','from_res_n']
df3 = df2[cols]
df4 = df3.astype(str)
df4['model#'] = df4['protein'].apply(label_kinases)
df4['merge'] = df4['model#'].astype(str) + '-' + df4['from_res_n'].astype(str)
driver_list = list(df4['merge'])
#####################
#
#
df_combo = pd.read_csv('combo.csv')
df_combo = df_combo.astype(str)
df_combo['merge'] = df_combo['model_no'] + '-' +df_combo['resno']
######################
df_combo['driver_mut'] = df_combo['merge'].apply(mark_driver_mut)
df_combo.to_csv('combo_with_kindriver_mutations.csv',index=False)