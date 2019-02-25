l,m,=map(int,input().split())
for i in range(l,m):
 y=i
 t=0
 u=0
 while(y>0):
    o=y%10
    o=o*o*o
    u=u+o
    y=int(y/10)
if(u==i):
  if(t==1):
       print(" ")
       print(u,end=" ")
  else:
       print(u,end=" ")
       t=1
   
