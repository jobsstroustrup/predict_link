#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int link[10000][2];
    ifstream fin("P.txt");
    int i=0;
    if(!fin){
        cout<<"can't find"<<endl;
    }
    while (!fin.eof())
    {
        fin>>link[i][0]>>link[i][1];

        i+=1;
    }
    cout<<link[0][0]<<" "<<link[0][1]<<endl;
    return 0;

}
