import pandas as pd
import asyncio
a=pd.read_csv('result.csv')

a['code_chord']=''
a['code_equal']=''
print(a)
import requests
import warnings
warnings.filterwarnings("ignore")
errored=[]
mylongstring=[]
def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)

    return wrapped


def url_status_code(url,i,a):

	try:			
		code1=requests.get(url, verify=False,allow_redirects=True,timeout=10).status_code
		a['code_chord'][i]=code1
		#mylongstring.append(domain+" "+a[1][i])
		if code1==a['code'][i]:
			a['code_equal'][i]=1
		else:
			a['code_equal'][i]=0
		print(url,i,str(code1))
		
	except Exception as e:
		print("exception in url "+str(url))
		a['code_chord'][i]='error'
		a['code_equal'][i]='NA'
		errored.append([url,i])




for i in range(len(a['domain'])):
	url_status_code(a['url'][i],i,a)
print(errored)




print(a)
a.to_csv('result1.csv',index=None)
#print(a['code_equal'].sum())


		#code2=requests.get("https://"+a[1][i], verify=False,allow_redirects=False).status_code
		#if code1==code2:
		#print(url +" "+str(requests.get(url, verify=False,allow_redirects=True).status_code)+ " https://"+str(a[1][i])+" "+str(requests.get("https://"+a[1][i], verify=False,allow_redirects=True).status_code))

		