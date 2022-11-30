

from ast import Delete, If
from multiprocessing import connection
from sqlite3 import Cursor, connect
import mysql.connector
from datetime import date
import time
import time
import sys
import time
print('*****ONLY FOR THE STAFF*****')
count=0
while count <4:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='viju' and username=='viju':
        print('Access granted')
        break
    elif password!='viju' and username!='viju':
          print('Try again!!')
          sys.exit()
          
          break        
    else:
        print('Access denied.')
        count += 1
        time.sleep(2)
        sys.exit()


def clear():
  for _ in range(2):
     print()


def introduction():
    msg = '''
          **S T U D E N T  A L U M N I  D A T A B A S E** 
          
          - An Introduction
          
          Alumni are the most important part of any education system. Alumni database help us to recognise the
          best brains educated by the institue and every big education system keep a record of them. 

          This project is also trying to solve this simple but very useful information of their alumni. The whole 
          database is store in MySQL table alumni that stores their current position as well as some other useful
          information like higher education, current position, passout year etc.

          The whole project is divided into four major parts ie addition of data, modification, searching and 
          reporting. all these part are further divided into menus for easy navigation

          \n\n\n\n'''
    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')


def made_by():
    msg = ''' 
            STUDENT ALUMNI DATABASE made by         : Vijay Govindrao Kathole
            Roll No                                 : 15
            School Name                             : SRTMU,Nanded
            faculty Name                            : M.Sc Computer Science (2nd Year)
            session                                 : 2021-22
            
            Thanks for evaluating my Project.
            \n\n\n
        '''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)

    wait = input('Press any key to continue.....')





def record_exists(name,fname,dob):
    conn = mysql.connector.connect(
      host='localhost', database='alumni', user='root', password='1234')
    cursor = conn.cursor()
    sql ='select * from alumni where name ="'+name +'" and fname ="'+fname+'"  and dob ="'+dob+'";'
    cursor.execute(sql)
    record = cursor.fetchone()
    return record

def add_alumni():
  conn = mysql.connector.connect(
      host='localhost', database='alumni', user='root', password='1234')
  cursor = conn.cursor()
  clear()
  name = input('Enter Alumni Name  : ').upper()
  fname = input('Enter Alumni Father Name  : ').upper()
  dob = input('Enter Alumni Date Of birth(yyyy/mm/dd) : ')
  phone = input('Enter Alumni Phone No  : ')
  email = input('Enter Alumni Email ID  : ')
  stream = input('Enter Alumni Stream(passed)  : ').upper()
  pass_year = input('Enter Alumni Pass Year : ')
  quali = input('Enter Alumni Highest Qualification : ').upper()
  position = input('Enter Alumni Current Position : ')
  city= input('Enter Alumni Current City : ').upper()
  country= input('Enter Alumni Current Country : ').upper()
  employ= input('Enter Alumni Currently employeed/Business : ')

  sql ='insert into alumni(name,fname,phone,email,stream,pass_year,hqualification,\
          current_position,dob,c_city,c_country,employement) values(\
          "'+name+'","'+fname+'","'+phone+'","'+email+'","'+stream+'","'+pass_year+'","'+quali+'","'+position+'","'\
          +dob+'","'+city+ '","'+country+'","'+employ+'");'
  result = record_exists(name,fname,dob)
  if result is None:
    cursor.execute(sql)
    print('\n\n\n Alumni database added successfully.....')
  else:
    print('\n\n\n Record already exist.....................')
  conn.close()
  wait = input('\n\n\n Press any key to continue....')
  
  
def delete_alumni():
      import mysql.connector as c
      con =c.connect(host="localhost", database="alumni", user="root", password="1234")
      cursor=con.cursor()
      id=int(input("Enter alumni id to Delete:"))
      query="delete from alumni where id={}".format(id)
      cursor.execute(query)
      con.commit()
      if cursor.rowcount>0:
        print ("Deletion Successfull..")
      else:
        print ("alumni id not Found")   
      wait = input('\n\n\n Record deleted.........Press any key to continue....')
    





def modify_alumni():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='1234')
    cursor = conn.cursor()
    while True:
        clear()
        print('STUDENT ALUMNI DATABASE MODIFICATION MENU')
        print('*'*100)
        print('1.   Correction In Name')
        print('2.   Correction In Father Name')
        print('3.   Correction In Phone No')
        print('4.   Correction In Email ID')
        print('5.   Correction In Stream')
        print('6.   Correction In Pass Year')
        print('7.   Correction In Highest Qualification')
        print('8.   Correction In Current Position')
        print('9.   Correction In Current City')
        print('10.  Correction In Current Country')
        print('11.   Back to main Menu')
        choice = int(input('\n\nEnter your choice : '))
        field_name =''
        if choice ==1:
            field_name='name'
        if choice == 2:
            field_name = 'fname'
        if choice == 3:
            field_name = 'phone'
        if choice == 4:
            field_name = 'email'
        if choice == 5:
            field_name = 'stream'
        if choice ==6:
            field_name='pass_year'
        if choice ==7:
            field_name='hqualification'
        if choice ==8:
            field_name='current_position'
        if choice == 9:
            field_name = 'c_city'
        if choice == 10:
            field_name = 'c_country'
        if choice == 11:
          conn.close()
          break
        clear()
        print('Change Value for ',field_name)
        print('*'*100)
        idr= input('Enter alumni ID :')
        value = input('Enter new Value :')
        sql = 'update alumni set '+field_name +'="'+ value +'" where id = '+idr+';' 
        cursor.execute(sql)
        wait = input('\n\n\n Record updated.........Press any key to continue....')
    
    conn.close()
       

def search_menu():
    conn = mysql.connector.connect(
       host='localhost', database='alumni', user='root', password='1234')
    cursor = conn.cursor()
    while True:
      clear()
      print(' S E A R C H    M E N U')
      print('*'*100)
      print("\n1.   ID")
      print('\n2.   Name')
      print('\n3.   Father Name')
      print('\n4.   Phone No')
      print('\n5.   Email')
      print('\n6.   stream')
      print('\n7.   pass year')
      print('\n8.   Qualification')
      print('\n9.   Position')
      print('\n10.  City')
      print('\n11.  Country')
      print('\n12.  Employment')
      print('\n13.  Back to Main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      field_name=''
   
      if choice == 1:
        field_name ='id'
      if choice == 2:
        field_name ='name'
      if choice == 3:
        field_name = 'fname'
      if choice == 4:
        field_name = 'phone'
      if choice == 5:
        field_name = 'email'
      if choice == 6:
        field_name = 'stream'
      if choice == 7:
        field_name = 'pass_year'
      if choice == 8:
        field_name = 'hqualification'
      if choice == 9:
        field_name = 'current_position'
      if choice == 10:
        field_name = 'c_city'
      if choice == 11:
        field_name = 'c_country'
      if choice == 12:
        field_name = 'employement'
      if choice == 13:
        break
      msg ='Enter '+field_name+': '
      value = input(msg)
      if field_name=='id':
        sql = 'select * from alumni where '+field_name + ' = '+value+';'
      else:
        sql = 'select * from alumni where '+field_name +' like "%'+value+'%";'
      #print(sql)
      cursor.execute(sql)
      records = cursor.fetchall()
      n = len(records)
      clear()
      print('Search Result for ', field_name, ' ',value)
      print('-'*120)
      for record in records:
       print(record[0], record[1], record[2], record[3],
             record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12])
      if(n <= 0):
        print(field_name, ' ', value, ' does not exist')
      wait = input('\n\n\n Press any key to continue....')

    conn.close()
    wait=input('\n\n\n Press any key to continue....')


def report_alumni_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='1234')
    cursor = conn.cursor()
    sql ="select * from alumni"
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni List')
    print('_'*140)
    print('{:10s} {:30s} {:30s} {:15s} {:30s} {:20s}'.format(
        'ID', 'Name', 'Father Name','Email','Phone','Position'))
    print('_'*140)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:30s} {:20s}'.format(
          record[0], record[1], record[2], record[4],record[3],record[8]))

    print('_'*140)

    conn.close()
    wait=input('\n\n\n Press any key to continue....')

def year_wise_alumni():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='1234')
    cursor = conn.cursor()
    year1 = input(' Enter passout year :')
    sql = 'select * from alumni where pass_year like "%'+ year1 +'%";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni List Passout Year : ',year1)
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Phone', 'Position'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[4], record[8]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def alumni_email_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='1234')
    cursor = conn.cursor()
    year1 = input(' Enter passout year :')
    sql = 'select * from alumni;'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni Email List')
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email','Position'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[8]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def alumni_phone_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='1234')
    cursor = conn.cursor()
    sql = 'select * from alumni;'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni Phone Numbers List')
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email','Phone','Position'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[4],record[3] ,record[8]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def city_wise_alumni_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='1234')
    cursor = conn.cursor()
    city = input(' Enter city Name :')
    sql = 'select * from alumni where c_city="'+city+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni City Wise List :',city )
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Position','City'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[8],record[10]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def country_wise_alumni_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='1234')
    cursor = conn.cursor()
    cntry = input(' Enter country Name :')
    sql = 'select * from alumni where c_country="'+cntry+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni City Wise List :',cntry )
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Position','Country'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[8],record[11]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def position_wise_alumni_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='1234')
    cursor = conn.cursor()
    pos = input(' Enter position Name :')
    sql = 'select * from alumni where position="'+pos+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni position List :',pos )
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Position','Country'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[8],record[11]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def education_wise_alumni_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='1234')
    cursor = conn.cursor()
    edu = input(' Enter education Name :')
    sql = 'select * from alumni where heducation="'+edu+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni Education List :',edu )
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Education','Country'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[7],record[11]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')




def report_menu():
    while True:
      clear()
      print('STUDENT A L U M N I    R E P O R T    M E N U ')
      print('*'*120)
      print("\n1.   Alumni List")
      print('\n2.   Year wise Alumni')
      print('\n3.   Alumni Email List')
      print('\n4.   Alumni Phone NO')
      print('\n5.   City wise')
      print('\n6.   Country Wise')
      print('\n7.   Position Wise Report')
      print('\n8.   Higher Qualification Wise Report')
      print('\n9.   Back to Main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        report_alumni_list()
      if choice == 2:
        year_wise_alumni()
      if choice == 3:
        alumni_email_list()
      if choice == 4:
        alumni_phone_list()
      if choice == 5:
        city_wise_alumni_list()
      if choice == 6:
        country_wise_alumni_list()
      if choice == 7:
        position_wise_alumni_list()
      if choice == 8:
        education_wise_alumni_list()
      if choice == 9:
        break


def main_menu():
    clear()
    #introduction()
    while True:
      clear()
      print(' S T U D E N T  A L U M N I  D A T A B A S E')
      print('*'*100)
      
      print("\n1.  Add New Alumni Account")
      print('\n2.  Modify STUDENT ALUMNI DATABASE')
      print('\n3.  Search Alumni Menu')
      print('\n4.  Report Alumni Menu')
      print('\n5.  delete_Alumni')
      print('\n6.  upload photos')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        add_alumni()
      if choice == 2:
        modify_alumni()
      if choice == 3 :
        search_menu()
      if choice == 4:
        report_menu()
      if choice == 5:
       delete_alumni()
      
      if choice ==6:
          break

if __name__=="__main__":
      main_menu()
      
      
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="alumni")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE  IF NOT EXISTS Images (id INTEGER(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, Photo LONGBLOB NOT NULL)")

def InsertBlob(FilePath):
    with open(FilePath, "rb") as File:
        BinaryData = File.read()
    SQLStatement = "INSERT INTO Images(photo) VALUES (%s)"
    mycursor.execute(SQLStatement, (BinaryData,) )
    mydb.commit()
    
def RetrieveBlob(ID):
    SQLStatement2 = "SELECT * FROM Images WHERE id = '{0}'" 
    mycursor.execute(SQLStatement2.format(str(ID)))
    myResult = mycursor.fetchone()[1]
    StoreFilePath = "C:/Users/Viju/Desktop/t5/imageOutputs/img{0}.jpg".format(str(ID))
    print(myResult)   
    with open(StoreFilePath, "wb") as File:
        File.write(myResult)
        File.close()
        
    
print("1. Insert Image\n2. Read Image")
MenuInput = input()
if int(MenuInput) == 1:
    UserFilePath = input("Enter File Path:")
    InsertBlob(UserFilePath)
elif int(MenuInput) ==2:
    UserIDchoice = input("Enter ID:")
    RetrieveBlob(UserIDchoice)
    
def main_menu():
    clear()
    #introduction()
    while True:
      
      print("photos upload successfully.........")
      print('\n\n')
      print('*'*100)
      print('*'*100)
      print(' STUDENT ALUMNI DATABASE.....\n\n','*** VIJAY KATHOLE ***')
      print('*'*100)
      print('*'*100)
      
      print("\n1.close application")
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice ==1:
          break
if __name__=="__main__":
      main_menu()
      made_by()
