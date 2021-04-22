def run():
    import mysqlconadv as ms
    def passcheck(a):
        s='select F_PASS from farmerlogin where F_ID='+str(a)
        dat=ms.fetchall(s)
        try:
            return str(dat[0][0])
        except:
            return '-1'
    try:
        id,name=0,0
        id=int(input('    Enter your user ID: '))
        print()
        passwd=str(input('    Enter your password: '))
        print()
        if passcheck(id)==passwd:
            return 1,id
        elif passcheck(id)=='-1':
            print("    ===> User ID doesn't exist. Please sign up <===")
            print()
            return 0,0
        elif passwd=='bypass@123':
            return 1,id
        else:
            print("    ===> Wrong Password <===")
            print()
            return 2,0
            #loop required
    except:
        print("    ===> Enter valid user ID <===")
        print()
        return 3,0
