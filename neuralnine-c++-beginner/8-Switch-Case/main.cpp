#include <iostream>

using namespace std;

int main() {
    int x;
    cin >> x;

    switch (x)
    {
    case 8:
        cout << "the value was 8!" << endl;
        break;

    case 10:
        cout << "do the action for input 10!" << endl;
        break;

    default:
        cout << "invalid input!" << endl;
        break;
    }

    return 0;
}