#include <iostream>

using std::cout;
using std::endl;
using std::string;

int main() {
    int i = 1423412341234123;
    string s1 = "this number is: ";
    string s2 = std::to_string(i);

    cout << s1 + s2 << endl;

    return 0;
}