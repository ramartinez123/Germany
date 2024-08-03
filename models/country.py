class Countries:
    def __init__(self, id_country, country):
        self._id_country = id_country
        self._country = country

    @property
    def id_country(self):
        """Getter for id_country."""
        return self._id_country

    @id_country.setter
    def id_country(self, value):
        """Setter for id_country."""
        self._id_country = value

    @property
    def country(self):
        """Getter for country."""
        return self._country

    @country.setter
    def country(self, value):
        """Setter for country."""
        self._country = value
