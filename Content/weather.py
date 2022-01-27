def run():
        import urllib.request,webbrowser
        def internet():
            try :
                stri = "https://www.google.co.in"
                data = urllib.request.urlopen(stri)
                return "Connected"
            except:
                return "not connected"

        a=internet()

        if a=='not connected':
            print('    No Internet ! Please connect to the internet and try again')
        else:
            print('    Weather forcast from Indian Metereological Department')
            print()
            print('    Internet connection successfull')
            print('    Your page is loading')
            print()
            webbrowser.open_new(r'https://mausam.imd.gov.in/')
            
