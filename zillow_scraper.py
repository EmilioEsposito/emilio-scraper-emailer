
# coding: utf-8

# # Setup Email
# 

# In[3]:

import smtplib

def mySendMail(sender, receivers, subject, body):
    receivers_text = ", ".join(["<"+receiver+">" for receiver in receivers])

    message = "From: <"+sender+">\nTo: "+receivers_text+"\nSubject: "+subject+"\n\n"+body+"\n"

    try:
        server = smtplib.SMTP('mail.smtp2go.com', 2525) #  8025, 587 and 25 can also be used. 
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("espo412@gmail.com", "7aeESWAwHN3D")
        server.sendmail(sender, receivers, message)
        print "Successfully sent email"
    except smtplib.SMTPException:
        print "Error: unable to send email"
        

sender = 'espo412@gmail.com'
receivers = ['emilio@serniacapital.com']
subject = "Sernia Capital Zillow Update"


# # Scrape Zillow continously

# In[4]:

import requests
import datetime
from bs4 import BeautifulSoup
 

url = 'http://www.zillow.com/homedetails/320-S-Mathilda-St-APT-12-Pittsburgh-PA-15224/2097514490_zpid/?view=public'
# url = 'http://www.zillow.com/homedetails/324-S-Mathilda-St-APT-12-Pittsburgh-PA-15224/2098920770_zpid/'
# url = 'http://www.zillow.com/homedetails/332-S-Mathilda-St-APT-02-Pittsburgh-PA-15224/2097352140_zpid/?view=public'

response = requests.get(url)

html_doc = response.content
soup = BeautifulSoup(html_doc, 'html.parser')

status_tag = soup.find("div", { "class" : "estimates" })
status_text = status_tag.text

body = "null"
offmarket = False
if "For Rent" in status_text:
    body = "The apartment is still For Rent..."+str(datetime.datetime.now())+"\n"
#    mySendMail(sender, receivers, subject, body)
elif "Off Market" in status_text:
    body = "\n**UPDATE\nThe apartment is now Off Market!"+str(datetime.datetime.now())+"\n" + url
    mySendMail(sender, receivers, subject, body)
print body
    

# In[ ]:



