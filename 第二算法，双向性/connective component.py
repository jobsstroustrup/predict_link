#计算联通分支

x=open('linkdata1.txt','r')
A=[]
while True:
    a=x.readline()
    if a=='':
	    break
    else:a1=[int(a.split()[i]) for i in range(3)]
    A.append(a1)

#对任意无向图G,计算其所有联通分支，结果以节点的列表为元素的列表表示.G以对称01矩阵形式表示.
def lt(G):
    def flt(G,n):#计算由n开始的第一个联通分支.G不能是空集.
        lian=[n]
        lian_step=[n]
        while True:
            delta=[]
            for x in lian_step:
                for i in range(len(G)):
                    if G[x][i]==1 and i not in lian and i not in delta:
                        delta.append(i)
            if delta==[]:
                break
            lian+=(delta)
            lian_step=delta
        print('该分支共有',len(lian),'个节点')
        return lian

    
    
    #正式计算
    fenzhi=[]
    dian=[]
    while True:
        for n in range(max1):
            if n not in dian:
                break
        else:return fenzhi
        lian=flt(G,n)
        fenzhi.append(lian)
        dian+=lian
    

#总节点数
max1=0
for x in A:
    max1=max(max1,x[0],x[1])

G1=[0]*max1
G=[]
for i in range(max1):
    G.append(G1.copy())



for x in A:
    G[x[0]-1][x[1]-1]=1
    G[x[1]-1][x[0]-1]=1



fenzhi=lt(G)

print('一共有',len(fenzhi),'个联通分支')

    
        
                
                
            
    
