import smtplib
import MySQLdb
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText 

sid=[]
rname=[]
location=[]
title=[]
content=[]
db=MySQLdb.connect("localhost","root","","Blog")
cursor=db.cursor()
try:
    cursor.execute("Select * from blog_post")
    results = cursor.fetchall()
    for row in results:
        sid.append(row[0])
        rname.append(row[1])
        location.append(row[2])
        title.append(row[3])
        content.append(row[4])
        #print sid,rname,location,title,content
except:
    print "Error:unable to fetch post"
db.close()

uid=[]
city=[]
phoneno=[]
carrier=[]

db1=MySQLdb.connect("localhost","root","","Blog")
cursor=db1.cursor()
try:
    cursor.execute("Select * from subscribers")
    results = cursor.fetchall()
    for row in results:
        uid.append(row[0])
        city.append(row[1])
        phoneno.append(row[2])
        carrier.append(row[3])
        #print uid,city,phoneno,carrier
except:
    print "Error:unable to fetch carrier"
db1.close()
to=[]
for i in range(len(carrier)):
    to.append(phoneno[i])
    if carrier[i]=="Altel":
        temp=to.pop()
        temp=temp[:len(temp)]+"@sms.alltelwireless.com"
        to.append(temp)
    elif carrier[i]=="AT&T":
        temp=to.pop()
        temp=temp[:len(temp)]+"@txt.att.net"
        to.append(temp)
    elif carrier[i]=="Boost Mobile":
        temp=to.pop()
        temp=temp[:len(temp)]+"@sms.myboostmobile.com"
        to.append(temp)
    elif carrier[i]=="Consumer Cellular":
        temp=to.pop()
        temp=temp[:len(temp)]+"@cingularme.com"
        to.append(temp)
    elif carrier[i]=="Cricket Wireless":
        temp=to.pop()
        temp=temp[:len(temp)]+"@sms.mycricket.com"
        to.append(temp)
    elif carrier[i]=="Google Fi":
        temp=to.pop()
        temp=temp[:len(temp)]+"@msg.fi.google.com"
        to.append(temp)
    elif carrier[i]=="Metro PCS":
        temp=to.pop()
        temp=temp[:len(temp)]+"@mymetropcs.com"
        to.append(temp)
    elif carrier[i]=="Sprint":
        temp=to.pop()
        temp=temp[:len(temp)]+"@messaging.sprintpcs.com"
        to.append(temp)
    elif carrier[i]=="T-Mobile":
        temp=to.pop()
        temp="1"+temp[len(temp):]+temp[:len(temp)]+"@tmomail.net"
        to.append(temp)
    elif carrier[i]=="U.S. Cellular":
        temp=to.pop()
        temp=temp[:len(temp)]+"@email.uscc.net"
        to.append(temp)
    elif carrier[i]=="Verizon":
        temp=to.pop()
        temp=temp[:len(temp)]+"@vtext.com"
        to.append(temp)
    elif carrier[i]=="Virgin Mobile":
        temp=to.pop()
        temp=temp[:len(temp)]+"@vmobl.com"
        to.append(temp)
    else:
        continue
#print to
#print location
lo=location.pop()
for i in range(len(to)):
    fromaddr = "thedogoodproject2k17@gmail.com"
    toaddr = to[i]
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "FREE FOOD"
    body = str(lo[:len(lo)])+"  "
    #print body
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Dogoodsparta")
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()
