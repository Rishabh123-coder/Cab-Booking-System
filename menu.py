import pickle as p


def adminLogin():
	a_name=input("Enter the name of the admin :")
	a_password=input("Enter the password :")

	file=open("admin.txt","rb")
	d3=p.load(file)

	file.close()
	c=0
	for i in d3:
		if d3[i][0] == a_name and d3[i][1] == a_password:
			c=1
	if c==1:
		print("login successfully")
		login()
	else:
		print("INVALID USERNAME OR PASSWORD")

def login():
			
	print(
		'''
		1. VIEW DEALER
		2. DELETE DEALER
		3. VIEW USER
		4. DELETE USER
		5. VIEW CABS
		6. DELETE CABS
		7. CHANGE PASSWORD
		8. ALL REQUEST
		9. LOGOUT 
		'''
		)
	ch=str(input("Enter your choice :"))
	if ch=="1":
		viewDealer()
	elif ch=="2":
		del_dealer()
	elif ch=="3":
		viewUser()
	elif ch=="4":
		del_user()
	elif ch=="5":
		viewCabA()
	elif ch=="6":
		deleteCabA()
	elif ch=="7":
		changePass()
	elif ch=="8":
		allRequest()
	elif ch=="9":
		logout()
	else:
		print("INVALID INPUT ")	
		login()


def allRequest():
	file=open("request.txt","rb")
	d=p.load(file)
	file.close()

	print("{0:<20} {1:<20} {2:<20} {3:20} {4:<20} {5:<20}".format("REQUEST ID","USER NAME","CAB ID","DEALER EMAIL","DEALER ID","USER ID"))
	for i,j in d.items():
		print("{0:<20} {1:<20} {2:<20} {3:20} {4:<20} {5:<20}".format(i,j[0],j[1],j[2],j[3],j[4]))
	login()


def viewUser():
	file=open("user1.txt","rb")
	d=p.load(file)
	file.close()
	# print(d)
	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format("USER ID","NAME","PASSWORD","EMAIL","PHONE NO"))
	for i,j in d.items():
		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format(i,j[0],j[1],j[2],j[3]))

	login()

def del_user():
	file=open("user1.txt","rb")
	d=p.load(file)
	file.close()
	
	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format("USER ID","NAME","PASSWORD","EMAIL","PHONE NO"))
	for i,j in d.items():
		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format(i,j[0],j[1],j[2],j[3]))

	ch=str(input("Enter the id :"))
	if ch>='0' and ch<='9':
		pass
	else:
		print("Invalid Input")
		del_user()

	for i in d.keys():
		if i==int(ch):
			a=i
			break

	d.pop(a)
	file=open("user1.txt","wb")
	p.dump(d,file)
	file.close()
	
	file=open("request.txt","rb")
	d1=p.load(file)
	file.close()

	for i,j in list(d1.items()):
		if j[4]==a:
			d1.pop(i)

	file=open("request.txt","wb")
	p.dump(d1,file)
	file.close()

	print("The user is deleted successfully")
	login()

def viewDealerA():
	file=open("dealer1.txt","rb")
	d=p.load(file)
	file.close()
	# print(d)
	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("DEALER ID","NAME","PASSWORD","EMAIL","PHONE NO","ADDRESS"))
	for i,j in d.items():
		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(i,j[0],j[1],j[2],j[3],j[4]))


def viewDealer():
	file=open("dealer1.txt","rb")
	d=p.load(file)
	file.close()
	# print(d)
	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format("DEALER ID","NAME","PASSWORD","EMAIL","PHONE NO","ADDRESS"))
	for i,j in d.items():
		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}".format(i,j[0],j[1],j[2],j[3],j[4]))

	login()

def del_dealer():
	file=open("dealer1.txt","rb")
	d=p.load(file)
	file.close()
	viewDealerA()

	ch=str(input("Enter the id :"))
	if ch>='0' and ch<='9':
		pass
	else:
		print("Invalid Input")
		del_dealer()
	for i in d.keys():

		if i==int(ch):
			a=i
			break

	d.pop(a)
	file=open("dealer1.txt","wb")
	p.dump(d,file)
	file.close()


	file=open("cab1.txt","rb")
	d1=p.load(file)
	file.close()
	for i,j in list(d1.items()):
		if j[1]==a:
			d1.pop(i)


	file=open("cab1.txt","wb")
	p.dump(d1,file)
	file.close()

			
	file=open("request.txt","rb")
	d2=p.load(file)
	file.close()
	for i,j in list(d2.items()):
		if j[3]==a:
			d2.pop(i)

	file=open("request.txt","wb")
	p.dump(d2,file)
	file.close()

	print("Dealer deleted successfully")
			
	login()

def dealerRegistration():

	file=open("dealer1.txt","rb")
	d=p.load(file)
	d_id=len(d)+1
	file.close()

	d_name=input("Enter the name of the dealer :")
	d_password=input("Enter the password of the dealer :")
	d_email=input("Enter the email of the dealer :")
	while True:
		d_phno=str(input("Enter the phone no of the dealer :"))
		if d_phno>='0' and d_phno<='9':
			break
		else:
			print("Invalid Input")
			
	d_addr=input("Enter the address of the dealer :")

	file=open("dealer1.txt","wb")
	
	d[d_id]=[d_name,d_password,d_email,d_phno,d_addr]
	p.dump(d,file)
	file.close()
	print("Dealer registered successfully")
	init()


def dealerLogin():
	file=open("dealer1.txt","rb")
	d=p.load(file)
	file.close()
	print(d)

	d_email=input("Enter the email of the dealer :")
	while True:
		d_id=str(input("Enter the id of the dealer :"))
		if d_id>='0' and d_id<='9':
			break
		else:
			print("INVALID Input")

	flag=0
	for i,j in d.items():
		if d_email == j[2] and int(d_id) == i:
			flag=1

	if flag==1:
		print("login successfully")
		login1(d_email,d_id)
	else:
		print("invalid Email or id ")
		
def login1(d_email,d_id):	
		print('''
		1. ADD CAB
		2. VIEW CAB
		3. DELETE CAB
		4. CHANGE PASSWORD
		5. LOGOUT
		6. SEE REQUEST
		''')
		ch = str(input("Enter your choice :"))
		if ch=="1":
			addCab(d_email,d_id)
		elif ch=="2":
			viewCab()
		elif ch=="3":
			deletecab()
		elif ch=="4":
			change_pass()
		elif ch=="5":
			logout()
		elif ch=="6":
			seeRequest()
		else:
			print("Invalid Input")
	

def seeRequest():
	file=open("request.txt","rb")
	d=p.load(file)
	file.close()

	d_email=input("verify your Email :")

	d1={}
	for i,j in d.items():
		if d_email==j[2]:
			d1[i]=j
			d_id=j[3]

	print("{0:<20} {1:<20} {2:<20} {3:20} {4:<20} {5:<20}".format("REQUEST ID","USER NAME","CAB ID","DEALER EMAIL","DEALER ID","USER ID"))
	for i,j in d1.items():
		print("{0:<20} {1:<20} {2:<20} {3:20} {4:<20} {5:<20}".format(i,j[0],j[1],j[2],j[3],j[4]))
	
	login1(d_email,d_id)


def addCab(d_email,d_id):
	file=open("cab1.txt","rb")
	d2=p.load(file)
	print(d2)
	c_id=len(d2)+1
	file.close()

	c_name=input("Enter the name of the cab :")
	c_type=input("Enter the type of the cab :")
	c_from=input("The cab starts from :")
	c_to=input("The cab ends to :")
	while True:
		c_status=str(input("The cab status :"))
		if c_status=='0' or c_status=='1':
			break
		else:
			print("INVALID INPUT")

	file=open("cab1.txt","wb")
	d2[c_id]=[d_email,d_id,c_name,c_type,c_from,c_to,c_status]
	p.dump(d2,file)
	file.close()

	file=open("cab1.txt","rb")
	print(p.load(file))
	file.close()
	login1(d_email,d_id)

def logout():
	init()	

def change_pass():
	file=open("dealer1.txt","rb")
	d=p.load(file)
	file.close()

	e_pass=input("Enter the password :")
	new_pass=input("Enter the new password :")

	for i,j in d.items():
		if j[1]==e_pass:
			j[1]=new_pass
			file=open("dealer1.txt","wb")
			p.dump(d,file)
			file.close()
			d_email=j[2]
			d_id=i
			break
	
	print("The password is changed successfully")
	login1(d_email,d_id)

def changePass():
	file=open("admin.txt","rb")
	d=p.load(file)
	file.close()

	e_pass=input("Enter the password :")
	new_pass=input("Enter the new password :")

	for i in d.values():
		if i[1]==e_pass:
			i[1]=new_pass
			file=open("admin.txt","wb")
			p.dump(d,file)
			file.close()
			break
	
	print("The password is changed successfully")
	login()


def viewCab():
	file=open("cab1.txt","rb")
	d3=p.load(file)
	file.close()

	d_email=input("verify the email :")
	d1={}
	for i,j in d3.items():
		if d_email == d3[i][0]:
			d1[i]=j
			d_id=j[1]
	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format("CAB ID","DEALER EMAIL","DEALER ID","NAME","TYPE","FROM","TO","STATUS"))
	for i,j in d1.items():
		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format(i,j[0],j[1],j[2],j[3],j[4],j[5],j[6]))

	login1(d_email,d_id)


def viewCabD():
	file=open("cab1.txt","rb")
	d3=p.load(file)
	file.close()

	d_email=input("verify the email :")
	d1={}
	for i,j in d3.items():
		if d_email == d3[i][0]:
			d1[i]=j
			d_id=j[1]
	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format("CAB ID","DEALER EMAIL","DEALER ID","NAME","TYPE","FROM","TO","STATUS"))
	for i,j in d1.items():
		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format(i,j[0],j[1],j[2],j[3],j[4],j[5],j[6]))	

def deleteCabA():
	file=open("cab1.txt","rb")
	d3=p.load(file)
	file.close()
	viewCaB()
	ch=int(input("Enter the id to delete :"))
	# a=""
	for i,j in d3.items():
		if ch==i:
			a=i
			d_email=j[0]
			d_id=j[1]
			break
	d3.pop(a)
	print("cab deleted successfully")
	file=open("cab1.txt","wb")
	p.dump(d3,file)
	file.close()
	login()

def deletecab():
	file=open("cab1.txt","rb")
	d3=p.load(file)
	file.close()
	viewCab()
	ch=int(input("Enter the id to delete :"))
	# a=""
	for i,j in d3.items():
		if ch==i:
			a=i
			d_email=j[0]
			d_id=j[1]
			break
	d3.pop(a)
	print("cab deleted successfully")
	file=open("cab1.txt","wb")
	p.dump(d3,file)
	file.close()

	login1(d_email,d_id)

def userRegister():
	file=open("user1.txt","rb")
	d1=p.load(file)
	print(d1)
	u_id=len(d1)+1
	file.close()
	u_name=input("Enter the user name :")
	u_password=input("Enter the password :")
	u_email=input("Enter the email of user :")
	u_phoneno=str(input("Enter the phone no of the user :"))
	if u_phoneno>='0' and u_phoneno<='9':
		pass
	else:
		print("Invalid INPUT")
		userRegister()

	file=open("user1.txt","wb")
	d1[u_id]=[u_name,u_password,u_email,u_phoneno]
	p.dump(d1,file)
	file.close()
	print("The user is registered successfully")
	init()

def userLogin():
	file=open("user1.txt","rb")
	print(p.load(file))
	file.close()
	
	u_email=input("Enmter the email to check :")
	u_password=input("Enter the password to check :")
	file=open("user1.txt","rb")
	d1=p.load(file)
	c=0
	for i in d1:
		if u_email == d1[i][2] and u_password == d1[i][1]:
			u_name=d1[i][0]
			u_id=i
			c=1
			
	if c==1:
		print("login successfully")
		login2(u_name,u_id)
	else:
		print("incorrect username and password")

def login2(u_name,u_id):	
		print('''
				1. VIEW CAB
				2. SEARCH CAB
				3. BOOK CAB
				4. CANCLE BOOKING
				5. LOGOUT
			''')
		ch=str(input("Enter the choice :"))
		if ch=="1":
			viewCabU(u_name,u_id)
		elif ch=="2":
			searchCab(u_name,u_id)
		elif ch=="3":
			bookCab(u_name,u_id)
		elif ch=="4":
			cancleBook(u_name,u_id)
		elif ch=="5":
			logout()
		else:
			print("Invalid INPUT")
			login2(u_name,u_id)

def cancleBook(u_name,u_id):
	file=open("request.txt","rb")
	d=p.load(file)
	file.close()

	uName=input("Enter the user name :")
	c_id=str(input("Enter the cab id to cancel :"))
	if c_id>='0' and c_id<='9':
		pass
	else:
		print("Invalid INPUT")
		cancelBook(u_name,u_id)

	c=0
	for i,j in list(d.items()):
		if j[1]==c_id and j[0]==uName:
			d.pop(i)
			c=1
		else:
			print("Invalid user name or Id")
	if c==1:
		print("Cab is canceled successfully")
	else:
		print("No cab is booked")

	file=open("request.txt","wb")
	p.dump(d,file)
	file.close()

	login2(u_name,u_id)


def bookCab(u_name,u_id):
	
	file=open("request.txt","rb")
	d=p.load(file)
	file.close()

	id=len(d)+1

	file=open("cab1.txt","rb")
	d1=p.load(file)
	file.close()
	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format("CAB ID","DEALER EMAIL","DEALER ID","NAME","TYPE","FROM","TO","STATUS"))
	for i,j in d1.items():
		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format(i,j[0],j[1],j[2],j[3],j[4],j[5],j[6]))

	uName=input("Enter the name of the user :")
	c_id=str(input("Enter the cab id :"))
	if c_id>='0' and c_id<='9':
		pass
	else:
		print("Invalid INPUT")
		bookCab(u_name,u_id)

	d_id=str(input("Enter the dealer id :"))
	if d_id>='0' and d_id<='9':
		pass
	else:
		print("Invalid INPUT")
		bookCab(u_name,u_id)

	d_email=input("Enter the email of the dealer :")
	a=0
	c=0
	for i,j in d.items():
		if int(c_id)==j[1]:
			a=1
			break
	if a==1:
		print("The cab is already booked")
	else:
		for i,j in d1.items():
			if i==int(c_id) and j[0]==d_email and j[1]==int(d_id):
				if uName==u_name:
					c=1
				else:
					print("Invalid username")
			
		if c==1:	
			d[id]=[u_name,c_id,d_email,d_id,u_id]
			print("Your request is accepted")
		else:
			print("The cab is not available")
 
	
	
	file=open("request.txt","wb")
	p.dump(d,file)
	file.close()

	login2(u_name,u_id)

def viewCaB():
	file=open("cab1.txt","rb")
	d=p.load(file)
	file.close()
	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format("CAB ID","DEALER EMAIL","DEALER ID","NAME","TYPE","FROM","TO","STATUS"))
	for i,j in d.items():
		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format(i,j[0],j[1],j[2],j[3],j[4],j[5],j[6]))
	

def viewCabA():
	file=open("cab1.txt","rb")
	d=p.load(file)
	file.close()
	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format("CAB ID","DEALER EMAIL","DEALER ID","NAME","TYPE","FROM","TO","STATUS"))
	for i,j in d.items():
		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format(i,j[0],j[1],j[2],j[3],j[4],j[5],j[6]))
	login()

def viewCabU(u_name,u_id):
	file=open("cab1.txt","rb")
	d=p.load(file)
	file.close()

	file=open("user1.txt","rb")
	d1=p.load(file)
	file.close()
	

	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format("CAB ID","DEALER EMAIL","DEALER ID","NAME","TYPE","FROM","TO","STATUS"))
	for i,j in d.items():
		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format(i,j[0],j[1],j[2],j[3],j[4],j[5],j[6]))
	login2(u_name,u_id)


def searchCab(u_name,u_id):
	
	start=input("Enter the starting point :")
	end=input("Enter the ending point :")

	d1={}
	file=open("cab1.txt","rb")
	d=p.load(file)
	file.close()

	file=open("user1.txt","rb")
	d2=p.load(file)
	file.close()
	for i in d2.values():
		u_name=i[0]

	for i,j in d.items():
		if d[i][4]==start and d[i][5]==end:
			d1[i]=j
	
	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format("CAB ID","DEALER EMAIL","DEALER ID","NAME","TYPE","FROM","TO","STATUS"))
	for i,j in d1.items():
		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20} {7:<20}".format(i,j[0],j[1],j[2],j[3],j[4],j[5],j[6]))

	login2(u_name,u_id)
	# print(d1)



def init():
	print('''
		CAB BOOKING 

		  1. ADMIN LOGIN
		  2. USER REGISTRATION
		  3. USER LOGIN
		  4. DEALER REGISTRATION
		  5. DEALER LOGIN
		  6. EXIT

		''')
	a=str(input("ENTER YOUR CHOICE :"))

	if a=="1":
		adminLogin()
	elif a=="2":
		userRegister()
	elif a=="3":
		userLogin()
	elif a=="4":
		dealerRegistration()
	elif a=="5":
		dealerLogin()
	elif a=="6":
		exit()
	else:
		print("Invalid Input")
		init()

	
init()                 