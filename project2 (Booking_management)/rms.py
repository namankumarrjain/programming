import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="rms")

def checkin(): 
	d=input("Days : ")
	g=input("Names :")
	a=input("Adhar card : ")
	dt=input("Date : ")
	b=input("Type & Number : ")
	
	data=(d,g,a,dt,b)
	
	query="Insert into checkin values(%s,%s,%s,%s,%s)"
	
	cursor=con.cursor()
	cursor.execute(query,data)
	
	con.commit()
	
	print("Data entered successfully")
	main()

def checkout(): 
	b=input("Type & Number : ")
	tg=int(input("Guests : "))
	f=int(input("Fare : "))
	d=int(input("Days : "))
	bl=f*d*tg
	cod=input("Date : ")
	
	data=(b,tg,f,d,bl,cod)
	
	query='Insert into checkout values(%s,%s,%s,%s,%s,%s)'
	
	cursor=con.cursor()
	cursor.execute(query,data)
	
	con.commit()
	
	print("Data entered successfully")
	main()

def rooms(): 
	print("Executive - 5000")
	print(" ")
	print(""" Facilities-wifi , TV , AC , Bathroom with Tub and Geyser , Breakfast , lunch, dinner""")
	print(" ")

	print("Deluxe - 2500")
	print(" ")
	print(""" Facilities-wifi , TV , AC , Bathroom with Tub and Geyser """)
	print(" ")

	print("Simple - 1000")
	print(" ")
	print(""" Facilities-wifi , TV , AC , Bathroom with Geyser""")
	
	main()


def main(): 
	while True: 

		print(""" 
			1. check in 
			2. check out 
			3. Fare and Amenities
			4. Exit
			""")
		c=int(input("choice : "))

		if c==1: 
			checkin()
		elif c==2: 
			checkout()
		elif c==3: 
			rooms()
		elif c==4: 
			print("Thank! you...")
			break 
		else: 
			print("please enter the correct choice")

main()
