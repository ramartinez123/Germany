from app import mysql,app
from decimal import *
from config.conf import Inic



class Queries: 

    def Query():
        query ="""SELECT st.state, ct.country,  sx.sex, ageRange, pp.population from countries as ct 
                inner join states as st on st.id_country=st.id_country
                inner join population as pp on st.id_state=pp.id_state
                inner join sex as sx on pp.id_sex=sx.id_sex
                inner join agerange as ag on pp.id_ageRange=ag.id_ageRange"""
        cur = mysql.connection.cursor()
        cur.execute(query)  
        answer=cur.fetchall() 
        return answer 
        
    def QuerySx():
        query ="""SELECT st.state, ct.country, 
                    SUM(CASE WHEN sx.sex='F'THEN pp.population END) AS Mujeres,
                    SUM(CASE WHEN sx.sex='M'THEN pp.population END) AS Hombres,
                    SUM(pp.population) As Total
                    from countries as ct 
                            inner join states as st on st.id_country=st.id_country
                            inner join population as pp on st.id_state=pp.id_state
                            inner join sex as sx on pp.id_sex=sx.id_sex 	
                            group by st.state"""
        parameter=[]                    
        answer = Inic.db_connect(query,parameter)
        return answer
        
 
    def QueryAg():
        query ="""SELECT st.state, ct.country,  sx.sex, ageRange, pp.population from countries as ct 
                inner join states as st on st.id_country=st.id_country
                inner join population as pp on st.id_state=pp.id_state
                inner join sex as sx on pp.id_sex=sx.id_sex
                inner join agerange as ag on pp.id_ageRange=ag.id_ageRange
                where ag.id_ageRange=1
                order by st.state"""
        cur = mysql.connection.cursor()
        cur.execute(query)  
        answer=cur.fetchall()
        return answer 

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