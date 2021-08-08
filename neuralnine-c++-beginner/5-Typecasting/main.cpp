#include <iostream>

using std::cout;
using std::endl;
using std::string;

int main() {
    string s = "1023";
    int i = stoi(s);

    cout << i + 100 << endl;

    float f = 10.78;
    int i = f;

    cout << i << endl;

    return 0;
}