#include <iostream>
using namespace std;

int main()
{
    int count;
    for (int i = 10; i > 0; i--)
    {
        for (int j = i; j > 0; j--)
        {
            cout << "#";
        }
        cout << "\n";
    }
    return 0;
}