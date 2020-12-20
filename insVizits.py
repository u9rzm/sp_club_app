from datetime import timedelta
from datetime import datetime
from random import randint
rows=('start_time','contract_id','end_time')
contracts=range(13,113)
def time_list(d,n,id):
    list_d=[] 
    z=0
    for i in range(1,n):
        z+=randint(2,3)
        a=d+timedelta(days=z, minutes=randint(-90,90))
        b=a+timedelta(minutes=randint(60,120))
        list_d.append([a.strftime('%Y-%m-%d %H:%M:%S'),id,b.strftime('%Y-%m-%d %H:%M:%S')])        
    return list_d
vizits_list=[]
for i in contracts:
    date=datetime(2020,12,1,randint(8,21),randint(0,59))
    a=time_list(date,4,i)
    for j in a:
        d=dict(zip(rows,j))
        vizits_list.append(d)   