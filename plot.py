def run():
    import matplotlib.pyplot as plt
    a=input('''    Choose crop:
                                                        1. Rice
                                                        2. Jowar
                                                        3. Ragi
                                                        4. Bhajra
                                                        5. Wheat
                                                        6. Groundnut
                                                        7. Sugarcane
                                                        8. Sunflower
                                                        9. Mustard
                                                       10. Arhar(Tur)

                                        Enter the crop: ''')
    if a=='1':
        x=['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21 (Expected)']
        y=[961,978,1020,1045,1117,1166,1208,1250]
        plt.plot(x,y,marker='o',markersize=5)
        plt.xlabel('Years')
        plt.ylabel('MSP (per quintal in rupees)')
        plt.title('Rice')
        for i in range(len(x)):
            plt.annotate(chr(8377)+str(y[i]),xy=(i,(y[i]+5)))
        plt.show()
    elif a=='2':
        x=['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21 (Expected)']
        y=[1269,1370,1467,1501,1556,1619,1698,1790]
        plt.plot(x,y,marker='o',markersize=5)
        plt.xlabel('Years')
        plt.ylabel('MSP (per quintal in rupees)')
        plt.title('Jowar')
        for i in range(len(x)):
            plt.annotate(chr(8377)+str(y[i]),xy=(i,(y[i]+5)))
        plt.show()
    elif a=='3':
        x=['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21 (Expected)']
        y=[1338,1474,1688,1733,1861,1931,2100,2260]
        plt.plot(x,y,marker='o',markersize=5)
        plt.xlabel('Years')
        plt.ylabel('MSP (per quintal in rupees)')
        plt.title('Ragi')
        for i in range(len(x)):
            plt.annotate(chr(8377)+str(y[i]),xy=(i,(y[i]+5)))
        plt.show()
    elif a=='4':
        x=['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21 (Expected)']
        y=[768,832,893,925,949,990,1083,1100]
        plt.plot(x,y,marker='o',markersize=5)
        plt.xlabel('Years')
        plt.ylabel('MSP (per quintal in rupees)')
        plt.title('Bhajra')
        for i in range(len(x)):
            plt.annotate(chr(8377)+str(y[i]),xy=(i,(y[i]+5)))
        plt.show()
    elif a=='5':
        x=['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21 (Expected)']
        y=[687,679,744,785,797,817,866,920]
        plt.plot(x,y,marker='o',markersize=5)
        plt.xlabel('Years')
        plt.ylabel('MSP (per quintal in rupees)')
        plt.title('Wheat')
        for i in range(len(x)):
            plt.annotate(chr(8377)+str(y[i]),xy=(i,(y[i]+5)))
        plt.show()
    elif a=='6':
        x=['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21 (Expected)']
        y=[2720,3232,3314,3371,3159,3260,3394,3500]
        plt.plot(x,y,marker='o',markersize=5)
        plt.xlabel('Years')
        plt.ylabel('MSP (per quintal in rupees)')
        plt.title('Groundnut')
        for i in range(len(x)):
            plt.annotate(chr(8377)+str(y[i]),xy=(i,(y[i]+5)))
        plt.show()
    elif a=='7':
        x=['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21 (Expected)']
        y=[120,123,140,140,145,157,156,165]
        plt.plot(x,y,marker='o',markersize=5)
        plt.xlabel('Years')
        plt.ylabel('MSP (per quintal in rupees)')
        plt.title('Sugarcane')
        for i in range(len(x)):
            plt.annotate(chr(8377)+str(y[i]),xy=(i,(y[i]+1)))
        plt.show()
    elif a=='8':
        x=['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21 (Expected)']
        y=[1260,1307,1504,1702,1871,2123,2212,2330]
        plt.plot(x,y,marker='o',markersize=5)
        plt.xlabel('Years')
        plt.title('Sunflower')
        plt.ylabel('MSP (per quintal in rupees)')
        for i in range(len(x)):
            plt.annotate(chr(8377)+str(y[i]),xy=(i,(y[i]+25)))
        plt.show()
    elif a=='9':
        x=['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21 (Expected)']
        y=[1260,1307,1504,1702,1871,2123,2212,2300]
        plt.plot(x,y,marker='o',markersize=5)
        plt.xlabel('Years')
        plt.ylabel('MSP (per quintal in rupees)')
        plt.title('Mustard')
        for i in range(len(x)):
            plt.annotate(chr(8377)+str(y[i]),xy=(i,(y[i]+5)))
        plt.show()
    elif a=='10':
        x=['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21 (Expected)']
        y=[3090,3105,3237,3241,3318,3432,3636,3750]
        plt.plot(x,y,marker='o',markersize=5)
        plt.xlabel('Years')
        plt.title('Ahar(Tur)')
        plt.ylabel('MSP (per quintal in rupees)')
        for i in range(len(x)):
            plt.annotate(chr(8377)+str(y[i]),xy=(i,(y[i]+5)))
        plt.show()


