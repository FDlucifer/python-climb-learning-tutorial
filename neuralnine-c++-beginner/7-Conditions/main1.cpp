#include <iostream>

using namespace std;

int main() {

    int a;
    cin >> a;

    if (a > 100) {
        cout << "your number is larger than 100!" << endl;
    } else if (a > 50) {
        cout << "greater than 50!" << endl;
    } else {
        cout << "less or equal to 50!" << endl;
    }

    return 0;
}