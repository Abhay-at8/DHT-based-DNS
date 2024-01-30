import pandas as pd
import sys,shutil
a=pd.read_csv('comp.csv')
print(sys.argv[1],a['chord_time'].mean(),a['reg_time'].mean())
colnames=['scenario','chord_avg','normal_avg'] 
df=pd.read_csv('final_comparision.csv',names=colnames,header=0)
  
dic={'scenario':[sys.argv[1]],'chord_avg':[a['chord_time'].mean()],'normal_avg':[a['reg_time'].mean()]}
df2=pd.DataFrame(dic)
#df.loc[len(df.index)] =[sys.argv[1],a['chord_time'].mean(),a['reg_time'].mean()]
#df = df.append(df2, ignore_index = True) 
df = pd.concat([df, df2], ignore_index = True) 
print(df)
df.to_csv('final_comparision.csv')
new_cmp='test_report/'+str(sys.argv[1])+'_comp.csv'
new_rp='test_report/'+str(sys.argv[1])+'_report.csv'
print(new_rp,new_cmp)
shutil.copy2('report.csv',new_rp)
shutil.copy2('comp.csv',new_cmp)

