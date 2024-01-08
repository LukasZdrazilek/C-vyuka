#include <iostream>

using namespace std;

void prehod (int* a, int* b)
{
    int temp = *a;      // ulozi se hodnota a
    *a = *b;
    *b = temp;
}

int main()
{
    int a = 2;
    int b = 5;

    cout << "a = " << a << ", b = " << b << endl;

    prehod (&a, &b);

    cout << "a = " << a << ", b = " << b << endl;


    return 0;
}