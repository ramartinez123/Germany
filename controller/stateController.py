from flask import render_template,request,redirect,url_for
from app import app
from dao.stateDao import Queries
from models.state import States

@app.route('/states')
def states():
    data= Queries.query_states()
    return render_template("states.html", states = data) 

@app.route('/states/add_contact', methods=['POST'])
def add_state():
    if request.method == "POST":
        state_r=request.form['f_state']
        country_r=request.form['f_idCountry']
        state= States("",state_r,country_r)
        Queries.insert_state(state)                       
        return redirect(url_for("states"))  

@app.route('/states/edit/<int:id>')
def get_state(id):  
    state= States (id,"","")
    data=Queries.get_state_by_id(state)
    if data is None or len(data) == 0:
        # Manejo del caso cuando no se encuentran datos
        return "State not found", 404  # O redirigir a una página de error
    state = data[0]
    return render_template("edit_states.html", contact=state)

@app.route('/states/update/<id>',methods=['POST'])
def update_state(id):
    if request.method == "POST":
        state_r=request.form['f_state']
        state = States (id,state_r,"")
        Queries.update_state(state)
        return redirect(url_for("states"))

@app.route('/states/delete/<int:id>')
def delete_state(id):
    try:
        Queries.delete_state(id) 
        return redirect(url_for("states"))
    except Exception as e:
        print(f"Error deleting state: {e}") 
    


