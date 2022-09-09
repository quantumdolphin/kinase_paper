import pandas as pd
raw_data_2 = pd.read_csv('combo-kindriver-CRDS.csv')
########
import numpy as np
raw_data_3 = raw_data_2[['x', 'y', 'z']]
X = np.array(raw_data_3)
############
# the script below will generate dendogram 
# this dendogram was used to calculate the ideal no of clusters
#
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
distances = linkage(X,method="centroid",metric="euclidean")
plt.figure(figsize=(8,6))
dn = dendrogram(distances)
plt.title("Dendrograms-CENTROID")
plt.xlabel('XYZ')
plt.ylabel('Euclidean distances')
plt.show()
##########
# Using the dendrogram to find the optimal numbers of clusters. 
# place dotted line at the optimum euclidean distance that will generate 31 clusters.
import scipy.cluster.hierarchy as sch
plt.figure(figsize=(10, 7))  
plt.title("Dendrograms")  
dend3 = sch.dendrogram(sch.linkage(X, method='ward'))
plt.xlabel('XYZ')
plt.ylabel('Euclidean distances')
plt.axhline(y=75, color='r', linestyle='--')
############
from sklearn.cluster import AgglomerativeClustering 
hc = AgglomerativeClustering(n_clusters = 32, affinity = 'euclidean', linkage ='ward')
y_hc=hc.fit_predict(X)
###########
import copy
clustered_xyz = pd.DataFrame(data=y_hc, columns=['clust_xyz'])
temp_df = pd.concat([raw_data_2,clustered_xyz], axis=1)
raw_data_with_xyz_clust = copy.deepcopy(temp_df)
raw_data_with_xyz_clust.to_csv('xyz_hc_clust.csv',index=False)