import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
#opening file in read mode
model = pickle.load(open('predictmodel.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/addbb')
def addbb():
    return render_template('addbb.html')

@app.route('/adddonor')
def adddonor():
    return render_template('adddonor.html')

@app.route('/addhospital')
def addhospital():
    return render_template('addhospital.html')

@app.route('/analysisbank')
def analysisbank():
    return render_template('analysisbank.html')

@app.route('/analysishosp')
def analysishosp():
    return render_template('analysishosp.html')

@app.route('/predictbank')
def predictbank():
    return render_template('predictbank.html')

@app.route('/predicthosp')
def predicthosp():
    return render_template('predicthosp.html')

@app.route('/query')
def query():
    return render_template('query.html')

@app.route('/viewbb')
def viewbb():
    return render_template('viewbb.html')

@app.route('/viewcsv')
def viewcsv():
    return render_template('viewcsv.html')

@app.route('/viewhosp')
def viewhosp():
    return render_template('viewhosp.html')

@app.route('/predict',methods=['POST']) 
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    if output==str(1):
        return render_template('index.html', prediction_text='donor wants to donate {}'.format(output))
    else:
        return render_template('index.html', prediction_text='donor wants to donate {}'.format(output))
@app.route('/predict_api',methods=['GET','POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if output == 1:
        return "HELLO"
    else:
         return "BYE"


if __name__ == "__main__":
    app.debug = True
    app.run()