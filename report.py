import pandas as pd
import datetime,time
a=pd.read_csv('report.csv',header=None)
print(a[2].mean())

#import dnspython3
# from dnspython import resolver

# result = resolver.query('tutorialspoint.com', 'A')
# for ipval in result:
#     print('IP', ipval.to_text())
import socket
pd.options.mode.chained_assignment = None
import warnings
warnings.filterwarnings("ignore")
import datetime,time

cp=a.copy()

for i in range(len(a[0])):
    start=time.time_ns()
    try:
        start1 = datetime.datetime.now()
        start=time.time_ns()
        # your code here    

        addr1 = socket.gethostbyname_ex(cp[0][i])
        time_taken=time.time_ns() - start
        cp[1][i]=addr1[2][0]
        cp[2][i]=time_taken/1000000
        print(addr1[2][0],time_taken)
    except Exception as e:
        print(e)
        time_taken=time.time_ns() - start
        cp[1][i]='NA'
        cp[2][i]=time_taken/1000000
        

a.drop(3, axis=1, inplace=True)
cp.drop(3, axis=1, inplace=True)

a.rename(columns = {0:'url',1:'chord_IP',2:'chord_time'}, inplace = True) 
cp.rename(columns = {0:'url',1:'reg_IP',2:'reg_time'}, inplace = True) 

#print(a)
res2 = pd.merge(a, cp, on='url')
print(res2)
res2.to_csv('comp.csv')
#print(len(res2[0]))


# df=pd.read_csv('comp.csv')
# print(df)
