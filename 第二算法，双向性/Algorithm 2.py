#Algorithm 2

#只考虑次数，不考虑时间.f=总阅读次数+k*互相阅读次数之积.g=强度积的和.
#k为参数

k=2

x=open('linkdata1.txt','r')
A=[]
while True:
    a=x.readline()
    if a=='':
	    break
    else:a1=[int(a.split()[i]) for i in range(3)]
    A.append(a1)

max1=0
for x in A:
    max1=max(max1,x[0],x[1])

#f,S

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
    S0[x[0]-1][x[1]-1]+=1
    S0[x[1]-1][x[0]-1]+=1

for x in A:
    S1[x[0]-1][x[1]-1]+=1
    S2[x[0]-1][x[1]-1]+=S1[x[1]-1][x[0]-1]
    S2[x[1]-1][x[0]-1]+=S1[x[1]-1][x[0]-1]

for i in range(max1):
    for j in range(max1):
        S[i][j]=S0[i][j]+k*S2[i][j]

#g

p1=[0]*max1
P1=[]
for i in range(max1):
    P1.append(p1.copy())

for i in range(max1):
    for j in range(i,max1):
        if S[i][j]>0:
            for k in range(max1):
                if S[i][k]>0 and k!=j and S[j][k]==0:
                    P1[j][k]+=S[i][j]*S[i][k]
                    P1[k][j]+=S[i][j]*S[i][k]
                if S[j][k]>0 and k!=i and S[i][k]==0:
                    P1[i][k]+=S[j][i]*S[j][k]
                    P1[k][i]+=S[j][i]*S[j][k]

P1_xu=[]
for i in range(max1):
    for j in range(i,max1):
        if P1[i][j]>0:
            P1_xu.append([P1[i][j],i,j])
P1_xu=sorted(P1_xu)
P1_xu.reverse()
P=[[P1_xu[i][1],P1_xu[i][2]] for i in range(10000)]

f1=open('2nd_S.txt','w')
f2=open('2nd_P1_xu.txt','w')
f3=open('2nd_P.txt','w')
for i in range(max1):
    for j in range(i,max1):
        if S[i][j]!=0:
            f1.write(str(i+1)+'\t'+str(j+1)+'\t'+str(S[i][j])+'\n')
for x in P1_xu:
    f2.write(str(x[1]+1)+'\t'+str(x[2]+1)+'\t'+str(x[0])+'\n')
    
for i in range(10000):
    f3.write(str(P[i][0]+1)+'\t'+str(P[i][1]+1)+'\n')

f1.close()
f2.close()
f3.close()














    

