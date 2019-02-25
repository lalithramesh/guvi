r,s,=map(int,input().split())
for i in range(r,s):
 y=i
 t=0
 u=0
 while(y>0):
    p=y%10
    p=p*p*p
    u=u+p
    y=int(y/10)
if(u==i):
  if(t==1):
       print(" ")
       print(u,end=" ")
  else:
       print(u,end=" ")
       t=1
   
