def run():
    import urllib.request,webbrowser,time
    
    def internet():
        try :
            stri = "https://www.google.co.in"
            data = urllib.request.urlopen(stri)
            return "Connected"
        except:
            return "not connected"
    while True:
        try:
            a=internet()
            b=int(input('''    Choose:
                                    1. Schemes for agriculture available from Govenment of Karnataka
                                    2. Schemes for agriculture available from Government of India
                                    3. Exit

                 Enter your choice: '''))
            if b==1:
                if a=='not connected':
                    print('    No Internet ! Please connect to the internet and try again')
                else:
                    print('    Internet connection successfull')
                    print('    Your page is loading')
                    print()
                    webbrowser.open_new(r'https://raitamitra.karnataka.gov.in/english')
            elif b==2:
                if a=='not connected':
                    print('    No Internet ! Please connect to the internet and try again')
                else:
                    print('    Internet connection successfull')
                    print('    Your page is loading')
                    print()
                    webbrowser.open_new(r'http://agricoop.nic.in/')
            elif b==3:
                break
            time.sleep(7)
        except:
            #continue
            print('===> Enter proper input <===')
            continue

