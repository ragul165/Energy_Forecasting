import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
import pickle
from sklearn.svm import SVR
plt.style.use('fivethirtyeight')
import numpy as np



df=pd.read_csv("T2.csv")

series = df['LV ActivePower (kW)']
time = []
for i in range(0,356):
  time.append([i])

rbf_svr=SVR(kernel='rbf',C=100.0,gamma=0.15)
rbf_svr.fit(time,series)


pickle.dump(rbf_svr,open('model2.pkl','wb'))
MLmodel=pickle.load(open('model2.pkl','rb'))
print(MLmodel.predict([[67]]))