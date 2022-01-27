def run():
    import mysqlconadv
    print("============================================================ SIGN-UP PAGE ===========================================================")
    print()
    print('Registrartion page')
    def uniqchk(a,c):
        if c=='em':
            dat=mysqlconadv.fetchall("select E_mail from farmerlogin")
            for i in dat:
                if i[0]==a:
                    return 0
                else:
                    continue
            else:
                return 1
        elif a.isnumeric()==True and c=='ph':
            dat=mysqlconadv.fetchall("select Phone from farmerlogin")
            for i in dat:
                if str(i[0])==a:
                    return 0
                else:
                    continue
            else:
                return 1
        elif a.isnumeric()==False and c=='ph':
            return 2
        
    def F_ID_Generator():
        a='select F_ID from farmerlogin order by F_ID desc'
        dat=mysqlconadv.fetchone(a)
        l=int(dat[0])
        return (l+1)
    ID=F_ID_Generator()
    print()
    print("Farmer ID: ",ID)
    print()
    print()
    name=input('Type your full name here: ')
    name=name.upper()
    while True:
        passwd=input('Type your password here: ')
        passwd2=input('Retype your password here: ')
        if passwd==passwd2:
            import random
            while True:
                e=input('Enter e-mail id: ')
                z=uniqchk(e,'em')
                if z==1:
                    break
                elif z==0:
                    print("Email ID already in use. Enter a different ID")
                    continue
            while True:
                j=input('Enter the phone number: ')
                z=uniqchk(j,'ph')
                if z==1:
                    break
                elif z==0:
                    print("Phone number already in use. Enter a different number")
                    continue
                elif z==2:
                    print("Enter vaild phone number. Please enter only numbers and not characters")
                    continue
            print()
            print('                                       ============ Answer the security questions ============                                     ')
            print()
            k=input("1. Your favorite game: ").capitalize()
            l=input('2. City/town were you born in: ').capitalize()
            m=input('3. Your favourite colour: ').capitalize()
            print()
            print('Remember the above entered answers')
            for i in range(3):
                #CAPTCHA
                print()
                print()
                print('CAPATCHA VERIFICATION')
                print('****************')
                print('''Verify that you are not a robot''')
                print()
                print('By verifying this you agree that the information entered above are to true to the best of my knowledge')
                print()
                n=random.randint(1000,9999)
                print()
                print('           ',n,'           ')
                print()
                o=int(input('Enter the number that is visible on the screen: '))            
                if o==n:
                    strr="insert into farmerlogin values('{}','{}','{}','{}','{}','{}','{}','{}')".format(ID,name,passwd,e,j,k,l,m)
                    mysqlconadv.execute(strr)
                    print("Account created")
                    return 1
                else:
                    print("Captcha verification failed. Try again.")
            
        else:
            print("Password not matching")
            continue

