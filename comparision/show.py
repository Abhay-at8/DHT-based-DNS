import pandas as pd
from datetime import date

a=pd.read_csv('result1.csv')
b=a[['url','eq','code_equal','code','code_chord']]
print("-----------------------------------------------------------------------")
print(date.today())
print('Total sample')
print(f"{len(b)} eq {len(b[b['code_equal']==1])} not eq {len(b[b['code_equal']!=1])}")

with open("results.txt", "a") as myfile:
	eq=f"{date.today()} equal {len(b[b['code_equal']==1])} not equal {len(b[b['code_equal']!=1])}\n-----------------\n"
	myfile.write(eq)
#print(b[b['code_equal']!=1])

print('\nIP equal case')
c=b[b['eq']==1]
print(f"{len(c)} eq {len(c[c['code_equal']==1])} not eq {len(c[c['code_equal']!=1])}")

print('\nIP not equal case')
c=b[b['eq']!=1]
print(f"{len(c)} eq {len(c[c['code_equal']==1])} not eq {len(c[c['code_equal']!=1])}")


print('\ncode equal case')

c=b[b['code_equal']==1]
print(f"{len(c)} eq {len(c[c['eq']==1])} not eq {len(c[c['eq']!=1])}")

print('\ncode not equal case')
c=b[b['code_equal']!=1]
print(f"{len(c)} eq {len(c[c['eq']==1])} not eq {len(c[c['eq']!=1])}")

