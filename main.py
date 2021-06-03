from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import requests
from sklearn import linear_model

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))
model2=pickle.load(open('model2.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("/welcome.html")

@app.route('/windfore',methods=['POST','GET'])
def hello():
    return render_template("/forest.html")

@app.route('/windfore1',methods=['POST','GET'])
def hell():
    return render_template("/forest2.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=ae60dfc2e98dee7b878de035aae690b5&q='
    city=[str(x) for x in request.form.values()]
    print(city)
    url=api_address+city[0]
    json_data=requests.get(url)
    data=json_data.json()
    print(data)
    degree=data['wind']['deg']
    speed=data['wind']['speed']
    print('wind speed ',speed)
    print('wind directiomn ',degree)
    y_predict=model.predict([[speed,degree]])
    if(y_predict[0]<0):
        print(0)
        return render_template('forest.html',pred=0)
    else:
        print(y_predict[0])
    return render_template('forest.html',pred=y_predict)

@app.route('/predict1',methods=['POST','GET'])
def predict1():
    dat=[str(x) for x in request.form.values()]
    #y_predict2=model.predict([[dat]])
    print(dat[0][5:7])
    print(dat[0][8:])
    date=int(dat[0][5:7])
    mon=int(dat[0][8:])
    print(date)
    x=((mon-1)*30)+date
    y_predict2=model2.predict([[x]])
    return render_template('forest.html',pred=y_predict2)

if __name__ == "__main__":
    app.run(debug=True)

