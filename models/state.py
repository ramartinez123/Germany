class States:
    def __init__(self,id_state,state,id_country):
        self._id_state = id_state
        self._state = state
        self._id_country = id_country

    def getid_state(self):
        return self._id_state

    def setid_state(self,x):
        self._id_state =x

    def getstate(self):
        return self._state

    def setstate(self,x):
        self._state =x

    def getid_country(self):
        return self._id_country

    def setidcontry(self,x):
        self._id_country =x 
