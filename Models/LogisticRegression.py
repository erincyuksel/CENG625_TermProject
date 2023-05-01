import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict

df = pd.read_csv("../DataGenerator/data.csv")
x = df.loc[:, df.columns != 'class']
y = df["class"]

scaler = StandardScaler()
x = scaler.fit_transform(x)

clf_LR = LogisticRegression(C=1.0, penalty='l2', tol=0.0001, solver="liblinear")
clf_LR.fit(x,y)

y_pred = cross_val_predict(clf_LR, x, y, cv=5)
print("Precision Score: \t {0:.4f}".format(precision_score(y,y_pred,average='weighted')))
print("Recall Score: \t\t {0:.4f}".format(recall_score(y,y_pred,average='weighted')))
print("F1 Score: \t\t {0:.4f}".format(f1_score(y,y_pred,average='weighted')))
print(confusion_matrix(y, y_pred))
res = cross_val_score(clf_LR, x, y, cv=5, scoring='accuracy')
print("Average Accuracy: \t {0:.4f}".format(np.mean(res)))
print("Accuracy SD: \t\t {0:.4f}".format(np.std(res)))