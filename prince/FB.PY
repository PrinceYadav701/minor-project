import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PRINCE98@YADAV"
)

mycursor=mydb.cursor()

mycursor.execute("create database mydatabase")