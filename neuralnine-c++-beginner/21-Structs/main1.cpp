#include <iostream>

struct person {
    std::string name;
    int age;
    char gender;
    float weight;

    void print_info() {
        std::cout << "name: " << name << ", age: " << age << ", gender: " << gender << std::endl;
    }
};

int main() {

    struct person p1;
    p1.name = "max";
    p1.age = 25;
    p1.gender = 'm';

    p1.print_info();

    std::cout << sizeof(p1) << std::endl;

    struct person p2;
    p2.name = "anna";
    p2.age = 35;
    p2.gender = 'f';

    p2.print_info();

    std::cout << sizeof(p2) << std::endl;

    return 0;
}