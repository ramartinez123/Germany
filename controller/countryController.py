from flask import render_template,request,redirect,url_for
from app import app,login_manager
from dao.countryDao import Queries
from flask_login import login_required
from models.country import Countries

@app.route('/countries')
def countries():
    data= Queries.Query2()
    #current_time=datetime.now().strftime("%y-%m-%d  %H: %M: %S")
    return render_template("countries.html", countries = data) 

@app.route('/countries/add_contact', methods=['POST'])
#@login_required
def add_contact():
    if request.method == "POST":
        country_r = request.form['f_country']
        country = Countries ("",country_r)
        Queries.Insert(country)                       
        return redirect(url_for("countries"))  

@app.route('/countries/edit/<id>')
#@login_required
def get_contact(id):
    country = Countries (id,"")
    data=Queries.Update1(country)
    return render_template("edit_countries.html", contact =data[0])

@app.route('/countries/update/<id>',methods=['POST'])
#@login_required
def update_contact(id):
    if request.method == "POST":
        country_r = request.form['f_country']
        country = Countries (id,country_r)
        Queries.Update2(country)
        return redirect(url_for("countries"))

@app.route('/countries/delete/<id>')
#@login_required
def delete_contact(id):
    country = Countries (id,"")
    Queries.Delete(country)
    return redirect(url_for("countries"))  
    


