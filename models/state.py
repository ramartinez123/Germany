class States:
    def __init__(self, id_state, state, id_country):
        self._id_state = id_state
        self._state = state
        self._id_country = id_country

    @property
    def id_state(self):
        return self._id_state

    @id_state.setter
    def id_state(self, value):
        self._id_state = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def id_country(self):
        return self._id_country

    @id_country.setter
    def id_country(self, value):
        self._id_country = value