from models.country import Countries
from config.conf import Inic

class Queries:   
    def get_all_countries() -> list[Countries]:  
        query ="SELECT * FROM countries" 
        parameters=[]
        answers = Inic.db_connect(query,parameters)
        records = []
        for answer in answers:
            answer = Countries( answer[0],answer[1] )
            records.append(answer)
        return records 
            
    def insert_country(country:Countries) -> None:
        query ="INSERT INTO countries (country) VALUES(%s)"
        parameters=[country.country]
        Inic.db_insert(query,parameters)

    def get_country_by_id(country:Countries)-> Countries: 
        query="SELECT * FROM countries WHERE id_country = (%s)"
        parameters=[country.id_country]
        answers= Inic.db_connect(query,parameters)
        if answers:
            return answers
        return None
        
    def update_country(country:Countries)-> None:
        query ="UPDATE countries SET country =(%s) WHERE id_country =(%s)"
        parameters= [country.country,country.id_country]
        Inic.db_insert(query,parameters)  
    
    def delete_country(country_id:int)-> None:
        query="DELETE FROM countries WHERE id_country =(%s)"
        parameters = [country_id]
        try:
            Inic.db_insert(query, parameters)
        except Exception as e:
            print(f"Error deleting state: {e}")
 
        
        
    