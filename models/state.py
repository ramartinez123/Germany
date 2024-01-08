class States:
    def __init__(self,id_state,state,id_country):
        self.id_state = id_state
        self.state = state
        self.id_country = id_country

    def getid_state(self):
        return self.id_state

    def setid_state(self,x):
        self.id_state =x

    def getstate(self):
        return self.state

    def setstate(self,x):
        self.state =x

    
    def getid_country(self):
        return self.id_country

    def setidcontry(self,x):
        self.id_country =x 
