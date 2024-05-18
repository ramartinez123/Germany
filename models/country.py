class Countries:
    def __init__(self,id_country,country):
        self._id_country = id_country
        self._country = country

    def getid_country(self):
        return self._id_country

    def setid_country(self,x):
        self._id_country =x

    def getcountry(self):
        return self._country

    def setcountry(self,x):
        self._country =x
