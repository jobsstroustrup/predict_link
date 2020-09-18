#include<cstdio>
#include<cstdlib>
#include<iostream>
#include <algorithm>
using namespace std;
int map[6000][6000],ave = 14000,lim = 1000000,num = 5775,cnt = 0;


int main()
{
    freopen("train.txt","r",stdin);
    int u,v,t,i=0,sum=0;
    while(scanf("%d%d%d",&u,&v,&t)!=EOF){
        if(t > lim) t = ave;
        if(t==0)t=ave;
        i+=1;
        sum+=t;

    }
    cout<<sum/i;
}
