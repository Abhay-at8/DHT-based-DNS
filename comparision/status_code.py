import pandas as pd
import asyncio
#a=pd.read_csv('report.csv',header=None)
a=pd.read_csv('comp.csv',index_col=0)

#a=b[:40]
a.rename(columns = {'url':0}, inplace = True)
#a=a.drop([2,3], axis=1)
a['code']=''
a['url']=''
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


def url_status_code(prot,domain,i,a):

	try:	
		url=""
		url=prot+"://"+str(domain)
		print("The link is "+url)		
		code1=requests.get(url, verify=False,allow_redirects=True,timeout=10).status_code
		a['code'][i]=code1
		a['url'][i]=url
		#mylongstring.append(domain+" "+a[1][i])
		print(url,i,str(code1))
		
	except Exception as e:
		print("exception in url "+str(url))
		if prot=="https":
			errored.append([domain,i])
			a['code'][i]='error'


@background
def url_http(prot,domain,i,a):

	try:
		url="http://"+domain
		code1=requests.get(url, verify=False,allow_redirects=True,timeout=50).status_code
		a['code'][i]=code1
		a['url'][i]=url
		print(url,i,str(code1))
		
	except Exception as e:
		print("exception in url "+str(url))
		
		a['code'][i]='error'


                         # Wait until finish

for i in range(len(a[0])):
	url_status_code("https",a[0][i],i,a)
print(errored)

for i in range(len(errored)):
	url_status_code("http",errored[i][0],errored[i][1],a)

a.rename(columns = {0:'domain'}, inplace = True)
print(a)
a.to_csv('result_before_dropping.csv',index=None)
a.dropna(inplace=True)
#a.reset_index(inplace=True)
a.to_csv('result.csv',index=None)
a.reset_index(inplace=True)
for i in range(len(a['domain'])):
	ip=str(a['chord_IP'][i]).split('_')[0]
	if a['code'][i]!='error' and  ip!='null':
		mylongstring.append(ip+" "+a['domain'][i])



f = open("temporary.txt","w+")
f.writelines([i + '\n' for i in mylongstring])
f.close()



		#code2=requests.get("https://"+a[1][i], verify=False,allow_redirects=False).status_code
		#if code1==code2:
		#print(url +" "+str(requests.get(url, verify=False,allow_redirects=True).status_code)+ " https://"+str(a[1][i])+" "+str(requests.get("https://"+a[1][i], verify=False,allow_redirects=True).status_code))

		