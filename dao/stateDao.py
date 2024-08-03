from app import mysql
from flask import render_template, request, redirect, url_for
from models.state import States
from config.conf import Inic

class Queries:
    
    
    def query_states() -> list[States]:  
        query = """
        SELECT st.id_state, st.state, ct.country 
        FROM states as st 
        INNER JOIN countries as ct ON st.id_country = ct.id_country
        """
        parameters = []
        try:
            answers = Inic.db_connect(query, parameters)
            records = [States(answer[0], answer[1], answer[2]) for answer in answers]
            return records
        except Exception as e:
            print(f"Error fetching states: {e}")
            return []

    
    def insert_state(state: States) -> None:
        query = "INSERT INTO states (state, id_country) VALUES (%s, %s)"
        parameters = [state.state, state.id_country]
        try:
            Inic.db_insert(query, parameters)
        except Exception as e:
            print(f"Error inserting state: {e}")

    
    def get_state_by_id(state:States)-> States:
        query = "SELECT * FROM states WHERE id_state = %s"
        parameters=[state.id_state]
        try:
            result = Inic.db_connect(query, parameters)  # Suponiendo que `db_query` devuelve una lista o tupla
            return result
        except Exception as e:
            print(f"Error fetching state: {e}")
            return None
    
    def update_state(state: States) -> None:
        query = "UPDATE states SET state = %s WHERE id_state = %s"
        parameters = [state.state, state.id_state]
        try:
            Inic.db_insert(query, parameters)
        except Exception as e:
            print(f"Error updating state: {e}")


    def delete_state(state_id: int) -> None:
        query = "DELETE FROM states WHERE id_state = %s"
        parameters = [state_id]
        try:
            Inic.db_insert(query, parameters)
        except Exception as e:
            print(f"Error deleting state: {e}")
        
