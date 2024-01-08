from flask import render_template,request,redirect,url_for
from app import app
from dao.populationDao import Queries
from decimal import *
from helpers.csv_write import Csv_w
from folium import plugins
import folium, os

@app.route('/map')
def map():
    states= os.path.join('static', 'germany.geojson') 
    head=["id","population"]
    state_data= Queries.QueryPopMap()
    state_data_json= Csv_w.csvWrite(head,state_data)
    m=folium.Map(location=[51.11,10.68],width=500,height=600,zoom_start=6,tiles="Cartodb Positron")
    minimap = plugins.MiniMap()
    m.add_child(minimap)    
    m.save('map.html')

    folium.Choropleth ( 
        geo_data=states,
        name="choropleth",
        data=state_data_json,   
        columns=['id','population'],
        key_on= 'feature.id',
        fill_color='YlGn',
        nan_fill_color='YlGn',
        fill_opacity=0.6,
        line_opacity=0.6,
        highlight=True, 
        legend_name='Poblacion'
        ).add_to(m)        
    
    folium.LayerControl().add_to(m)   
    #return render_template("map.html")
    return m._repr_html_()      



