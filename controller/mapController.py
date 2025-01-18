from flask import Response
from app import app
from dao.populationDao import Queries
from decimal import *
from helpers.csv_write import Csv_w
import os
from dao.map import create_map

@app.route('/static/map')
def map():
    states= os.path.join('static', 'germany.geojson') 
    head=["id","population"]
    state_data= Queries.QueryPopMap()
    state_data_json= Csv_w.csvWrite(head,state_data)
    m = create_map(states, state_data_json)
    
    # Rendariza mapa en memoria
    map_html = m._repr_html_()
    return Response(map_html, mimetype='text/html')  
  
      



