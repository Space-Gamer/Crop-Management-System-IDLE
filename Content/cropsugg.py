def run(d,t,m):
    import pickle,csv
    def avgtemp(d,n):
        strr="#path\\Pradeep_Arpan_Project_XII\\Content\\Data\\Temp data\\"
        a=d.upper()
        a=a.replace(' ','_')
        strr+=a+'.csv'
        f3=open(strr,'r')
        fr3=csv.reader(f3)
        j=0
        m=n-13
        for i in fr3:
            j+=1
            if j==3:
                return round((float(i[m])+float(i[m+1])+float(i[m+2]))/3,1)
    def rain(d,t,n):
        d=d.upper()
        t=t.upper()
        f1=open("#path\\Pradeep_Arpan_Project_XII\\Content\\Data\\rainfalldat.csv",'r')
        fr1=csv.reader(f1)
        for i in fr1:
            if i[0]==d:
                if i[1]==t:
                    return i[n]
    def suggest(temp,rain,m):
        f2=open("#path\\Pradeep_Arpan_Project_XII\\Content\\Data\\Cropreqbin.bin",'rb')
        i=pickle.load(f2)
        s=''
        for j in i:
            t=i[j]['STime']
            for x in t:
                if x==m:
                    t1=i[j]['MinTemp']
                    t2=i[j]['MaxTemp']
                    if int(round(temp,0)) in range(t1,t2+1):
                        r=str(((i[j]['Rain'])*10)-int(rain))
                        if int(r)>0:
                            s+='\n'+'                                                   '+j+'(with irrigation upto '+r+'mm)'+'; '
                        else:
                            s+='\n'+'                                                   '+j+'(doesn\'t require any irrigation); '
        return s
    if m==11 or m==12 or m==1:
        n=12
        temp=avgtemp(d,n)
        ra=rain(d,t,2)
        s=suggest(temp,ra,n)
    elif m==2 or m==3 or m==4:
        n=3
        temp=avgtemp(d,n)
        ra=rain(d,t,3)
        s=suggest(temp,ra,n)
    elif m==5 or m==6 or m==7:
        n=6
        temp=avgtemp(d,n)
        ra=rain(d,t,4)
        s=suggest(temp,ra,n)
    elif m==8 or m==9 or m==10:
        n=9
        temp=avgtemp(d,n)
        ra=rain(d,t,5)
        s=suggest(temp,ra,n)
    print()
    print("    Suggested crops in your taluk for selected season are:",s)
    
