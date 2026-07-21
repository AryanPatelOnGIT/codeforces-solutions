#include <iostream>
using namespace std;
int main()
{
    int n=0;int pol=0;int count=0;
    cin>>n;
    int* dep=new int[n];
    for (int i=0;i<n;i++)
    {
        cin>>dep[i];
        if(dep[i]==-1 && pol==0)
        {
            count++;
        }
        else if(dep[i]==1)
        {
            pol++;
        }
        else 
        {
            pol--;
        }
    }
    cout<<count;
}
