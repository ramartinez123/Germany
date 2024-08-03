from config.conf import Inic

class Queries:      
        def QueryUm():
                query ="SELECT st.state, ue.rate FROM unemployment as ue inner join states as st on st.id_state=ue.id_state"
                parameter=[]
                answer = Inic.db_connect(query,parameter)
                return answer
    
        
    

    