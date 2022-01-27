def run(a):
    import csv
    strr="#path\\Pradeep_Arpan_Project_XII\\Content\\Data\\Temp data\\"
    a=a.upper()
    a=a.replace(' ','_')
    strr+=a+'.csv'
    f=open(strr,'r')
    r=csv.reader(f)
    z=0
    for i in r:
        if i!=[] and i[0]!='Jan':
            z=1
            l=[]
            for j in i:
                l.append(int(round(float(j),0)))
            print("Please wait...")
            import Bar
            Bar.run(l)
            a=''
    if z==0:
       print("Invalid district")
    return a
    f.close()
     
