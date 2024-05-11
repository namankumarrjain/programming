import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="",database="class")
cursor=con.cursor()

def monitor(): 
	o=int(input("1. Update Monitor 2. Check Monitor \n"))
	if o==1: 
		r=input("Enter student roll : ")
		n=input("Enter student name : ")
		c=input("Enter month : ")
		data=(r,n,c)
		query='Insert into monitor value(%s,%s,%s)'
		cursor=con.cursor()
		cursor.execute(query,data)
		con.commit()
		print("Data entered successfully")
		main()
	else: 
		query="select*from monitor"
		cursor=con.cursor()
		cursor.execute(query)
		d=cursor.fetchall()
		for i in d: 
			print(i)
		main()

def marks():
	o=int(input("1. Update Marks   2. Check Marks \n"))
	if o==1:
		r=input("Enter student roll : ")
		n=input("Enter student name : ")
		s1=float(input("subject 1 : "))
		s2=float(input("subject 2 : "))
		s3=float(input("subject 3 : "))
		t=s1+s2+s3
		per=(t/300)*100
		term=input("Enter term : ")
		data=(r,n,s1,s2,s3,t,per,term)
		query='Insert into marks values(%s,%s,%s,%s,%s,%s,%s,%s)'
		cursor=con.cursor()
		cursor.execute(query,data)
		con.commit()
		print("Data update successfully....")
		main()
	else: 
		r=input("enter roll :")
		t=input("enter terms : ")
		query="select*from marks where roll=%s and term=%s"
		cursor=con.cursor()
		cursor.execute(query,(r,t))

		for i in cursor: 
			print(i) 
		main()

def att(): 
	o=int(input("1. Update Attendence 2. Check Attendence \n"))
	if o==1: 
		d=input("enter date : ")
		ab=input("enter roll numbers : ")
		data=(d,ab)
		query="Insert into att values(%s,%s)"
		cursor=con.cursor()
		cursor.execute(query,data)
		print("Data entered successfully....")
		main()

	else: 
		query="select*from att"
		cursor=con.cursor()
		cursor.execute(query)
		d=cursor.fetchall()
		for i in d: 
			print(i)
		main()

def student(): 
	o=int(input("1. Update Details  2. Check Details \n"))
	if o==1: 
		r=input("enter students roll : ")
		n=input("enter students name : ")
		p=input("enter phone : ")
		a=input("enter address : ")
		data=(r,n,p,a)
		query='Insert into student values(%s,%s,%s,%s)'
		cursor=con.cursor()
		cursor.execute(query,data)
		con.commit()
		print("Data entered successfully")
		main()
	else: 
		query="select*from student"
		cursor=con.cursor()
		cursor.execute(query)
		d=cursor.fetchall()
		for i in d: 
			print(i)
		main()


def main(): 
	print(""" 
	1. Monitor 
	2. Report Card 
	3. Attendence 
	4. student 
	5. exit
	""")
	choice=input("Enter task no : ")
	while True: 
		if(choice=='1'): 
			monitor()
		elif(choice=='2'): 
			marks()
		elif(choice=='3'): 
			att() 
		elif(choice=='4'): 
			student()
		elif(choice=='5'): 
			print("Thank you")
			break
		else: 
			print("wrong choice......")
main()
