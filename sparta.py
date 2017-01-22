import xlrd
import smtplib
import MySQLdb
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
to=[]
name=[]
age=[]
income=[]
db=MySQLdb.connect("localhost","root","","Blog")
cursor=db.cursor()
zip=0
try:
    cursor.execute("Select * from subscribers")
    results = cursor.fetchall()
    for row in results:
        city.append(row[0])
        phonen.append(row[1])
        carrier.append(row[2])
        #print name,age,income
except:
    print "Error:unable to fetch data"
db.close()
for i in range(sheet.nrows):
    to.append(data[2][i])
    if carrier[i][3]=="Altel":
        temp=to.pop()
        temp=temp[:len(temp)]+"@sms.alltelwireless.com"
        to.append(temp)
    elif carrier[i][3]=="AT&T":
        temp=to.pop()
        temp=temp[:len(temp)]+"@txt.att.net"
        to.append(temp)
    elif carrier[i][3]=="Boost Mobile":
        temp=to.pop()
        temp=temp[:len(temp)]+"@sms.myboostmobile.com"
        to.append(temp)
    elif carrier[i][3]=="Consumer Cellular":
        temp=to.pop()
        temp=temp[:len(temp)]+"@cingularme.com"
        to.append(temp)
    elif carrier[i][3]=="Cricket Wireless":
        temp=to.pop()
        temp=temp[:len(temp)]+"@sms.mycricket.com"
        to.append(temp)
    elif carrier[i][3]=="Google Fi":
        temp=to.pop()
        temp=temp[:len(temp)]+"@msg.fi.google.com"
        to.append(temp)
    elif carrier[i][3]=="Metro PCS":
        temp=to.pop()
        temp=temp[:len(temp)]+"@mymetropcs.com"
        to.append(temp)
    elif carrier[i][3]=="Sprint":
        temp=to.pop()
        temp=temp[:len(temp)]+"@messaging.sprintpcs.com"
        to.append(temp)
    elif carrier[i][3]=="T-Mobile":
        temp=to.pop()
        temp="1"+temp[len(temp):]+temp[:len(temp)]+"@tmomail.net"
        to.append(temp)
    elif carrier[i][3]=="U.S. Cellular":
        temp=to.pop()
        temp=temp[:len(temp)]+"@email.uscc.net"
        to.append(temp)
    elif carrier[i][3]=="Verizon":
        temp=to.pop()
        temp=temp[:len(temp)]+"@vtext.com"
        to.append(temp)
    elif carrier[i][3]=="Virgin Mobile":
        temp=to.pop()
        temp=temp[:len(temp)]+"@vmobl.com"
        to.append(temp)
    else:
        continue

fromaddr = "thedogoodproject2k17@gmail.com"
toaddr = "12134217070@m@tmomail.net"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "FREE FOOD"
body = "MSU, East Lansing  "
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Dogoodsparta")
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()
