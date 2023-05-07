import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import BaggingClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df = pd.read_csv("../DataGenerator/data.csv")
x = df.loc[:, df.columns != 'class']
y = df["class"]

# STARTING PCA FEATURE EXTRACTION
sc = StandardScaler()
X_scaled = sc.fit_transform(x)
pca = PCA(n_components=4)
pca.fit(X_scaled)
X_pca = pca.transform(X_scaled)

bgclassifier = BaggingClassifier(estimator=LogisticRegression(random_state=1), n_estimators=200,
                                 max_features=4,
                                 max_samples=12,
                                 random_state=1, n_jobs=5)
bgclassifier.fit(X_pca, y)

y_pred = cross_val_predict(bgclassifier, X_pca, y, cv=5)
print("************************ PCA FEATURE EXTRACTION ************************")
print("Precision Score: \t {0:.4f}".format(precision_score(y,y_pred,average='weighted')))
print("Recall Score: \t\t {0:.4f}".format(recall_score(y,y_pred,average='weighted')))
print("F1 Score: \t\t {0:.4f}".format(f1_score(y,y_pred,average='weighted')))
print(confusion_matrix(y, y_pred))
res = cross_val_score(bgclassifier, X_pca, y, cv=5, scoring='accuracy')
print("Average Accuracy: \t {0:.4f}".format(np.mean(res)))
print("Accuracy SD: \t\t {0:.4f}".format(np.std(res)))
fpr, tpr, thresholds = metrics.roc_curve(y, y_pred)
roc_auc = metrics.auc(fpr, tpr)
display_roc = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc,estimator_name='Logistic Regression With PCA Feature Extraction')
display_roc.plot()
plt.show()
display_matrix = metrics.ConfusionMatrixDisplay(confusion_matrix(y, y_pred, labels=[0,1]), display_labels=["Normal", "Pre-Diabetic"])
display_matrix.plot()
plt.show()