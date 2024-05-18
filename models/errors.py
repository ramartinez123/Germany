from flask import render_template, Response
from app import app
from models import erro

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

 #<script>
 #   let arrpopulation = {{ populations | tojson}}                                                      
    #</script>



