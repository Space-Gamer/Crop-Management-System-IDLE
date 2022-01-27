def run():
    try:
        import mysql.connector as ml
        mycon=ml.connect(host='localhost',user='root',passwd='#pass',)
        cur=mycon.cursor()
        cur.execute('drop database if exists project')
        cur.execute('create database project')
        try:
            print("Table creation in progress. Please wait...")
            cur.execute('use project')
            cur.execute("create table farmerlogin(F_ID int(5) primary key,F_NAME VARCHAR(30),F_PASS varchar(30),E_mail varchar(30) unique,Phone bigint unique,Game char(20),Native char(50),FAV_COLOR char(30))")
            cur.execute("insert into farmerlogin values(1,'ADMIN','welcome2python','',0,'','','')")
            cur.execute('create table status(C_ID int(7) PRIMARY KEY,F_ID int(5),Date_of_sowing date,Crop_Name varchar(225),Status varchar(255),Update_on DATETIME NOT NULL default NOW())')
            cur.execute("insert into status values(1001,1,'2000-01-01','Sample','Sample',now())")
            mycon.commit()
            mycon.close()
            print("Database and table successfully created")
        except:
            print("Table creation error.")
    except:
        print('Error connecting to mysql')
