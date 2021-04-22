def run(a=[],b=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']):
        import matplotlib.pyplot as plt
        def bar_graph(a,b):
                plt.bar(b,a)
                plt.xlabel('Month')
                plt.ylabel('Temperature in degree celsius')
                for i in range(len(a)):
                        plt.annotate(str(a[i])+chr(176)+'C',xy=(i-.25,a[i]+.5))
                plt.show()
        c=bar_graph(a,b)
