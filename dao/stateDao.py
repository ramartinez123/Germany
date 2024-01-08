from app import mysql
from flask import render_template,request,redirect,url_for
from models.state import States
from config.conf import Inic

class Queries: 
    def Query2() -> list[States]:  
        query ="SELECT st.id_state, st.state, ct.country from states as st inner join countries as ct on st.id_country=ct.id_country "
        parameters=[]
        answers = Inic.db_connect(query,parameters)
        records = []
        for answer in answers:
            answer = States( answer[0],answer[1],answer [2])
            records.append(answer)
        return records 
        
    def Insert(state:States) -> States:
        query ="INSERT INTO states (state,id_country) VALUES(%s,%s)"
        parameters = [state.getstate(),state.getid_country()]
        Inic.db_insert(query,parameters)    

    def Update1(state:States)-> States:  
        query="SELECT * FROM states WHERE id_state = (%s)"
        parameters=[state.getid_state()]
        answers= Inic.db_connect(query,parameters)
        return answers     

    def Update2(state:States) -> States:
        query ="UPDATE states SET state =(%s) WHERE id_state =(%s)"
        parameters= [state.getstate(),state.getid_state()]
        Inic.db_insert(query,parameters)     
    
    def Delete(state:States)-> States:
        query="DELETE FROM states WHERE id_state =(%s)"
        parameters = [state.getid_state()]
        Inic.db_insert(query,parameters) 
        
