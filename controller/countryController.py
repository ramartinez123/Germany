from flask import render_template,request,redirect,url_for
from app import app,login_manager
from dao.countryDao import Queries
from flask_login import login_required
from models.country import Countries

@app.route('/countries')
def countries():
    data = Queries.get_all_countries()
    return render_template("countries.html", countries = data) 

@app.route('/countries/add_contact', methods=['POST'])
#@login_required
def add_contact():
    if request.method == "POST":
        country_r = request.form['f_country']
        country = Countries ("",country_r)
        Queries.insert_country(country)                       
        return redirect(url_for("countries"))  

@app.route('/countries/edit/<id>')
#@login_required
def get_contact(id):
    country = Countries (id,"")
    data=Queries.get_country_by_id(country)
    if data:
        return render_template("edit_countries.html", contact =data[0])
    else:
        return "Country not found", 404

@app.route('/countries/update/<id>',methods=['POST'])
#@login_required
def update_contact(id):
    if request.method == "POST":
        country_r = request.form['f_country']
        country = Countries (id,country_r)
        Queries.update_country(country)
        return redirect(url_for("countries"))

@app.route('/countries/delete/<id>')
#@login_required
def delete_contact(id):
    country = Countries (id,"")
    Queries.delete_country(id)
    return redirect(url_for("countries"))  
    


