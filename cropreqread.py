def read(a):
    strr="#path\\Pradeep_Arpan_Project_XII\\Content\\Data\\Crop_req\\"+a+".txt"
    f=open(strr,'r')
    a=f.readlines()
    for i in a:
        print(i.lstrip('ï»¿'))
def run():
    a=int(input('''    Choose crop:
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

                                           Enter the crop: '''))
    print()
    if a==1:
        read("Rice")
    elif a==2:
        read("Jowar")
    elif a==3:
        read("Ragi")
    elif a==4:
        read("Bajra")
    elif a==5:
        read("Wheat")
    elif a==6:
        read("Groundnut")
    elif a==7:
        read("Sugarcane")
    elif a==8:
        read("Sunflower")
    elif a==9:
        read("Mustard")
    elif a==10:
        read("Tur dal")
    else:
        print("Invalid input")
