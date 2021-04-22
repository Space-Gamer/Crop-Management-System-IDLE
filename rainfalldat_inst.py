def run():
    import csv
    f=open("#path\\Pradeep_Arpan_Project_XII\\Content\\Data\\rainfalldat.csv",'w',newline='')
    w=csv.writer(f)
    data=[
        ['District','Taluk','Average Cold weather rainfall','Average Hot weather rainfall','Average South-West monsoon rainfall','Average North-East monsoon rainfall','Average annual rainfall'],
        ['BAGALKOTE','BADAMI',3,198,370,96,667],
        ['BAGALKOTE','BAGALKOTE',18,154,385,77,634],
        ['BAGALKOTE','BILGI',37,230,470,127,864],
        ['BAGALKOTE','HUNGUND',17,120,384,82,603],
        ['BAGALKOTE','JAMKHANDI',0,102,373,124,599],
        ['BAGALKOTE','MUDHOL',0,117,267,98,482],
        ['BANGALORE RURAL','DEVANAHALLI',0,122,309,287,718],
        ['BANGALORE RURAL','DODDABALLAPUR',0,97,429,237,763],
        ['BANGALORE RURAL','HOSKOTE',0,145,508,334,987],
        ['BANGALORE RURAL','NELAMANGALA',0,135,544,291,970],
        ['BANGALORE URBAN','ANEKAL',0,84,190,159,433],
        ['BANGALORE URBAN','BANGALORE NORTH',0,111,526,382,1019],
        ['BANGALORE URBAN','BANGALORE SOUTH',0,131,492,302,925],
        ['BANGALORE URBAN','BANGALORE EAST',0,52,327,232,611],
        ['BELGAUM','ATHANI',11,31,350,96,488],
        ['BELGAUM','BAILHONGAL',2,160,546,233,941],
        ['BELGAUM','BELGAUM',0,205,917,216,1338],
        ['BELGAUM','CHIKKODI',3,81,482,127,693],
        ['BELGAUM','GOKAK',3,116,294,153,566],
        ['BELGAUM','HUKKERI',1,105,500,170,776],
        ['BELGAUM','KHANAPUR',0,124,2671,203,2998],
        ['BELGAUM','RAIBAGH',4,119,270,105,498],
        ['BELGAUM','RAMDURG',9,183,369,146,707],
        ['BELGAUM','SOUNDATTI',12,264,430,245,951],
        ['BELLARY','BELLARY',2,115,270,101,488],
        ['BELLARY','HADAGALI',0,125,272,196,593],
        ['BELLARY','HAGARIBOMMANAHALLI',0,75,325,138,538],
        ['BELLARY','HOSPET',1,153,396,141,691],
        ['BELLARY','KUDLUGI',0,121,323,82,526],
        ['BIDAR','AURAD',17,139,372,18,546],
        ['BIDAR','BASAVAKALYAN',15,138,557,55,765],
        ['BIDAR','BIDAR',7,123,456,25,611],
        ['BIDAR','HUMNABAD',7,127,375,56,565],
        ['BIJAPUR','BAGEWADI',6,259,763,122,1150],
        ['BIJAPUR','BIJAPUR',8,153,785,132,1088],
        ['BIJAPUR','INDI',14,174,409,93,690],
        ['BIJAPUR','MUDDEBIHAL',3,141,336,75,555],
        ['BIJAPUR','SINDGI',6,158,538,65,767],
        ['CHAMARAJANAGAR','CHAMARAJANAGARA',4,163,261,379,807],
        ['CHAMARAJANAGAR','GUNDLUPET',10,270,346,304,930],
        ['CHAMARAJANAGAR','KOLLEGAL',0,201,295,357,853],
        ['CHAMARAJANAGAR','YELANDUR',9,204,329,388,930],
        ['CHICKMAGALUR','CHICKMAGALUR',0,251,913,111,1275],
        ['CHICKMAGALUR','KADUR',0,237,419,187,843],
        ['CHICKMAGALUR','KOPPA',4,275,3303,119,3701],
        ['CHICKMAGALUR','MUDIGERE',3,379,2738,219,3339],
        ['CHICKMAGALUR','NARASIMHARAJAPUR',0,313,1615,126,2054],
        ['CHICKMAGALUR','SRINGERI',7,208,4863,197,5275],
        ['CHICKMAGALUR','TARIKERE',0,236,736,208,1180],
        ['CHITRADURGA','CHALLAKERE',3,149,242,171,565],
        ['CHITRADURGA','CHITRADURGA',4,258,465,263,990],
        ['CHITRADURGA','HIRIYUR',0,108,295,239,642],
        ['CHITRADURGA','HOLALKERE',0,203,523,236,962],
        ['CHITRADURGA','HOSADURGA',0,127,288,220,635],
        ['CHITRADURGA','MONAKALMURU',1,231,375,97,704],
        ['CHICKBALLAPUR','BAGEPALLI',0,85,152,146,383],
        ['CHICKBALLAPUR','CHIKBALLAPUR',0,75,256,155,486],
        ['CHICKBALLAPUR','CHINTAMANI',0,136,175,79,390],
        ['CHICKBALLAPUR','GAURIBIDANUR',0,88,298,139,525],
        ['CHICKBALLAPUR','GUDIBANDA',0,126,226,89,441],
        ['CHICKBALLAPUR','SIDLAGHATTA',0,97,129,113,339],    
        ['DAKSHIN KANNADA','BELTANGADI',0,332,3498,347,4175],
        ['DAKSHIN KANNADA','BANTWAL',0,176,3097,347,3620],
        ['DAKSHIN KANNADA','MANGALORE',0,165,2810,296,3271],
        ['DAKSHIN KANNADA','PUTTUR',0,296,3282,328,3906],
        ['DAKSHIN KANNADA','SULYA',0,372,3189,303,3864],
        ['DAVANGERE','CHANNAGIRI',0,157,659,212,1028],
        ['DAVANGERE','DAVANAGERE',0,170,459,199,828],
        ['DAVANGERE','HARIHAR',0,169,549,231,949],
        ['DAVANGERE','HARAPANAHALLI',0,171,508,236,915],
        ['DAVANGERE','HONAALI',9,142,629,159,939],
        ['DAVANGERE','JAGALUR',0,113,356,176,645],
        ['DHARVAD','DHARVAD',3,223,533,217,976],
        ['DHARVAD','HUBLI',0,217,390,140,747],
        ['DHARVAD','KALGHATGI',0,220,888,262,1370],
        ['DHARVAD','KUNDGOL',0,271,625,188,1084],
        ['DHARVAD','NAVALGUND',10,229,416,184,839],
        ['GADAG','GADAG',0,142,492,145,779],
        ['GADAG','MUNDARGI',5,108,311,151,575],
        ['GADAG','NARAGUND',0,279,402,119,800],
        ['GADAG','RON',6,106,362,37,511],
        ['GADAG','SHIRAHATTI',26,148,504,193,871],
        ['GULBARGA','AFZALPUR',14,154,536,80,784],
        ['GULBARGA','ALAND',12,168,458,83,721],
        ['GULBARGA','CHINCHOLI',3,125,550,63,741],
        ['GULBARGA','CHITAPUR',0,124,464,75,663],
        ['GULBARGA','GULBARGA',4,128,517,82,731],
        ['GULBARGA','JEWARGI',2,127,336,75,540],
        ['GULBARGA','SEDAM',0,143,550,68,761],
        ['HASSAN','ALUR',0,197,910,179,1286],
        ['HASSAN','ARKALGUD',0,194,575,104,873],
        ['HASSAN','BELUR',0,289,857,169,1315],
        ['HASSAN','CHANNARAYAPATNA',0,202,376,186,764],
        ['HASSAN','HASSAN',0,237,594,207,1038],
        ['HASSAN','HOLENARASIPUR',0,169,487,171,827],
        ['HASSAN','SAKALESHPUR',1,230,2285,151,2667],
        ['HAVERI','BYADGI',4,154,659,215,1032],
        ['HAVERI','HAVERI',0,264,671,188,1123],
        ['HAVERI','HANAGAL',0,266,872,227,1365],
        ['HAVERI','HIREKERUR',3,226,738,278,1245],
        ['HAVERI','RANEBENNUR',0,176,542,170,888],
        ['HAVERI','SAVANUR',0,157,495,157,809],
        ['HAVERI','SHIGGAVI',1,217,562,197,977],
        ['KODAGU','MADEKERI',3,312,3664,191,4170],
        ['KODAGU','SOMWARPET',1,179,2060,169,2409],
        ['KODAGU','VIRAJPET',1,237,1772,147,2157],
        ['KOLAR','BANGARPET',0,47,200,200,447],
        ['KOLAR','KOLAR',0,105,305,190,600],
        ['KOLAR','MALUR',0,85,207,245,537],
        ['KOLAR','MULBAGAL',0,92,271,133,496],
        ['KOLAR','SRINIVASAPURA',0,90,182,146,418],
        ['KOPPAL','GANGAVATHI',0,106,373,102,581],
        ['KOPPAL','KOPPAL',8,153,500,146,807],
        ['KOPPAL','KUSHTAGI',20,172,498,89,779],
        ['KOPPAL','YELBURGA',6,144,501,114,765],
        ['MANDYA','KRISHNARAJPET',0,280,353,189,822],
        ['MANDYA','MADDUR',0,195,521,184,900],
        ['MANDYA','MALAVALLI',14,142,325,221,702],
        ['MANDYA','MANDYA',0,227,383,233,843],
        ['MANDYA','NAGAMANGALA',9,157,354,139,659],
        ['MANDYA','PANDAVAPURA',0,219,277,221,717],
        ['MANDYA','SRIRANGAPATNA',0,162,342,228,732],
        ['MYSORE','HEGGADADEVANAKOTE',1,230,593,208,1032],
        ['MYSORE','HUNSUR',0,196,337,155,688],
        ['MYSORE','KRISHNARAJANAGAR',0,238,379,265,882],
        ['MYSORE','MYSORE',0,227,470,194,891],
        ['MYSORE','NANJANAGUD',0,180,370,92,642],
        ['MYSORE','PERIYAPATNA',0,223,485,104,812],
        ['MYSORE','T NARASIPUR',3,124,476,159,762],
        ['RAICHUR','DEVDURG',1,126,423,56,606],
        ['RAICHUR','LINGSUGUR',0,0,385,64,449],
        ['RAICHUR','MANVI',0,91,427,36,554],
        ['RAICHUR','RAICHUR',0,82,443,70,595],
        ['RAICHUR','SINDHANUR',0,75,357,76,508],
        ['SHIMOGA','BHADRAVATHI',2,192,758,146,1098],
        ['SHIMOGA','HOSANAGAR',4,151,5110,182,5447],
        ['SHIMOGA','SAGAR',30,140,3199,167,3536],
        ['SHIMOGA','SHIKARIPUR',3,213,977,149,1342],
        ['SHIMOGA','SHIMOGA',0,196,835,161,1192],
        ['SHIMOGA','SORAB',0,126,1659,37,1822],
        ['SHIMOGA','TIRTHAHALLI',4,195,3264,123,3586],
        ['TUMKUR','C N HALLI',14,123,267,217,621],
        ['TUMKUR','GUBBI',4,88,397,214,703],
        ['TUMKUR','KORATAGERE',0,180,401,192,773],
        ['TUMKUR','KUNIGAL',0,94,509,235,838],
        ['TUMKUR','MADHUGIRI',0,109,180,121,410],
        ['TUMKUR','PAVAGADA',0,104,202,173,479],
        ['TUMKUR','SIRA',0,189,294,172,655],
        ['TUMKUR','TIPTUR',4,128,353,244,729],
        ['TUMKUR','TUMKUR',0,161,508,216,885],
        ['TUMKUR','TURVEKERE',0,123,384,233,740],
        ['UDUPI','KARKALA',2,222,3969,407,4600],
        ['UDUPI','KUNDAPUR',0,86,3586,237,3909],
        ['UDUPI','UDUPI',0,134,2854,332,3320],
        ['UTTARA KANNADA','ANKOLA',0,99,2743,191,3033],
        ['UTTARA KANNADA','BHATKAL',0,174,3358,146,3678],
        ['UTTARA KANNADA','HALIYAL',0,172,892,262,1326],
        ['UTTARA KANNADA','HONNAVAR',0,122,4205,176,4503],
        ['UTTARA KANNADA','KARWAR',0,112,2511,248,2871],
        ['UTTARA KANNADA','KUMTA',0,245,3778,117,4140],
        ['UTTARA KANNADA','MUNDAGOD',1,180,942,158,1281],
        ['UTTARA KANNADA','SIDDAPUR',0,91,4818,186,5095],
        ['UTTARA KANNADA','SIRSI',0,123,2643,245,3011],
        ['UTTARA KANNADA','SUPA',0,133,3605,249,3987],
        ['UTTARA KANNADA','ANKOLA',0,99,2743,191,3033],
        ['UTTARA KANNADA','YELLAPUR',1,181,1917,244,2343],
        ['RAMNAGAR','CHANNAPATNA',0,143,380,147,670],
        ['RAMNAGAR','KANAKAPURA',0,181,328,189,698],
        ['RAMNAGAR','MAGADI',0,81,533,234,848],
        ['RAMNAGAR','RAMANAGARAM',0,131,441,215,787],
        ['RAMNAGAR','CHANNAPATNA',0,143,380,147,670],
        ['YADGIR','SHAHAPUR',0,33,346,97,476],
        ['YADGIR','SHORAPUR',1,20,429,98,548],
        ['YADGIR','YADGIR',0,75,431,74,580],
        
        
        
        
        
        
        
        
        
        
        ]
    w.writerows(data)
    f.close()
    print("Data upload successful")
