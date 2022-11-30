import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root', password='1234')
print(mydb)
'''
if (mydb):
    print("d")
else:
    print('g')
'''

############################################################################################
############################################################################################
##############    CREATE DATABASE       ##########################################

import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root', password='1234')

mycursor =mydb.cursor()
mycursor.execute("CREATE databases vijay")
mycursor.execute("show databases")
'''
for db in mycursor:
    
    print(db)
'''
########################################################################################
#######################      CREATE TABLES   ############################################

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="fd")
mycursor = mydb.cursor()
#create table alumni ( id int(11) primary key auto_increment, name  char(30), fname char(30), email char(30), stream char(30),pass_year  char(4), hqualification char(40), current_position char(30), dob date, c_city char(30),c_country  char(30), employement  char(30) );

mycursor.execute("CREATE TABLE alumni ( id int(11) primary key auto_increment, name  char(30), fname char(30), email char(30), stream char(30),pass_year  char(4), hqualification char(40), current_position char(30), dob date, c_city char(30),c_country  char(30), employement  char(30) )" )

mycursor.execute("CREATE TABLE IF NOT EXISTS images (id INTEGER(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, Photo LONGBLOB NOT NULL)")

'''
mycursor.execute("Show tables")
for tb in mycursor:
    print(tb)
'''

#########################


