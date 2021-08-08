#include <iostream>

using namespace std;

int main() {
    int n1, n2;
    char op;

    cout << "enter the first number: ";
    cin >> n1;
    cout << "choose an arithmetic operation: ";
    cin >> op;
    cout << "enter the second number: ";
    cin >> n2;

    switch(op) {
        case '+':
            cout << n1 + n2 << endl;
            break;
        case '-':
            cout << n1 - n2 << endl;
            break;
        case '*':
            cout << n1 * n2 << endl;
            break;
        case '/':
            cout << n1 / n2 << endl;
            break;
        case '%':
            cout << (int) n1 % (int) n2 << endl;
            break;
        default:
            cout << "operator not support!" << endl;
            break;
    }

    return 0;
}