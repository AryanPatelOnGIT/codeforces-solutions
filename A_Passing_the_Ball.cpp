#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    int t = 0;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int k = 0;
        cin >> k;
        string s;
        cin >> s;
        int players = 0;                     // start at student 1 (index 0)
        vector<bool> visited(k, false);      // keep track of who got the ball
        visited[players] = true;

        for (int j = 0; j < k; j++)          // exactly k passes
        {
            if (s[players] == 'R')
                ++players;                   // pass to the right neighbour
            else
                --players;                   // pass to the left neighbour
            visited[players] = true;         // mark this student
        }

        int ans = 0;
        for (bool v : visited)
            if (v) ++ans;
        cout << ans << '\n';
    }
}
