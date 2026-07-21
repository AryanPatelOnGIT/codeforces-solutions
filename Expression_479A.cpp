#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int x=0,y=0,z=0;
    cin>>x;
    cin>>y;
    cin>>z; 
    int s=x*(y+z);
    int s1=(x+y)*z;
    int s2=x*y*z;
    int s3=x+y*z;
    int s4=x*y+z;
    cout<<max({s,s1,s2,s3,s4})<<endl;
}