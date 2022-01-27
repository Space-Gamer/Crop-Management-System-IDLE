'''MySQL connection module'''
import sys
def connect():
    try:
        import mysql.connector as mp
        global mycon
        global cur
        mycon=mp.connect(host='localhost',user='root',passwd='#pass',database='project')
        cur=mycon.cursor()
        return 1
    except:
        print("Connection error. Please check if username and password are correct")
        return 0
def execute(strr):#only for  executing statements
    a=connect()
    if a==1:
        try:
            cur.execute(strr)
            mycon.commit()
            mycon.close()
        except:
            print("Execution error")
            mycon.close()
            sys.exit()
    elif a==0:
        print("Execution incomplete.")
        sys.exit()
def fetchone(strr):#for execute and read one line
    b=connect()
    if b==1:
        try:
            cur.execute(strr)
            a=cur.fetchone()
            mycon.close()
            return a
        except:
            print("Execution error")
            mycon.close()
            sys.exit()
    elif b==0:
        print("Execution incomplete.")
        sys.exit()
def fetchall(strr):#for executing and reading all outputs
   b=connect()
   if b==1:
       try:
            cur.execute(strr)
            dat=cur.fetchall()
            mycon.close()
            return dat
       except:
            print("Execution error")
            mycon.close()
            sys.exit()
   elif b==0:
        print("Execution incomplete.")
        sys.exit()
