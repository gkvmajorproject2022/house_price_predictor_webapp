from flask import Flask, render_template, request
import pandas as pd
model = pd.read_pickle('/home/gkvmajorproject/mysite/house_price_predictor.pkl')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/house',methods=['GET','POST'])
def house_page():
    global model
    if request.method=='POST':
        inc = request.form['income']
        age = request.form['age']
        room = request.form['rooms']
        pop = request.form['population']

        query = pd.DataFrame({'income':[inc],'house_age':[age], 'rooms':[room],'population':[pop]})
        result = str(round(model.predict(query)[0],2))
        return render_template('mypage.html',price=result)

    return render_template('mypage.html')