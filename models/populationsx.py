class Populationsx:
    def __init__(self,state,female,male,total):
        self._state=state
        self._female = female
        self._male= male
        self._total = total

    def getstate(self):
        return self._state
    
    def setstate(self,x):
        self._state =x

    def getfemale(self):
        return self._female
       
    def setfemale(self,x):
        self._female =x

    def getmale(self):
        return self._male
    
    def setmale(self,x):
        self._male =x

    def gettotal(self):
        return self._total
    
    def settotal(self,x):
        self._total =x  
    


 
 
