#include <iostream>
using namespace std;
int main()
{

    int op1, op2;
    char oprt;

    oprt = '+', '-', '*', '/';

    printf("=========================================\n");
    printf("KALKULATOR SEDERHANA\n");
    printf("=========================================\n");

    // Masukan Input
    cout << ("Masukan operand 1: ");
    cin >> op1;
    cout << endl;

    cout << ("Masukan operator yang diinginkan! (\"+\", \"-\", \"*\", \"/\"): ");
    cin >> oprt;
    cout << endl;

    cout << ("Masukan operand 2: ");
    cin >> op2;
    cout << endl;

    // Operasi terhadap input
    switch (oprt)
    {
    case '+':
        cout << "Hasilnya adalah: " << (op1 + op2) << endl;
        break;

    case '-':
        cout << "Hasilnya adalah: " << (op1 - op2) << endl;
        break;

    case '*':
        cout << "Hasilnya adalah: " << (op1 * op2) << endl;
        break;

    case '/':
        if (op2 != 0)
        {
            cout << "Hasilnya adalah: " << (op1 / op2) << endl;
        }
        else
        {
            cout << "Tidak terdefinisi" << endl;
        }
        break;
    }
    return 0;
}
