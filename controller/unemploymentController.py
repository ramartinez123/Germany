from flask import render_template
from app import app
from dao.unemploymentDao  import Queries
    
@app.route('/unemployment') 
def unemployment():
    try:
        data= Queries.QueryUm()
        return render_template("unemployment.html",unemployment = data) 
    
    except Exception as e:
        print(f"Error en la ruta /unemployment: {e}")

