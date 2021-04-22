def run(a,b):
    import csv
    f=open("#path\\Pradeep_Arpan_Project_XII\\Content\\Data\\rainfalldat.csv",'r')
    r=csv.reader(f)
    for i in r:
        if i[0]==a:
            if i[1]==b:
                print()
                print('                                  Average seaonal rainfall data of',a.capitalize(),'district',b.capitalize(),'taluk: ')
                print('                                  Average Cold weather rainfall: ',i[2],'mm')
                print('                                  Average Hot weather rainfall: ',i[3],'mm')
                print('                                  Average South-West monsoon rainfall: ',i[4],'mm')
                print('                                  Average North-East monsoon rainfall: ',i[5],'mm')
                return
    else:
        print("Invalid district or taluk")
                
    f.close()
