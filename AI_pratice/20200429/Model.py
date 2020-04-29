'''
info of this practice in 'kaggle' website
file from 'titanic practice'
model method from course of kaggle
'''

import pandas as pd
from sklearn.tree import DecisionTreeRegressor

file_path = './train.csv'

data = pd.read_csv(file_path)
print(data.describe())
# 定義 預測的 input / output
data = data.dropna(axis = 0) # dropna drops missing values (think of na as "not available")
y = data.Survived # 要預測的目標 (最後的output)
features = ['Pclass', 'Age', 'Fare'] #選擇用來當作預測的條件 (開始的input)
X = data[features] 
'''
Building Model:
* Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
* Fit: Capture patterns from provided data. This is the heart of modeling.
* Predict: Just what it sounds like
* Evaluate: Determine how accurate the model's predictions are.
'''

# Define model. Specify a number for random_state to ensure same results each run
model = DecisionTreeRegressor(random_state = 1)
# Fit model
model.fit(X,y) 
#印出結果
print('\n#Making predictions for the following 5:')
print(X.head())
print('#The predictions are:')
print(model.predict(X.head())) #要預測的資料及印出結果

