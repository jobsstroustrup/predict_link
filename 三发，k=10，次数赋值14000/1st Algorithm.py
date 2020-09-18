x=open('linkdata1.txt','r')
A=[]
while True:
    a=x.readline()
    if a=='':
	    break
    else:a1=[int(a.split()[i]) for i in range(3)]
    A.append(a1)
#异常数据变中值
for x in A:
    if x[2]>=1000000:
        x[2]=46744
    if x[2]==0:
        x[2]=46744


        
max1=0
for x in A:
    max1=max(max1,x[0],x[1])
U=[i for i in range(max1)]

s=[0]*max1
S=[]
for i in range(max1):
    S.append(s.copy())

s0=[0]*max1
S0=[]
for i in range(max1):
    S0.append(s0.copy())

s1=[0]*max1
S1=[]
for i in range(max1):
    S1.append(s1.copy())

s2=[0]*max1
S2=[]
for i in range(max1):
    S2.append(s2.copy())
    
for x in A:
    S[x[0]-1][x[1]-1]+=x[2]+46744
    S[x[1]-1][x[0]-1]+=x[2]+46744

for x in A:
    S0[x[0]-1][x[1]-1]+=1
    S0[x[1]-1][x[0]-1]+=1

for x in A:
    S1[x[0]-1][x[1]-1]+=1
    S2[x[0]-1][x[1]-1]+=S1[x[1]-1][x[0]-1]
    S2[x[1]-1][x[0]-1]+=S1[x[1]-1][x[0]-1]

for i in range(max1):
    for j in range(max1):
        S[i][j]+=10*S2[i][j]*14000

for i in range(max1):
    for j in range(max1):
        S[i][j]+=S0[i][j]*14000


p1=[0]*max1
P1=[]
for i in range(max1):
    P1.append(p1.copy())

for i in range(max1):
    for j in range(max1):
        if S[i][j]>0:
            for k in range(max1):
                if S[i][k]>0 and k!=j and S[j][k]==0:
                    P1[j][k]+=S[i][j]*S[i][k]
                    P1[k][j]+=S[i][j]*S[i][k]
                if S[j][k]>0 and k!=i and S[i][k]==0:
                    P1[i][k]+=S[j][i]*S[j][k]
                    P1[k][i]+=S[j][i]*S[j][k]

xu=[]
for i in range(max1):
    for j in range(i,max1):
        xu.append([P1[i][j],i,j])
xu=sorted(xu)
xu.reverse()
P=[[xu[i][1],xu[i][2]] for i in range(10000)]

f1=open('S.txt','w')
f2=open('P1.txt','w')
f3=open('P.txt','w')
for i in range(max1):
    for j in range(i,max1):
        if S[i][j]!=0:
            f1.write(str(i+1)+' '+str(j+1)+' '+str(S[i][j])+'\n')
for i in range(max1):
    for j in range(i,max1):
        if P1[i][j]!=0:
            f2.write(str(i+1)+' '+str(j+1)+' '+str(P1[i][j])+'\n')
for i in range(10000):
    f3.write(str(P[i][0]+1)+'\t'+str(P[i][1]+1)+'\n')

f1.close()
f2.close()
f3.close()

    





