#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 0;
    cin >> t;
    vector<int> result(t);

    for (int j = 0; j < t; j++)
    {
        int n = 0, k = 0;
        cin >> n >> k;
        int temp = k;
        int evens = 0; // Track even numbers for k = 4

        for (int i = 0; i < n; ++i)
        {
            int number = 0;
            cin >> number;

            if (number % 2 == 0)
            {
                evens++;
            }

            int min_op = (k - (number % k)) % k;
            if (min_op < temp)
            {
                temp = min_op;
            }
        }

        // Special case for k = 4
        if (k == 4)
        {
            int ops_for_two_evens = max(0, 2 - evens);
            if (ops_for_two_evens < temp)
            {
                temp = ops_for_two_evens;
            }
        }

        result[j] = temp;
    }

    for (int i = 0; i < t; i++)
    {
        cout << result[i] << "\n";
    }
}