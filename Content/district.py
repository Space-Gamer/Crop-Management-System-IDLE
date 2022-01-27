def run():
    while True:
        print('''                                    Select district:

                                                    1. Bagalkot		
                                                    2. Bangalore Rural	
                                                    3. Bangalore Urban
                                                    4. Belgaum
                                                    5. Bellary	
                                                    6. Bidar	
                                                    7. Bijapur	
                                                    8. Chamarajanagar	
                                                    9. Chikmagalur	
                                                    10. Chitradurga	
                                                    11. Chickballapur	
                                                    12. Dakshin Kannada
                                                    13. Davanagere	
                                                    14. Dharwad		
                                                    15. Gadag		
                                                    16. Gulbarga	
                                                    17. Hassan	
                                                    18. Haveri	
                                                    19. Kodagu	
                                                    20. Kolar	
                                                    21. Koppal
                                                    22. Mandya	
                                                    23. Mysore	
                                                    24. Raichur	
                                                    25. Ramnagar	
                                                    26. Shivamoga	
                                                    27. Tumkur
                                                    28. Udupi	
                                                    29. Uttara Kannada	
                                                    30. Yadgir''')

        print()
        a1=input('                                Enter the district: ')
        print()
        print()
        print()
        b1=a1.lower
        try:
            if a1=='1' or b1=='bagalkot':
                print('''                                    Select Taluk: 
                                                    1. BADAMI
                                                    2. BAGALKOTE
                                                    3. BILGI
                                                    4. HUNGUND
                                                    5. JAMKHANDI
                                                    6. MUDHOL''')
                x1='BAGALKOTE'
                print()
                c1=int(input('                                     Enter taluk: '))
                y1=['BADAMI','BAGALKOTE','BILGI','HUNGUND','JAMKHANDI','MUDHOL']
                z1=y1[c1-1]

            elif a1=='3' or b1=='bangalore urban':
                print('''                                    Select Taluk:
                                                    1. ANEKAL
                                                    2. BANGALORE NORTH
                                                    3. BANGALORE EAST
                                                    4. BANGALORE SOUTH''')
                x1='Bangalore Urban'
                print()
                y1=['Anekal','Bangalore North','Bangalore East','Bangalore South']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]
            
            elif a1=='2' or b1=='bengauluru rural':
                print('''                                    Select Taluk:
                                                    1. Nelamangala	
                                                    2. Doddaballapura	
                                                    3. Devanahalli	
                                                    4. Hosakote''')
                print()
                x1='Bangalore Rural'
                y1=['Nelamangala','Doddaballapur','Devanahalli','Hoskote']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]
                
            elif a1=='4' or b1=='belgaum':
                print('''                                    Select Taluk:
                                                    1. ATHANI 
                                                    2. BAILHONGAL 
                                                    3. BELGAUM 
                                                    4. CHIKKODI 
                                                    5. GOKAK 
                                                    6. HUKKERI 
                                                    7. KHANAPUR 
                                                    8. RAIBAGH 
                                                    9. RAMDURG 
                                                    10. SOUNDATTI''')
                print()
                x1='Belgaum'
                y1=['Athani','Bailhongal','Belgaum','Chikkodi','Gokak','Hukkeri','Khanapur','Raibagh','Ramdurg','Soundatti']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]

            elif a1=='5' or b1=='bellary':
                print('''                                    Select Taluk:
                                                    1. BELLARY
                                                    2. HADAGALI
                                                    3. HAGARIBOMMANAHALLI
                                                    4. HOSPET
                                                    5. KUDLUGI''')
                print()
                x1='Bellary'
                y1=['Bellary','Hadagali','Hagaribommanahalli','Hospet','Kudlugi']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]

            elif a1=='6' or b1=='bidar':
                print('''                                    Select Taluk:
                                                    1. AURAD
                                                    2. BASAVAKALYAN
                                                    3. BIDAR
                                                    4. HUMNABAD''')
                print()
                x1='BIDAR'
                y1=['AURAD','BASAVAKALYAN','BIDAR','HUMNABAD']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]

            elif a1=='7' or b1=='bijapur':
                print('''                                    Select Taluk:	
                                                    1. BAGEWADI
                                                    2. BIJAPUR
                                                    3. INDI
                                                    4. MUDDEBIHAL
                                                    5. SINDGI''')
                print()
                x1='Bijapur'
                y1=['BAGEWADI','BIJAPUR','INDI','MUDDEBIHAL','SINDGI']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]

            elif a1=='8' or b1=='chamarajanagar':
                print('''                                    Select Taluk:
                                                    1. CHAMARAJANAGARA
                                                    2. GUNDLUPET
                                                    3. KOLLEGAL
                                                    4. YELANDUR''')
                print()
                x1='Chamarajanagar'
                y1=['CHAMARAJANAGARA','GUNDLUPET','KOLLEGAL','YELANDUR']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]

            elif a1=='9' or b1=='chikmagalur':
                print('''                                    Select Taluk:	
                                                    1. CHICKMAGALUR
                                                    2. KADUR
                                                    3. KOPPA
                                                    4. MUDIGERE
                                                    5. NARASIMHARAJAPUR
                                                    6. SRINGERI
                                                    7. TARIKERE''')
                x1='Chickmagalur'
                y1=['CHICKMAGALUR','KADUR','KOPPA','MUDIGERE','NARASIMHARAJAPUR','SRINGERI','TARIKERE']
                print()
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]

            elif a1=='10' or b1=='chitradurga':
                print('''                                    Select Taluk:	
                                                    1. CHALLAKERE
                                                    2. CHITRADURGA
                                                    3. HIRIYUR
                                                    4. HOLALKERE
                                                    5. HOSADURGA
                                                    6. MONAKALMURU''')
                x1='CHITRADURGA'
                y1=['CHALLAKERE','CHITRADURGA','HIRIYUR','HOLALKERE','HOSADURGA','MONAKALMURU']
                
                print()
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='11' or b1=='chickballapur':
                print('''                                    Select Taluk:	
                                                    1. BAGEPALLI
                                                    2. CHIKBALLAPUR
                                                    3. CHINTAMANI
                                                    4. GAURIBIDANUR
                                                    5. GUDIBANDA
                                                    6. SIDLAGHATTA''')
                print()
                x1='CHICKBALLAPUR'
                Y1=['BAGEPALLI','CHIKBALLAPUR','CHINTAMANI','GAURIBIDANUR','GUDIBANDA','SIDLAGHATTA']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='12' or b1=='dakshin Kannada':
                print('''                                    Select Taluk:
                                                    1. BELTANGADI
                                                    2. BANTWAL
                                                    3. MANGALORE
                                                    4. PUTTUR
                                                    5. SULYA''')
                print()
                x1='DAKSHIN KANNADA'
                y1=['BELTANGADI','BANTWAL','MANGALORE','PUTTUR','SULYA']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='13' or b1=='davanagere':
                print('''                                    Select Taluk:
                                                    1. CHANNAGIRI
                                                    2. DAVANAGERE
                                                    3. HARIHAR
                                                    4. HARAPANAHALLI
                                                    5. HONAALI
                                                    6. JAGALUR''')
                x1='DAVANGERE'
                y1=['CHANNAGIRI','DAVANAGERE','HARIHAR','HARAPANAHALLI','HONAALI','JAGALUR']
                print()
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='14' or b1=='dharwad':
                print('''                                    Select Taluk:
                                                    1. DHARVAD
                                                    2. HUBLI
                                                    3. KALGHATGI
                                                    4. KUNDGOL
                                                    5. NAVALGUND''')
                x1='DHARVAD'
                y1=['DHARVAD','HUBLI','KALGHATGI','KUNDGOL','NAVALGUND']
                print()
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='15' or b1=='gadag':
                print('''                                    Select Taluk:
                                                    1. GADAG
                                                    2. MUNDARGI
                                                    3. NARAGUND
                                                    4. RON
                                                    5. SHIRAHATTI''')
                x1='GADAG'
                y1=['GADAG','MUNDARGI','NARAGUND','RON','SHIRAHATTI']
                print()
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='16' or b1=='gulbarga':
                print('''                                    Select Taluk:
                                                    1. AFZALPUR
                                                    2. ALAND
                                                    3. CHINCHOLI
                                                    4. CHITAPUR
                                                    5. GULBARGA
                                                    6. JEWARGI
                                                    7. SEDAM''')
                print()
                x1='GULBARGA'
                y1=['AFZALPUR','ALAND','CHINCHOLI','CHITAPUR','GULBARGA','JEWARGI','SEDAM']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='17' or b1=='hassan':
                print('''                                    Select Taluk:
                                                    1. ALUR
                                                    2. ARKALGUD
                                                    3. BELUR
                                                    4. CHANNARAYAPATNA
                                                    5. HASSAN
                                                    6. HOLENARASIPUR
                                                    7. SAKALESHPUR''')
                print()
                x1='HASSAN'
                y1=['ALUR','ARKALGUD','BELUR','CHANNARAYAPATNA','HASSAN','HOLENARASIPUR','SAKALESHPUR']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]



            elif a1=='18' or b1=='haveri':
                print('''                                    Select Taluk:	
                                                    1. BYADGI
                                                    2. HAVERI
                                                    3. HANAGAL
                                                    4. HIREKERUR
                                                    5. RANEBENNUR
                                                    6. SAVANUR
                                                    7. SHIGGAVI''')
                print()
                x1='HAVERI'
                y1=['BYADGI','HAVERI','HANAGAL','HIREKERUR','RANEBENNUR','SAVANUR','SHIGGAVI']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='19' or b1=='kodagu':
                print('''                                    Select Taluk:	
                                                    1. MADEKERI
                                                    2. SOMWARPET
                                                    3. VIRAJPET''')
                x1='KODAGU'
                y1=['MADEKERI','SOMWARPET','VIRAJPET']
                print()
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='20' or b1=='kolar':
                print('''                                    Select Taluk:
                                                    1. BANGARPET
                                                    2. KOLAR
                                                    3. MALUR
                                                    4. MULBAGAL
                                                    5. SRINIVASAPURA''')
                x1='KOLAR'
                y1=['BANGARPET','KOLAR','MALUR','MULBAGAL','SRINIVASAPURA']
                print()
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='21' or b1=='koppal':
                print('''                                    Select Taluk:
                                                    1. GANGAVATHI
                                                    2. KOPPAL
                                                    3. KUSHTAGI
                                                    4. YELBURGA''')
                print()
                x1='KOPPAL'
                y1=['GANGAVATHI','KOPPAL','KUSHTAGI','YELBURGA']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='22' or b1=='mandya':
                print('''                                    Select Taluk:
                                                    1. KRISHNARAJPET
                                                    2. MADDUR
                                                    3. MALAVALLI
                                                    4. MANDYA
                                                    5. NAGAMANGALA
                                                    6. PANDAVAPURA
                                                    7. SRIRANGAPATNA''')
                x1='MANDYA'
                y1=['KRISHNARAJPET','MADDUR','MALAVALLI','MANDYA','NAGAMANGALA','PANDAVAPURA','SRIRANGAPATNA']
                print()
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='23' or b1=='mysore':
                print('''                                    Select Taluk:	
                                                    1. HEGGADADEVANAKOTE
                                                    2. HUNSUR
                                                    3. KRISHNARAJANAGAR
                                                    4. MYSORE
                                                    5. NANJANAGUD
                                                    6. PERIYAPATNA
                                                    7. T NARASIPUR''')
                x1='MYSORE'
                y1=['HEGGADADEVANAKOTE','HUNSUR','KRISHNARAJANAGAR','MYSORE','NANJANAGUD','PERIYAPATNA','T NARASIPUR']
                print()
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='24' or b1=='raichur':
                print('''                                    Select Taluk:
                                                    1. DEVDURG
                                                    2. LINGSUGUR
                                                    3. MANVI
                                                    4. RAICHUR
                                                    5. SINDHANUR''')
                print()
                x1='RAICHUR'
                y1=['DEVDURG','LINGSUGUR','MANVI','RAICHUR','SINDHANUR']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='26' or b1=='shimoga':
                print('''                                    Select Taluk:
                                                    1. BHADRAVATHI
                                                    2. HOSANAGAR
                                                    3. SAGAR
                                                    4. SHIKARIPUR
                                                    5. SHIMOGA
                                                    6. SORAB
                                                    7. TIRTHAHALLI''')
                x1='SHIMOGA'
                y1=['BHADRAVATHI','HOSANAGAR','SAGAR','SHIKARIPUR','SHIMOGA','SORAB','TIRTHAHALLI']
                print()
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='27' or b1=='tumkur':
                print('''                                    Select Taluk:
                                                    1. C N HALLI
                                                    2. GUBBI
                                                    3. KORATAGERE
                                                    4. KUNIGAL
                                                    5. MADHUGIRI
                                                    6. PAVAGADA
                                                    7. SIRA
                                                    8. TIPTUR
                                                    9. TUMKUR
                                                    10. TURVEKERE''')
                x1='TUMKUR'
                y1=['C N HALLI','GUBBI','KORATAGERE','KUNIGAL','MADHUGIRI','PAVAGADA','SIRA','TIPTUR','TUMKUR','TURVEKERE']
                print()
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='28' or b1=='udupi':
                print('''                                    Select Taluk:	
                                                    1. KARKALA
                                                    2. KUNDAPUR
                                                    3. UDUPI''')
                x1='UDUPI'
                y1=['KARKALA','KUNDAPUR','UDUPI']
                print()
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='29' or b1=='uttara Kannada':
                print('''                                    Select Taluk:
                                                    1. ANKOLA
                                                    2. BHATKAL
                                                    3. HALIYAL
                                                    4. HONNAVAR
                                                    5. KARWAR
                                                    6. KUMTA
                                                    7. MUNDAGOD
                                                    8. SIDDAPUR
                                                    9. SIRSI
                                                    10. SUPA
                                                    11. ANKOLA
                                                    12. YELLAPUR''')
                x1='UTTARA KANNADA'
                y1=['ANKOLA','BHATKAL','HALIYAL','HONNAVAR','KARWAR','KUMTA','MUNDAGOD','SIDDAPUR','SIRSI','SUPA','ANKOLA','YELLAPUR']
                print()
                c1=int(input('                                    Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='25' or b1=='ramnagar':
                print('''                                    Select Taluk:	
                                                    1. CHANNAPATNA
                                                    2. KANAKAPURA
                                                    3. MAGADI
                                                    4. RAMANAGARAM''')
                print()
                x1='RAMNAGAR'
                y1=['CHANNAPATNA','KANAKAPURA','MAGADI','RAMANAGARAM']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]


            elif a1=='30' or b1=='yadgir':
                print('''                                    Select Taluk:
                                                    1. SHAHAPUR
                                                    2. SHORAPUR
                                                    3. YADGIR''')
                print()
                x1='YADGIR'
                y1=['SHAHAPUR','SHORAPUR','YADGIR']
                c1=int(input('                                     Enter taluk: '))
                z1=y1[c1-1]
            
        except:
            print('Please enter valid input')
        
        try:
            return x1.upper(),z1.upper()
        except:
            print("Please enter valid input")

