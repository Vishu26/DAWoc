class Condition(object):
    def __init__(self, condition_data):
        self._condition_data = condition_data

    def date(self):
        return self._condition_data['date']

    def text(self):
        return self._condition_data['text']

    def code(self):
        return self._condition_data['code']

    def temp(self):
        return self._condition_data['temp']
