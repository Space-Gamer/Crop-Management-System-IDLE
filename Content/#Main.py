
import mysqlconadv as ml
import sys,time
print('''
                                 This OPEN-SOURCE project was developed by PRADEEP J and ARPAN M
                                              ''')
time.sleep(5)
ml.connect()
print('''=====================================================================================================================================
------------------------------------------------------ CROP MANAGEMENT SYSTEM -------------------------------------------------------''')
while True:
    print('''=====================================================================================================================================
''')
    print('''    Welcome to CROP MANAGEMENT SYSTEM

                                                        1. Sign in
                                                        2. Create a new account
                                                        3. Forgot password
                                                        4. Help
                                                        5. About this software
                                                        6. Exit
                                                        ''')
    a=input('    Enter your choice: ')
    if a=='1':
        print()
        print('============================================================= Login =================================================================')
        print()
        import login_page as l
        z,id=l.run()
        if z==1:
            fname=ml.fetchone('select F_Name from farmerlogin where F_ID='+str(id))[0]
            import Main_menu as m
            m.run(id,fname)
        elif z==2:
            continue
        elif z==0:
            inp=input("Enter 'Y' if you want to create a new account or press any other key to continue to main menu: ")
            if inp=='Y' or inp=='y':
                import signup_paget2
                a=signup_paget2.run()
                if a==1:
                    print("Please login again to access your account")
                    continue
                else:
                    print('Account creation failed')
            else:
                continue

    elif a=='2':
        print()
        import signup_paget2
        a=signup_paget2.run()
        if a==1:
            print()
            print("Please login again to access your account")
            continue
        else:
            print('Account creation failed')
    elif a=='3':
        print()
        print('========================================================== Forgot Password ==========================================================')
        print('Answer the security questions in order to retrive your account')
        print()
        f=int(input("Enter your FarmerID: "))
        k=input("1. Your favorite game: ").capitalize()
        l=input('2. Which city/town were you born in: ').capitalize()
        m=input('3. Your favourite colour: ').capitalize()
        strr="select * from farmerlogin where F_ID={}".format(f)
        data=ml.fetchall(strr)
        z=data[0]
        if k==z[5] and l==z[6] and m==z[7]:
            print()
            print('===> The data match <===')
            print()
            print('The username is:',z[1])
            print('The password is:',z[2])
            print()
            b1=input('Do you want to set a new password (Y/N)?')
            if b1=='Y' or b1=='y':
                b3=input('Enter the password to be set: ')
                b2="update farmerlogin set F_PASS='{}' where F_ID='{}'".format(b3,f)
                ml.execute(b2)
                print('Your password is successfully changed to:',b3)
        else:
            print('===> The data do not mach <====')
            print()
    elif a=='4':
        import guidelines as g
        g.run()
        continue
    elif a=='5':
        print("====================================================>Information about this project<=================================================")
        print()
        print("This project was developed by PRADEEP J and ARPAN M as a part of Class XII CBSE Investigatory project for the academdic year 2020-21")
        print()
        print("Although this software is not copyrighted("+chr(169)+"), the developers of this project strongly recommend the users to NOT COPY the source code of \nthis project but instead use this one as a refrence or follow this idea and then implement it in their projects")
        print()
        print('''Crop Management System is a computer program, developed using python and MySQL. It mainly aims to help the farmers with the adequate
information for growing crops and maximizing yields and profits. In this program the user will have to create an account of his own
and sign-in through the same. This account can be used in future. After signing in the user can use the available functions.
Here, the data regarding the login credentials will be stored in MySQL which is used as a back phase. The rainfall data and the
temperature data are stored in CSV files. The ordered seeds data will be stored in a binary file.''')
        print()
        print("For more info on the software check out this report: \"https://drive.google.com/file/d/1Bw50RIwtq6P07BJhUna9rPXgP9ZPy_mS/view?usp=sharing\"")
        time.sleep(12)
    elif a=='6':
        break
    else:
        print("\t\t\t\t\t\t\tInvalid Input!!")
        print('Refer the help forum for more details.')
        print()
        import guidelines as g
        g.run()
        continue
print()
print("Bye. Have a nice day!")

                  
        
        
