import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="")

cursor=con.cursor()

query1="create database rms"
cursor.execute(query1)

query2="use rms"
cursor.execute(query2)

query3="create table checkin (day varchar(50), names varchar(20),adhar varchar(20),date varchar(20),typenumber varchar(20))"
cursor.execute(query3)

query4="create table checkout (typenumber varchar(20),guests integer, fare integer, days integer , tbill integer ,date varchar(20))"
cursor.execute(query4)

con.commit()
