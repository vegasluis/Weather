import json
import urllib 

class myIP(object):
    """
    Get the IP of user running the program 

    attributes:myip 
    """

    def __init__(self,myip=0):
        self.myip = myip

    def __str__(self):
        return str(self.myip)
    
    def getIP(self):
        url = 'http://httpbin.org/ip'
        self.myip =str(json.load(urllib.urlopen(url))['origin'])

    def retIP(cls):
        return str(cls.myip)
    
def main():
    IP = myIP()
    IP.getIP()
    print(IP)
    other = myIP('125.99.114.130')
    print(other)


if __name__ == "__main__":
    main()

