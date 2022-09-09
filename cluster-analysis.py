df1 = pd.read_csv('xyz_hc_clust.csv')
counts = df1.groupby('clust_xyz').Count.agg(['max', 'min', 'count'])
df_count = pd.DataFrame(counts)
#####
sum_per_cluster = df1[['clust_xyz','Count']].groupby('clust_xyz').sum()
#########
sum_of_kindriver_per_cluster = df1[['clust_xyz','driver_mut']].groupby('clust_xyz').sum()
######
series1 = df1['clust_xyz'].value_counts()
no_of_members_per_cluster = series1.to_frame()
type(no_of_members_per_cluster)
no_of_members_per_cluster['x'] = no_of_members_per_cluster.index
dict = {'clust_xyz': 'no_of_members',
        'x': 'clust_xyz'}
 # call rename () method
no_of_members_per_cluster.rename(columns=dict,inplace=True)
#####################
combined_sum = pd.merge(sum_per_cluster,sum_of_kindriver_per_cluster,on='clust_xyz')
############
combined_sum_2 = pd.merge(combined_sum,no_of_members_per_cluster,on='clust_xyz')
combined_sum_2['avg_count'] = combined_sum_2['Count'] /combined_sum_2['no_of_members']
############
combined_sum_3 = pd.merge(combined_sum_2,df_count,on='clust_xyz')
############
combined_sum_3.to_csv('summary-of-clusters-final.csv')
##########
filter = (combined_sum_3['avg_count'] >= 5)
known_driver_clusters = combined_sum_3.loc[filter]
########
filter = (combined_sum_3['avg_count'] < 5)
novel_driver_clusters = combined_sum_3.loc[filter]
#########
known_driver_clusters.to_csv('known_driver_clusters.csv',index=False)
novel_driver_clusters.to_csv('novel_driver_clusters.csv',index=False)
##########
combined_sum_3.to_csv('summary-cluster-count-driver-members.csv',index=False)
