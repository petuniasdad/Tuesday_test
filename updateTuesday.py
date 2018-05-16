import os

try:
  updateString = "cd /home/pi/Desktop/Tuesday_test && sudo git pull"
  os.system(updateString)
except:
  print('Error')
