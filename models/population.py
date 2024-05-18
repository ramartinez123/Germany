class Population:
    def __init__(self,id_population,id_state,id_sex,id_agerange,population):
        self._id_popullation=id_population
        self._id_state = id_state
        self._id_sex=id_sex
        self._id_agerange = id_agerange
        self._population = population

    def getid_popullation(self):
        return self._id_popullation
    
    def setid_popullation(self,x):
        self._id_popullation =x

    def getid_state(self):
        return self._id_state
       
    def setid_state(self,x):
        self._id_state =x

    def getid_sex(self):
        return self._id_sex
    
    def setid_sex(self,x):
        self._id_sex =x

    def getid_agerange(self):
        return self._id_agerange
    
    def setid_agerange(self,x):
        self._id_agerange =x  
    
    def getpopullation(self):
        return self._popullation

    def setid_popullation(self,x):
        self._id_popullation =x  

 
 
