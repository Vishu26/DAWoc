import requests
import pprint
from .objects.weather_obj import WeatherObject


class Weather(object):
    URL = 'http://query.yahooapis.com/v1/public/yql'

    def lookup(self, woeid):
        url = '%s?q=select * from weather.forecast where woeid = %s&format=json' % (self.URL, woeid)
        results = self._call(url)
        return results

    def lookup_by_location(self, location):
        url = "%s?q=select* from weather.forecast " \
              "where woeid in (select woeid from geo.places(1) where text='%s')&format=json" % (self.URL, location)
        results = self._call(url)
        return results

    @staticmethod
    def _call(url):
        req = requests.get(url)

        if not req.ok:
            req.raise_for_status()

        results = req.json()

        if int(results['query']['count']) > 0:
            wo = WeatherObject(results['query']['results']['channel'])
            return wo
        else:
            pprint.pprint(results)
