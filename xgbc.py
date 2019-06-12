
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score,roc_auc_score
from xgboost.sklearn import XGBClassifier
import numpy as np

df = pd.read_csv(r'F:\Date\student\raw_data_bp2.csv',header=None)
x=df.iloc[:,[2,4,6,7,8,10,12,14]].values.tolist()
y=df.iloc[:,1].values.tolist()
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=2018)
X_train=np.array(X_train)
X_test=np.array(X_test)
y_train=np.array(y_train)
y_test=np.array(y_test)

Xgbc=XGBClassifier(random_state=2018)
Xgbc.fit(X_train,y_train)
y_xgbc_pred=Xgbc.predict(X_test)
Xgbc_score=accuracy_score(y_test,y_xgbc_pred) #准确率
Xgbc_auc=roc_auc_score(y_test,y_xgbc_pred) #Xgbc_auc值

print('Xgbc_score:',Xgbc_score)
print('Xgbc_auc:',Xgbc_auc)
