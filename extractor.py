
#Author: Arbin Khadka
#Mail: arbin.khadka10@gmail.com


#Purpose: Extract the Log messages of appications from elasticsearch and send emails to specified mail address 

import json
import objectpath
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import date

recipients = ['receipents@email.com'] #Insert the REcepeints email address

#This function sends mail
def sendMail():
    sender_email = "sender@email.com" #Insert Sender Email Address
    email_password = "passwordText" #Enter senders email's password
    today = date.today()
    todayDate= today.strftime("%B %d, %Y")
    message = MIMEMultipart()

    message["From"] = sender_email
    message['To'] =  ", ".join(recipients)
    message['Subject'] = "Log report of "+ todayDate
    body = "Dear people,\n\nPlease find the Log report from Applications of " + todayDate +" attached with this mail\n\nThank you \n\n\nRegards,\nLog Extractor Bot"
    body = MIMEText(body, 'plain') 
    message.attach(body)

    files = ["filename.txt","filename2.txt"] #Insert Files to be attached
    for file in files:
        attachment = open(file,'rb')

        obj = MIMEBase('application','octet-stream')

        obj.set_payload((attachment).read())
        encoders.encode_base64(obj)
        obj.add_header('Content-Disposition',"attachment; filename= "+file)

        message.attach(obj)

    my_message = message.as_string()
    email_session = smtplib.SMTP('smtp.email.com',587) #Insert SMTP Details of Email
    email_session.starttls()
    email_session.login(sender_email, email_password)

    email_session.sendmail(sender_email,recipients,my_message)
    email_session.quit()
    
url = "http://domain.com:5601/kibana/internal/search/es" #Please insert your domain name
header ={
'Content-Type': 'application/json' ,   
'kbn-version': '7.10.2' 
}


#This function extracts the Error message from JSON file and writes in a text file
def extractError(httpData,filename):  

   
    resp = requests.post(url, headers=header, data=httpData, auth =('KibanaUsername','KibanaPassword'))  #Insert username and Password for Kibana
    outfile = filename + ".txt"
    data = resp.json()      
    messageList = []
    hit_tree = objectpath.Tree(data['rawResponse']['hits'])    
    messageList.append({"Total Count" : list(hit_tree.execute('$..total'))})   
    c=0
    for hits in data['rawResponse']['hits']['hits']:
        c = c + 1                 
        string = "Log " + str(c) + ": "   
        messageList.append({string : hits['_source']['message'].replace("\n"," ").replace("\t"," ") })
  
    
          
    with open(outfile, "w") as outfile:
        out_data = json.dumps(messageList, indent =2 )        
        outfile.writelines(out_data)



param1 = '{}'  #insert the Kibana request json parameter
param2 = '{}'  #insert the Kibana request json parameter
paramters = [param1,param2]
filenames = ["filename1", "filename2"]

c = 0
for parameter in paramters:   
    filename = filenames[c]
    extractError(parameter,filename)
    c +=1
sendMail()


        







