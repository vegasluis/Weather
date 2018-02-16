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
        self.myip = json.load(urllib.urlopen(url))['origin']
        return str(self.myip)  

def main():
    IP = myIP()
    print(IP.getIP())


if __name__ == "__main__":
    main()

