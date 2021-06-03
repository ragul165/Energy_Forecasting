from sklearn import linear_model
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
import pickle


df=pd.read_csv("T1.csv")

reg=linear_model.LinearRegression()
reg.fit(df[['Wind Speed (m/s)','Wind Direction (°)']],df['LV ActivePower (kW)'])

pickle.dump(reg,open('model.pkl','wb'))
#MLmodel=pickle.load(open('model.pkl','rb'))