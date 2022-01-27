def run(fid):
    import pickle
    f=open("#path//Pradeep_Arpan_Project_XII//Content//Data//seed.bin",'rb')
    seed=pickle.load(f)
    f.close()
    def enqueue(qu,item):
        qu.append(item)
        if len(qu)==1:
            front=rear=0
        else:
            rear=len(qu)-1
        seed=qu
    def dequeue(qu):
        try:
            item=qu.pop(0)
            print(item,"delivered")
            print('--------------------------------------------------------------------------')
            if len(qu)==0:
                front=rear=None
        except:
            print("Nothing to be delivered")
    if fid!=1:
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
        if a==1:
            crop='Rice'
            qty=input('    Enter the amount of seeds required in kilograms: ')
            fin=crop+' '+qty+' kgs'
        elif a==2:
            crop='Jowar'
            qty=input('    Enter the amount of seeds required in kilograms: ')
            fin=crop+' '+qty+' kgs'
        elif a==3:
            crop='Ragi'
            qty=input('    Enter the amount of seeds required in kilograms: ')
            fin=crop+' '+qty+' kgs'
        elif a==4:
            crop='Bhajra'
            qty=input('    Enter the amount of seeds required in kilograms: ')
            fin=crop+' '+qty+' kgs'
        elif a==5:
            crop='Wheat'
            qty=input('    Enter the amount of seeds required in kilograms: ')
            fin=crop+' '+qty+' kgs'
        elif a==6:
            crop='Groundnut'
            qty=input('    Enter the amount of seeds required in kilograms: ')
            fin=crop+' '+qty+' kgs'
        elif a==7:
            crop='Sugarcane'
            qty=input('    Enter the amount of seeds required in kilograms: ')
            fin=crop+' '+qty+' kgs'
        elif a==8:
            crop='Sunflower'
            qty=input('    Enter the amount of seeds required in kilograms: ')
            fin=crop+' '+qty+' kgs'
        elif a==9:
            crop='Mustard'
            qty=input('    Enter the amount of seeds required in kilograms: ')
            fin=crop+' '+qty+' kgs'
        elif a==10:
            crop='Arhar(Tur)'
            qty=input('    Enter the amount of seeds required in kilograms: ')
            fin=crop+' '+qty+' kgs'
        l={fid:fin}
        enqueue(seed,l)
        print("    Seed order for",crop,"added successfully")
    elif fid==1:
        while True:
            print("    The present order list is",seed)
            i=input("    Press Y to dequeue the first order or N to exit to main_menu: ")
            if i=='y' or i=='Y':
                dequeue(seed)
            else:
                break
    f=open('#path//Pradeep_Arpan_Project_XII//Content//Data//seed.bin','wb')
    pickle.dump(seed,f)
    f.close()
