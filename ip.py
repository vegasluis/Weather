import json
import urllib 

class myIP:
    """
    Get the IP of user running the program 

    attributes:myip 
    """

    def __init__(self):
        self.myip = 0

    def __str__(self):
        return str(self.myip)
    
    def getIP(self):
        url = 'http://httpbin.org/ip'
        self.myip =str(json.load(urllib.urlopen(url))['origin'])

    def retIP(self):
        return str(self.myip)
    
def main():
    IP = myIP()
    IP.getIP()
    print(IP)


if __name__ == "__main__":
    main()

