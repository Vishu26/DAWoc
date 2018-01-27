class Forecast(object):
    def __init__(self, forecast_data):
        self._forecast_data = forecast_data

    def text(self):
        return self._forecast_data['text']

    def date(self):
        return self._forecast_data['date']

    def high(self):
        return self._forecast_data['high']

    def low(self):
        return self._forecast_data['low']