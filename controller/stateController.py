from flask import render_template,request,redirect,url_for
from app import app
from dao.stateDao import Queries
from models.state import States

@app.route('/states')
def states():
    data= Queries.Query2()
    return render_template("states.html", states = data) 

@app.route('/states/add_contact', methods=['POST'])
def add_state():
    if request.method == "POST":
        state_r=request.form['f_state']
        country_r=request.form['f_idCountry']
        state= States("",state_r,country_r)
        Queries.Insert(state)                       
        return redirect(url_for("states"))  

@app.route('/states/edit/<id>')
def get_state(id):
    state= States (id,"","")
    data=Queries.Update1(state)
    return render_template("edit_states.html", contact =data[0])

@app.route('/states/update/<id>',methods=['POST'])
def update_state(id):
    if request.method == "POST":
        state_r=request.form['f_state']
        state = States (id,state_r,"")
        Queries.Update2(state)
        return redirect(url_for("states"))

@app.route('/states/delete/<id>')
def delete_state(id):
    state = States (id,"","")
    print(state)
    Queries.Delete(state) 
    return redirect(url_for("states"))  
    


