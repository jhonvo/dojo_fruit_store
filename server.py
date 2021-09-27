#!/usr/bin/env python3

from datetime import date, datetime
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    customer_name = f"{request.form['first_name']} {request.form['last_name']}"
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    count = int(strawberry)+int(raspberry)+int(apple)
    date = datetime.now()
    date_format = date.strftime("%B %d %Y, %I:%M:%S %p")
    print (f'Charging {customer_name} for {count} fruits')
    return render_template("checkout.html", count = count, date = date_format, last_name = request.form['last_name'], first_name = request.form['first_name'], student_id = request.form['student_id'] )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)     