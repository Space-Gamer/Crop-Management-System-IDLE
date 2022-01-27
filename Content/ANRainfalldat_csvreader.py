def run(a,b):
    import csv
    f=open("#path\\Pradeep_Arpan_Project_XII\\Content\\Data\\rainfalldat.csv",'r')
    r=csv.reader(f)
    for i in r:
        if i[0]==a:
            if i[1]==b:
                print()
                print('    Average Anuual rainfall recieved in',a.capitalize(),'district',b.capitalize(),'taluk is',i[6],'mm')
                return
    else:
        print("===> Invalid district or taluk <===")
                
    f.close()
