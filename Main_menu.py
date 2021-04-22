def run(f,n):
    print()
    print("                                                            Welcome",n)
    while True:
        print('''
=====================================================================================================================================

    The available functions are:

                                                1. Average seasonal taluk-wise rainfall data
                                                2. Annual taluk-wise rainfall data
                                                3. Average monthly temperature data
                                                4. Crops and their requirements
                                                5. Get a crop suggestion based on the available conditions
                                                6. Variation in market rates of various crops (previous years' trends)
                                                7. Schemes available from the government
                                                8. Weather forcast
                                                9. Place an order for the seeds
                                                10. Update crop status
                                                11. Help
                                                12. Sign-Out''')
        print()
        a=input('                             Enter your choice: ')
        b=a.lower()
        if b=='1' or b=='average seasonal taluk-wise rainfall data':
            print()
            print('============================================== Average seasonal taluk-wise rainfall data ============================================')
            print()
            import district
            a,b=district.run()
            import Rainfalldat_csvreader as rc
            rc.run(a,b)
            continue
        elif b=='2' or b=='annual taluk-wise raindfall data':
            print()
            print('================================================== Annual taluk-wise rainfall data ==================================================')
            print()
            import district
            a,b=district.run()
            import ANRainfalldat_csvreader as rc
            rc.run(a,b)
            continue
        elif b=='3' or b=='average temperature data':
            print()
            print('=================================================== Average monthly teperature data =================================================')
            print()
            import district
            a,b=district.run()
            import tempdat_csvreader as rc
            rc.run(a)
            continue
        elif b=='4' or b=='crops and their requirements':
            print()
            print('========================================================= Crops and their info ======================================================')
            import cropreqread
            cropreqread.run()
            continue
        elif b=='5' or b=='Get a crop suggestion based on the available conditions':
            print()
            print('=========================================================== Crop Suggestion =========================================================')
            print()
            import district
            a,b=district.run()
            m=int(input('''    Select month in which the seeds are to be sown:
                                                           1. January
                                                           2. Febraury
                                                           3. March
                                                           4. April
                                                           5. May
                                                           6. June
                                                           7. July
                                                           8. August
                                                           9. September
                                                           10.October
                                                           11.November
                                                           12.December
                                                    Enter your choice: '''))
            import cropsugg
            cropsugg.run(a,b,m)
            continue
        elif b=='6' or b=="variation in market rates of various crops (previous years' trends)":
            print()
            print('================================= Variation in market rates of various crops (previous years\' trends) ===============================')
            print()
            import plot
            plot.run()
            continue
        elif b=='7' or b=='schemes available from the govenment':
            print()
            print('============================================== Schemes available from the Government ================================================')
            print()
            import schemes
            schemes.run()
            continue
        elif b=='8' or b=='weather forcast':
            print()
            print('========================================================= Weather Forcast ===========================================================')
            print()
            import weather
            weather.run()
            continue
        elif b=='9' or b=='place an order for the seeds':
            print()
            print('===================================================== Place an Order for Seeds ======================================================')
            import seedbin
            seedbin.run(f)
            continue
        elif b=='10' or b=='update crop status':
            print()
            print('======================================================== Updating Crop Status =======================================================')
            print()
            import status
            status.run(f)
            continue
        elif b=='11' or b=='Help':
            print()
            import guidelines as g
            g.run()
            continue
        elif b=='12' or b=='Sign-Out':
            print()
            print('Thank you for using this service')
            break
        else:
            print()
            print('Invalid input.')
            print('Refer the help forum for more details.')
            print()
            import guidelines as g
            g.run()
            continue
            

