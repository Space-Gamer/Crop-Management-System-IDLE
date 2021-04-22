import os,sys,mysql.connector,pickle
inp=''
def replace(file):
    with open(file,'r') as a:
        dat=a.read()
        dat=dat.replace('#path',path)
        dat=dat.replace('#pass',inp)
    with open(file,'w') as a:
        a.write(dat)
    print(file,"file rewriting completed")
print("======================Installation file=============================")
print('''After pasting or extracting the folder \"Pradeep_Arpan_Project_XII\" follow the following steps:
1. Find and select the folder \"Pradeep_Arpan_Project_XII\"
2. Copy the path of the folder in your system
3. Paste below the copied file in described format WITHOUT QUOTES:
   Example of path: C:\\Users\MyPC\Downloads <-- correct format

   Wrong path syntax examples: C > Users > MyPC > Downloads   }
                               C:/Users/MyPC/Downloads        }WRONG SYNTAX
                               C:\\\\Users\\\MyPC\\\Downloads }
                               "C:\\Users\MyPC\Downloads\Pradeep_Arpan_Project_XII"
                               ''')
path=str(input('Enter the copied path of "Pradeep_Arpan_Project_XII" folder :'))
path=path.replace('\\',('\\'+'\\'))
print("Rewriting files...")
try:
    strr=path+"\\Pradeep_Arpan_Project_XII\\Installation"
    os.chdir(strr)
except:
    print("Entered path is invalid. Please try again")
    sys.exit()
replace("cropreqbin_inst.py")
replace("rainfalldat_inst.py")
try:
    strr=path+"\\Pradeep_Arpan_Project_XII\\Content"
    os.chdir(strr)
except:
    print("Entered path is invalid. Please try again")
    sys.exit()
replace("ANRainfalldat_csvreader.py")
replace("cropreqread.py")
replace("cropsugg.py")
replace("Rainfalldat_csvreader.py")
replace("tempdat_csvreader.py")
replace("seedbin.py")
print("Rewriting completed")
while True:
    inp=input("Enter your MySQL password(case-sensitive): ")
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',passwd=inp)
        if mycon.is_connected()==True:
            mycon.close()
            print("Password accepted")
            break
    except:
        print("Please enter valid MySQL password")
        continue
print("Please wait....")
strr=path+"\\Pradeep_Arpan_Project_XII\\Installation"
os.chdir(strr)
replace('mysqlconadv.py')
replace('creationofdatabase.py')
#seedbin_inst
f=open(path+'//Pradeep_Arpan_Project_XII//Content//Data//seed.bin','wb')
l=[]
pickle.dump(l,f)
f.close()
print("Please close this shell and run the file: 'Install_2.py'")
