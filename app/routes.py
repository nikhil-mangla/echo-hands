from flask import render_template, request
from app import app
from app.model import predict

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/predict')
def make_prediction():
    # if request.method == 'POST':
    #     data = request.form['input_data']
    #     prediction = predict(data)
    return render_template('index.html')


@app.route('/start.html')
def start():
    return render_template('start.html')
  
