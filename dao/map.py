import folium
from folium import LinearColormap

def create_map(states, state_data_json):
    m = folium.Map(location=[51.11, 10.68], width=500, height=600, zoom_start=6, tiles="Cartodb Positron")
    
   
    folium.Choropleth(
        geo_data=states,
        name="choropleth",
        data=state_data_json,
        columns=['id', 'population'],
        key_on='feature.id',
        fill_color='YlGn',
        nan_fill_color='grey',
        fill_opacity=0.7,
        line_opacity=0.3,
        highlight='True',
        legend_name='Population',
           
    ).add_to(m)

    folium.LayerControl().add_to(m)
    return m

