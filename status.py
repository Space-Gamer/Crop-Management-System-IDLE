def run(f):
    def C_ID_Generator():
            a='select C_ID from status order by C_ID desc'
            dat=ml.fetchone(a)
            l=int(dat[0])
            return (l+1)
    def crops():
        a=int(input('''Choose crop:
                                1. Rice
                                2. Jowar
                                3. Ragi
                                4. Bajra
                                5. Wheat
                                6. Groundnut
                                7. Sugarcane
                                8. Sunflower
                                9. Mustard
                               10. Arhar(Tur)
                               11. Exit
                    ​
                Enter the crop: '''))
        return str(a)
    def check():
        b=len(dat)
        if b==0:
            print("    You haven't sown any crops yet")
            inp=input("    Enter 'Y' to create a crop status or enter any other key to exit: ")
            if inp=='y' or inp=='Y':
                a=2
            else:
                a=4
        else:
            for x6 in range(b):
                x5=dat[x6]
                print('    Your Crop is: ',)
                print('    The status of crop',x5[3],'with Crop_ID',x5[0],'was: \"',x5[4],'\" as of',x5[5])
                print()
            a=int(input('''
=====================================================================================================================================
        Available functions are:

                                                    1. Update crop status
                                                    2. Add crop
                                                    3. Delete crop
                                                    4. Exit

                                  Enter your choice: '''))
        return a
    while True:
        try:
            import mysqlconadv as ml
            x='Select distinct(Crop_Name) from status where F_ID="{}"'.format(f)
            data=ml.fetchall(x)
            y='Select * from status where F_ID="{}"'.format(f)
            dat=ml.fetchall(y)
            a=check()
            if a==1:
                b=len(data)
                if b>1:
                    print('-----------------------------------------------------')
                    print("    Select your crop: ")
                    for x6 in range(b):
                        x5=data[x6]
                        print(x6+1,'.',x5[0])
                    m1=int(input("    Choose your crop whose status is to be altered: "))
                    z=data[m1-1][0]
                else:
                    z=data[0][0]
                t='Select C_ID,Date_of_sowing from status where Crop_Name="{}" and F_ID="{}"'.format(z,f)
                da=ml.fetchall(t)
                if len(da)>1:
                    print('-----------------------------------------------------')
                    print("    Select your crop: ")
                    for j in range(len(da)):
                        print('Crop:',z)
                        x5=da[j]
                        print(j+1,'.','Crop_ID:',x5[0],'Date of sowing:',x5[1])
                    m1=int(input("    Choose your crop whose status is to be altered: "))
                    cid=da[m1-1][0]
                else:
                    cid=da[0][0]
                b=input('    Enter the status of the crop: ')
                c="update status set Status='{}',Update_on=now() where C_ID='{}'".format(b,cid)
                ml.execute(c)
                print()
                print('    Your crop status is set to: ',b)
            elif a==2:
                while True:
                    a=crops()
                    if a=='1':
                        a='Rice'
                    elif a=='2':
                        a='Jowar'
                    elif a=='3':
                        a='Ragi'
                    elif a=='4':
                        a=='Bhajra'
                    elif a=='5':
                        a='Wheat'
                    elif a=='6':
                        a='Groundnut'
                    elif a=='7':
                        a='Sugarcane'
                    elif a=='8':
                        a='Sunflower'
                    elif a=='9':
                        a='Mustard'
                    elif a=='10':
                        a='Tur'
                    elif a=='11':
                        break
                    x1="Sown the seeds"
                    cid=C_ID_Generator()
                    strr1='insert into status values("{}","{}",curdate(),"{}","{}",now())'.format(cid,f,a,x1)
                    ml.execute(strr1)
                    print("    Crop added successfully") 
                    break
            elif a==3:
                b=len(data)
                if b>1:
                    print('-----------------------------------------------------')
                    print("    Select your crop: ")
                    for x6 in range(b):
                        x5=data[x6]
                        print(x6+1,'.',x5[0])
                    m1=int(input("    Choose your crop whose status is to be deleted: "))
                    z=data[m1-1][0]
                else:
                    z=data[0][0]
                t='Select C_ID,Date_of_sowing from status where Crop_Name="{}" and F_ID="{}"'.format(z,f)
                da=ml.fetchall(t)
                if len(da)>1:
                    print('-----------------------------------------------------')
                    print("Select your crop: ")
                    for j in range(len(da)):
                        print('Crop:',z)
                        x5=da[j]
                        print(j+1,'.','Crop_ID:',x5[0],'Date of sowing:',x5[1])
                    m1=int(input("    Choose your crop whose status is to be deleted: "))
                    cid=da[m1-1][0]
                else:
                    cid=da[0][0]
                q="select * from status where C_ID='{}'".format(cid)
                p=ml.fetchone(q)
                print("    Proceed to delete crop",p[3],"with Crop ID",p[0],"which was sown on",p[2])
                inp=input("    Enter 'Y' to confirm deletion or enter any other key to cancel deletion: ")
                print()
                if inp=='Y' or inp=='y':
                    c3='DELETE FROM status WHERE C_ID="{}"'.format(cid)
                    ml.execute(c3)
                    print('    Record deleted')
                    print()
                else:
                    print("    Deletion cancelled")
                    print()
            elif a==4:
                break
        except:
            print()
            print("Enter valid input")
            print()
            continue

       
