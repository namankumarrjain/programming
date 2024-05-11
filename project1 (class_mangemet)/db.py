import mysql.connector 

con=mysql.connector.connect(host="localhost",user="root",password="")
cursor=con.cursor()

query1="create database class"
cursor.execute(query1)

query2="use class"
cursor.execute(query2)

query3="create table monitor(roll varchar(5),name varchar(50),month varchar(20))"
cursor.execute(query3)

query4="create table marks (roll varchar(5),name varchar(50),s1 int , s2 int , s3 int , total int , per float , term varchar(20))"
cursor.execute(query4)

query5="create table att(date varchar(10) , abs varchar(500))"
cursor.execute(query5)

query6="create table student(roll varchar(5),name varchar(50),phone varchar(20), address varchar(50))"
cursor.execute(query6)

con.commit()

