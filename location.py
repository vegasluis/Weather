import urllib
import json
import re 
from ip import myIP

class location(myIP):
    """
        Get the location based off 
        of a global ip

        attributes: city, country, state

    """

    def __init__(self,myip=0,city='',country='',state=''):
        self.city = ''
        self.country = ''
        self.state = ''
        super(location,self).__init__(myip)
       

    def __str__(self):
        return '\nCountry:' + self.country + '\tState:' + self.state + '\tCity:' + self.city + '\n'

    def getLocation(self):
       url = 'http://ipinfo.io/' + self.retIP() + '/json'
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
    print('My Information: ')
    myInfo = location()
    myInfo.getIP()
    myInfo.getLocation()
    print(myInfo)
    print('Desired Ip Info: ')
    other = location('125.99.114.130')  
    other.getLocation()
    print(other)

if __name__ == "__main__":
    main()
    

