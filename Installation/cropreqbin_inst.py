def run():
    import pickle
    f=open("#path\\Pradeep_Arpan_Project_XII\\Content\\Data\\Cropreqbin.bin",'wb')
    l={'MinTemp':20,'MaxTemp':30,'Rain':50,'GPeriod':95,'STime':[6,9]}
    m={'MinTemp':26,'MaxTemp':34,'Rain':75,'GPeriod':135,'STime':[6]}
    n={'MinTemp':25,'MaxTemp':32,'Rain':40,'GPeriod':75,'STime':[3,6,9,12]}
    o={'MinTemp':10,'MaxTemp':25,'Rain':80,'GPeriod':125,'STime':[9]}
    p={'MinTemp':22,'MaxTemp':34,'Rain':100,'GPeriod':100,'STime':[3,6]}
    q={'MinTemp':20,'MaxTemp':40,'Rain':125,'GPeriod':135,'STime':[6]}
    r={'MinTemp':18,'MaxTemp':42,'Rain':125,'GPeriod':135,'STime':[9,12]}
    s={'MinTemp':21,'MaxTemp':30,'Rain':60,'GPeriod':100,'STime':[12,3]}
    t={'MinTemp':17,'MaxTemp':30,'Rain':42,'GPeriod':120,'STime':[6]}
    u={'MinTemp':14,'MaxTemp':25,'Rain':65,'GPeriod':50,'STime':[9,12]}
    dictt={'Bajra':l,'Groundnut':m,'Jowar':n,'Mustard':o,'Ragi':p,'Rice':q,'Sugarcane':r,'Sunflower':s,'Arhar':t,'Wheat':u}
    pickle.dump(dictt,f)
    print("Data upload successful")
    f.close()

