p=input()
q=input()
p=p.split()
q=q.split()
sum=0
for i in range(int(p[1])):
    sum=sum+int(q[i])
print(sum)
