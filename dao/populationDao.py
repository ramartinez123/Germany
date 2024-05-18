from app import mysql,app
from decimal import *
from models.populationsx import Populationsx
from config.conf import Inic

class Queries: 

    def Query():
        query ="""SELECT st.state, ct.country,  sx.sex, pp.population from countries as ct 
                inner join states as st on st.id_country=st.id_country
                inner join population as pp on st.id_state=pp.id_state
                inner join sex as sx on pp.id_sex=sx.id_sex
                inner join agerange as ag on pp.id_ageRange=ag.id_ageRange"""
        cur = mysql.connection.cursor()
        cur.execute(query)  
        answers=cur.fetchall()  
        records = []
        for answer in answers:
            answer = Populationsx( answer[0],answer[1],answer [2],answer [3])
            records.append(answer)
        return records 
    
    # consulta por sexo 
    def QuerySx():
        query ="""SELECT st.state,
                    SUM(CASE WHEN pp.id_sex=1 THEN pp.population END) AS Mujeres,
                    SUM(CASE WHEN pp.id_sex=2 THEN pp.population END) AS Hombres,
                    SUM(CASE WHEN pp.id_sex=3 THEN pp.population END) AS Total
                    from population as pp 
                            inner join states as st on pp.id_state=st.id_state
                            group by st.state"""
        parameter=[]                        
        answers = Inic.db_connect(query,parameter)
        records = []
        total1 =total2 = total3 =0
        for answer in answers:
            answer = Populationsx (answer[0],answer[1],answer[2],answer[3])
            total1= total1 + answer.getfemale()
            total2= total2 + answer.getmale()
            total3= total3 + answer.gettotal()
            records.append(answer)
        total = Populationsx ("Total",total1,total2,total3)
        records.append(total)
        return records

    def QuerySxGra():
        query ="""SELECT sx.sex,
                    SUM(CASE WHEN pp.id_state=10 THEN pp.population END) AS Northrein,
                    SUM(CASE WHEN pp.id_state=2 THEN pp.population END) AS Bayern
                    from population as pp 
                            inner join sex as sx on pp.id_sex=sx.id_sex
                            WHERE sx.id_sex <> 3
                            group by sex"""
        parameter=[]   
        answers2 = Inic.db_connect(query,parameter)
        return answers2   
 
    # consulta por sexo 
    def QueryAg():
        query = """SELECT ar.ageRange, SUM(pp.population) as Population
                        from population as pp 
                                inner join agerange as ar on pp.id_ageRange=ar.id_ageRange 
                                group by ar.ageRange
                                order by ar.id_ageRange"""     
        
        parameter=[] 
        answers = Inic.db_connect(query,parameter)
        return answers 

    def QueryBySt():
        query ="""SELECT st.state, ct.country,  sx.sex, ageRange, pp.population from countries as ct 
                inner join states as st on st.id_country=st.id_country
                inner join population as pp on st.id_state=pp.id_state
                inner join sex as sx on pp.id_sex=sx.id_sex
                inner join agerange as ag on pp.id_ageRange=ag.id_ageRange
                group by st.state, sx.sex order by st.state"""
        cur = mysql.connection.cursor()
        cur.execute(query)  
        answer=cur.fetchall()
        return answer 

    def QueryByAg():
        query ="""SELECT st.state, ct.country,  sx.sex, ag.ageRange, pp.population from countries as ct 
                inner join states as st on st.id_country=st.id_country
                inner join population as pp on st.id_state=pp.id_state
                inner join sex as sx on pp.id_sex=sx.id_sex
                inner join agerange as ag on pp.id_ageRange=ag.id_ageRange
                group by st.state, ag.ageRange order by st.state"""
        cur = mysql.connection.cursor()
        cur.execute(query)  
        answer=cur.fetchall()
        return answer 
    
    def QueryCi():
        query ="SELECT city, density, population FROM cities"
        cur = mysql.connection.cursor()      
        cur.execute(query)                
        answer=cur.fetchall()              
        return answer
    
    def QueryCi2():
        query ="SELECT city, density, population FROM cities where id_city <> 8"
        cur = mysql.connection.cursor()
        cur.execute(query)  
        answer=cur.fetchall()
        return answer
       
    def QueryPopMap():
        query ="SELECT id_state, SUM(population) As Total from population group by id_state"
        parameter=[] 
        answer =  Inic.db_connect(query,parameter)
        return answer