from flask import render_template
from app import app
from dao.unemploymentDao  import Queries
import json
    
@app.route('/unemployment') 
def unemployment():
    data= Queries.QueryUm()
    #data2= Consultas.ConsultarUmJson1(data)
    #data3= Consultas.ConsultarUmJson2(data)
    return render_template("unemployment.html",unemployment = data) 
