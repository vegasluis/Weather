import urllib
import json
import re 
from ip import myIP

class location:
    """
        Get the location based off 
        of a global ip

        attributes: city, country, state

    """
    IP = myIP()

    def __init__(self):
        self.city = ''
        self.country = ''
        self.state = ''

    def __str__(self):
        return '\nCountry:' + self.country + '\tState:' + self.state + '\tCity:' + self.city + '\n'

    def getLocation(self):
       self.IP.getIP()
       url = 'http://ipinfo.io/' + self.IP.retIP() + '/json'
       response = urllib.urlopen(url)
       data = json.load(response)
       self.city = data['city']
       self.country = data['country']
       self.state = data['region']
    
    def retCity(self):
        return str(self.city)
    def retCountry(self):
        return str(self.country)
    def retState(self):
        return str(self.state)
    
def main():
    myInfo = location()
    myInfo.getLocation()
    print(myInfo)


if __name__ == "__main__":
    main()
    

