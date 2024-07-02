import pandas as pd
a=pd.read_csv('1.csv',header=None)
cnt=1;
prev=0
for i in range(10000,50001,10000):
	name='1.'+str(cnt)+'.csv'
	b=a[prev:i+1]
	b.to_csv(name,header=None,index=None)
	cnt+=1
	prev=i
