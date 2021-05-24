import pymysql

hostname = 'aa100b8g7kab2pc.cgsawl0mfq5k.us-east-1.rds.amazonaws.com'
username = 'abhishek'
password = 'cclabdemo'

# Connect to the databaset
con = pymysql.connect(host=hostname, user=username, password=password)

# Checking connection
cur = con.cursor()
temp = cur.execute('select version()')
data = cur.fetchone()
print(data)

# Creating the database
query_1 = 'CREATE DATABASE abhishek'
cur.execute(query_1)
cur.connection.commit()

# Creating the table
query_2 = 'USE abhishek'
query_3 = '''CREATE TABLE New_Users (
    Personid int not NULL AUTO_INCREMENT,
    username varchar(255),
    password varchar(255),
    age INT,
    mobile_number varchar(10),
    PRIMARY KEY (Personid)
);'''

cur.execute(query_2)
cur.execute(query_3)
cur.connection.commit()

# To check if it works
query_4 = 'INSERT INTO New_Users(username,password,age,mobile_number) VALUES ("abhishek", "pass", "pass123", 20);'
query_5 = 'SELECT * FROM New_Users;'
cur.execute(query_4)
cur.connection.commit()
cur.execute(query_5)
print(cur.fetchall())
