import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("../DataGenerator/data.csv")
x = df.loc[:, df.columns != 'class']
y = df["class"]

sc = StandardScaler()
X_scaled = sc.fit_transform(x)
pca = PCA(n_components=15)
pca.fit(X_scaled)
X_pca = pca.transform(X_scaled)
titles = []
for i in range(15):
        titles.append("PC " + str(i+1))

plt.bar(titles, pca.explained_variance_, color ='maroon',
        width = 0.4)
plt.xlabel("Principal Components")
plt.ylabel("Eigen Values")
plt.title("Eigen Value Distribution of First 15 Principal Components")
plt.show()
