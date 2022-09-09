filter = (combined_sum_3['avg_count'] >= 5)
known_driver_clusters = combined_sum_3.loc[filter]
###########
filter = (combined_sum_3['avg_count'] < 5)
novel_driver_clusters = combined_sum_3.loc[filter]
###########
known_driver_clusters.to_csv('known_driver_clusters.csv',index=False)
novel_driver_clusters.to_csv('novel_driver_clusters.csv',index=False)