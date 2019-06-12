import lightgbm as lgb
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.datasets import  make_classification

import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score,roc_auc_score
from xgboost.sklearn import XGBClassifier



df = pd.read_csv(r'F:\Date\student\raw_data_bp2.csv',header=None)
x=df.iloc[:,[2,4,6,7,8,10,12,14]].values.tolist()
y=df.iloc[:,1].values.tolist()
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=2018)


lgb_train = lgb.Dataset(X_train, y_train)  # 将数据保存到LightGBM二进制文件将使加载更快
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)  # 创建验证数据

# 将参数写成字典下形式
params = {
    'task': 'train',
    'boosting_type': 'gbdt',  # 设置提升类型
    'objective': 'regression',  # 目标函数
    'metric': {'l2', 'auc'},  # 评估函数
    'num_leaves':128,  # 叶子节点数
    'learning_rate': 0.005, # 学习速率
    'feature_fraction': 0.9,  # 建树的特征选择比例
    'bagging_fraction': 0.8,  # 建树的样本采样比例
    'bagging_freq': 5,  # k 意味着每 k 次迭代执行bagging
    'verbose': 1  # <0 显示致命的, =0 显示错误 (警告), >0 显示信息
}

print('Start training...')
# 训练 cv and train
gbm = lgb.train(params, lgb_train, num_boost_round=500, valid_sets=lgb_eval)  # 训练数据需要参数列表和数据集

print('Save model...')

gbm.save_model('model2.txt')  # 训练后保存模型到文件

print('Start predicting...')
# 预测数据集
y_pred = gbm.predict(X_test)  # 如果在训练期间启用了早期停止，可以通过best_iteration方式从最佳迭代中获得预测
# 评估模型
print('The auc of prediction is:', roc_auc_score(y_test, y_pred) )
print('The rmse of prediction is:', mean_squared_error(y_test, y_pred) ** 0.5)
