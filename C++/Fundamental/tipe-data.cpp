#include <iostream>
#include <climits>
#include <cfloat>

using namespace std;

int main() {

    // Numerikal
    short a;
    int b;
    long c;
    
    // Angka Desimal
    float d;
    double e;

    // Karakter
    char f;

    // Cek maksimum batas bawah dan atas tipe numerikal
    cout << "short: " << SHRT_MIN << " - " << SHRT_MAX << endl;
    cout << "int: " << INT_MIN << " - " << INT_MAX << endl;
    cout << "long: " << LONG_MIN << " - " << LONG_MAX << endl;
    cout << "float: " << FLT_MIN<< " - " << FLT_MAX << endl;
    cout << "double: " << DBL_MIN << " - " << DBL_MAX << endl;

    // Input

    cin >> a >> b >> c >> d >> e >> f;

    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
    cout << d << endl;
    cout << e << endl;
    cout << f << endl;
    return 0;
}