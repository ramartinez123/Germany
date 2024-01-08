from flask import render_template
from app import app
from dao.populationDao import Queries

@app.route('/population')
def population():
    data= Queries.Query()
    return render_template("population.html", population = data) 

@app.route('/populationSx') 
def populationSx():
    data= Queries.QuerySx()
    return render_template("populationSx.html", population = data) 
    
@app.route('/populationAg')
def populationAg():
    data= Queries.QueryAg()
    return render_template("populationAg.html", population = data) 

@app.route('/populationBySt')
def populationBySt():
    data= Queries.QueryBySt()
    return render_template("populationBySt.html", population = data) 

@app.route('/populationByAg')
def populationByAg():
    data= Queries.QueryByAg()
    return render_template("populationByAg.html", population = data) 

@app.route('/populationCi')
def populationCi():
    data= Queries.QueryCi()
    data2= Queries.QueryCi2()
    return render_template("populationCi.html", population = data, population2 = data2) 