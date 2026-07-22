#include <iostream>
using namespace std;
void ans()
{
    int a=0,b=0,n=0,s=0;
    cin>>a>>b>>n>>s;
    
        int x=min(a,s/n);
        int rem=s-(x*n);
        if(rem<=b)
        {
            cout<<"YES"<<"\n";
        }
        else
        {
            cout<<"NO"<<"\n";
        }
    
}
int main()
{
    int q;
    cin>>q;
    while(q--)
    {
        ans();
    }
    return 0;
}