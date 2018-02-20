import urllib2
import json
import re 
from location import location 

class weather(location):
    """
        Get the statics of the weather
        based on your location 

        attributes: tempature, humidty, condition, pressure 

    """
    def __init__(self,myip=0,city='',country='',state=''):
       self.tempature = ''
       self.humidity = ''
       self.condition = ''
       self.pressure = ''
       self.windSpeed = ''
       super(weather,self).__init__(str(myip),city,country,state)

    def getWeather(self):
        self.getLocation()
        api = 'e4260b30df4e60cfa169c2656c9b207f'
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + self.retCity() + ',' + self.retCountry() + '&appid=' + api
        response = urllib2.urlopen(url)
        data =  json.load(response) 
        self.tempature = data['main']['temp']-273.0
        self.humidity = data['main']['humidity']
        self.pressure = data['main']['pressure']
        self.condition = data['weather'][0]['description']
        self.windSpeed =  data['wind']['speed']
        
    def printWeather(self):
        print('\nGetting Weather Information in ' + self.city + ', ' + self.country + ' ...' )
        print('Weather : ' + str(self.condition))
        print('Tempature: ' + str( self.tempature) + ' C')
        print('Wind : ' + str(self.windSpeed) + ' Kmph')
        print('Humidity: ' + str(self.humidity))
        print('Presure: ' + str(self.pressure) + '\n')

def main():
    my_weather = weather()
    my_weather.getIP()
    my_weather.getWeather()
    my_weather.printWeather()

    """
    other_weather = weather('125.99.114.130')
    other_weather.getWeather()
    other_weather.printWeather()
    """

if __name__ == "__main__":
    main()
    

