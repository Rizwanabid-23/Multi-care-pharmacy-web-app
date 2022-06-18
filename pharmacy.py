from flask import Flask, render_template, request
app = Flask(__name__, template_folder="templates")

import pandas as pd


from db import editemployee
from db import admin_id
from db import admin_pin
import numpy as np
from db import emp_id
from db import emp_pin
from db import check_emp



#to_send=[]

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/home.html")
def hi():
    return render_template("home.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/admin.html")
def admin():
    return render_template("admin.html")

@app.route("/newEmployee.html")
def newEmployee():
    return render_template("newEmployee.html")

@app.route("/newProduct.html")
def newProduct():
    return render_template("newProduct.html")


@app.route("/editEmployee.html",methods=['POST','GET'])
def editEmployee():
    
    df,fname,lname,uname,pin,cnic,adress,phone,email=editemployee()
  #  to_send=df.to_html()
    df=str(df).replace('[','').replace('[','').replace(']','')
    fname=str(fname).replace('[','').replace('[','').replace(']','').replace("'",'')
    lname=str(lname).replace('[','').replace('[','').replace(']','').replace("'",'')
    uname=str(uname).replace('[','').replace('[','').replace(']','').replace("'",'')
    pin=str(pin).replace('[','').replace('[','').replace(']','').replace("'",'')
    cnic=str(cnic).replace('[','').replace('[','').replace(']','').replace("'",'')
    adress=str(adress).replace('[','').replace('[','').replace(']','').replace("'",'')
    phone=str(phone).replace('[','').replace('[','').replace(']','').replace("'",'')
    email=str(email).replace('[','').replace('[','').replace(']','').replace("'",'')

    return render_template('editEmployee.html',to_send=df,fname=fname,lname=lname,uname=uname,pin=pin,cnic=cnic,adress=adress,phone=phone,email=email)


@app.route("/wrong.html")
def wrong():
    return render_template("wrong.html")

@app.route("/sales.html")
def sales():
    return render_template("sales.html")

@app.route("/index.html", methods=['POST','GET'])
def signin():
    uname = request.form
    id = uname['username']
    upin=request.form
    pin=upin['password']

    if id==admin_id() and pin==admin_pin():
        return render_template("admin.html")
    else:
        u,i=check_emp(id,pin)
        if u.size==0:
            return render_template("wrong.html")
        elif u==id:
            i=int(i)
            return render_template("sales.html",id=id,i=i)



    

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
