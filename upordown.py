## Is it Up or is it down ##
import socket
import time
from datetime import datetime

## Define timeout, port to test, and array of servers to test
socketTimeout = 1
port = 443
servers = ["labpsc1", "labvcenter1", "labesx3"]

while True:
   testTime = datetime.now()
   print (' ')
   print('-----' + str(testTime) + '-----')
   for server in servers:
      print ('Testing ' + server + ' port ' + str(port))
      ## Get IP Address of Server
      serverIP = socket.gethostbyname(server)
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      ## Set the timeout for the connection
      sock.settimeout(socketTimeout)
      ## Try to connect
      result = sock.connect_ex((serverIP, port))
      ## If connection was successful
      if result == 0:
         text = server + ' is UP'
      ## If connection was not successful   
      else:
         text = '**** ' + server + ' is DOWN ****'
      print(text)
      sock.close()
   ## Slee for 5 seconds and go again   
   time.sleep(5)
