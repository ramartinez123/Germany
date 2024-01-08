from app import mysql
from models.country import Countries
from config.conf import Inic

class Queries:   
    def Query2() -> list[Countries]:  
        query ="SELECT * FROM countries" 
        parameters=[]
        answers = Inic.db_connect(query,parameters)
        records = []
        for answer in answers:
            answer = Countries( answer[0],answer[1] )
            records.append(answer)
        return records 
            
    def Insert(country:Countries) -> Countries:
        query ="INSERT INTO countries (country) VALUES(%s)"
        parameters=[country.getcountry()]
        Inic.db_insert(query,parameters)

    def Update1(country:Countries)-> Countries: 
        query="SELECT * FROM countries WHERE id_country = (%s)"
        parameters=[country.getid_country()]
        answers= Inic.db_connect(query,parameters)
        return answers

    def Update2(country:Countries)-> Countries:
        query ="UPDATE countries SET country =(%s) WHERE id_country =(%s)"
        parameters= [country.getcountry(),country.getid_country()]
        Inic.db_insert(query,parameters)  
    
    def Delete(country:Countries)-> Countries:
        query="DELETE FROM countries WHERE id_country =(%s)"
        parameters = [country.getid_country()]
        Inic.db_insert(query,parameters) 
 
        
        
    