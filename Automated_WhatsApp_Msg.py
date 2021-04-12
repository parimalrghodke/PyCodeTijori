############
#This will help you to send a certain msg at specific time to a specific number
#Installation
#pip3.7 install pywhatkit
#Author: Parimal Ghodke
####################################################################################

import pywhatkit as kit

kit.sendwhatmsg("+9199********","Helloo, this is automated msg from pycodeTijori",23,3)
#("+91 10 number","msg in double qoutes", hrs , mins) time is in 24 hrs format
#Will open web.whatsapp.com at 23:3 and message will be sent at exactly 23:5


#method 2
kit.sendwhatmsg_with_selenium("+9198********","Helloo, this is autmoated msg from pycodeTijori",23,1)
#Will send message with most of the processes hidden





