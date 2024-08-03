class Populationsx:
    def __init__(self, state, female, male, total):
        self._state = state
        self._female = female
        self._male = male
        self._total = total

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def female(self):
        return self._female

    @female.setter
    def female(self, value):
        self._female = value

    @property
    def male(self):
        return self._male

    @male.setter
    def male(self, value):
        self._male = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

 
 
