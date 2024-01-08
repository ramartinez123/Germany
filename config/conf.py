from app import mysql

class Inic:
    query=""
    def __init__(self,query,paramters):
        self.db(query)
        self.db(paramters)

    def db_connect(quers,parameter):
        query = quers
        paramtersa = parameter
        try:
           cur = mysql.connection.cursor()
           try:  
                 cur.execute(query,paramtersa) 
                 answer=cur.fetchall()
           except:
                 print("Error de acceso a los datos")
        except:
           print("No se puedo establecer la conexion")            
        cur.close()
        return answer
     
    def db_insert(quers,parameter):
        query = quers
        parametersa= parameter
        try:
           cur = mysql.connection.cursor()
           try:  
                 cur.execute(query,parametersa) 
                 mysql.connection.commit()
           except:
                 print("Error de acceso a los datos")
        except:
           print("No se puedo establecer la conexion")            
        cur.close()
      

        

        

