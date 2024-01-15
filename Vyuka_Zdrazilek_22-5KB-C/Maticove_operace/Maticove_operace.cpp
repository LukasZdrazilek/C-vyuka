#include <iostream>

using namespace std;

struct Matrix 
{
    int** matrix;
    int rows;
    int cols;
};

void print2DMatrix(Matrix matrix) 
{
    for (int i = 0; i < matrix.rows; i++) 
    {
        for (int j = 0; j < matrix.cols; j++) 
            cout << matrix.matrix[i][j] << " ";

        cout << endl;
    }
}

void init2DArray(int**& arr, int rows, int cols) 
{
    arr = new int* [rows];
    for (int i = 0; i < rows; i++) 
        arr[i] = new int[cols];
}

void initMatrix(Matrix& m, int rows, int cols) 
{
    m.rows = rows;
    m.cols = cols;
    init2DArray(m.matrix, rows, cols);
}



void sumMatrix(Matrix m1, Matrix m2) 
{
    Matrix result;
    if (m1.rows == m2.rows && m1.cols == m2.cols) 
    {
        initMatrix(result, m1.rows, m1.cols);
        for (int i = 0; i < m1.rows; i++) 
            for (int j = 0; j < m1.cols; j++) 
                result.matrix[i][j] = m1.matrix[i][j] + m2.matrix[i][j];

        cout << "Vysledek = " << endl;
        print2DMatrix(result);
    }
    else 
        cout << "Matice nejsou kompatibilni ke scitani" << endl;
}

void subMatrix(Matrix m1, Matrix m2) 
{
    Matrix result;
    if (m1.rows == m2.rows && m1.cols == m2.cols) 
    {
        initMatrix(result, m1.rows, m1.cols);
        for (int i = 0; i < m1.rows; i++) 
        {
            for (int j = 0; j < m1.cols; j++) 
                result.matrix[i][j] = m1.matrix[i][j] - m2.matrix[i][j];
        }
        cout << "Vysledek = " << endl;
        print2DMatrix(result);
    }
    else 
        cout << "Matice nejsou kompatibilni k odcitani" << endl;
}

void multiplyMatrix(Matrix m1, Matrix m2) 
{
    if (m1.cols == m2.rows) 
    {
        Matrix result;
        initMatrix(result, m1.rows, m2.cols);
        for (int i = 0; i < m1.rows; i++) 
        {
            for (int j = 0; j < m2.cols; j++) 
            {
                result.matrix[i][j] = 0;
                for (int k = 0; k < m1.cols; k++) 
                    result.matrix[i][j] += m1.matrix[i][k] * m2.matrix[k][j];
            }
        }
        cout << "Vysledek = " << endl;
        print2DMatrix(result);
    }
    else
        cout << "Matice nejsou kompatibilni k nasobeni" << endl;
}

int main() 
{
    Matrix m1, m2;
    int rows, cols;
    char op;

    cout << "Rows: ";
    cin >> rows;

    cout << "Cols: ";
    cin >> cols;

    initMatrix(m1, rows, cols);

    for (int i = 0; i < m1.rows; i++) 
    {
        for (int j = 0; j < m1.cols; j++) 
            m1.matrix[i][j] = rand() % 10;
    }

    print2DMatrix(m1);

    cout << "Vlozte op ( +, -, * ): ";
    cin >> op;

    cout << "Rows: ";
    cin >> rows;

    cout << "Cols: ";
    cin >> cols;

    initMatrix(m2, rows, cols);

    for (int i = 0; i < m2.rows; i++)
    {
        for (int j = 0; j < m2.cols; j++)
            m2.matrix[i][j] = rand() % 10; 
    }

    print2DMatrix(m2);

    switch (op) 
    {
    case '+':
        sumMatrix(m1, m2);
        break;
    case '-':
        subMatrix(m1, m2);
        break;
    case '*':
        multiplyMatrix(m1, m2);
        break;
    default:
        cout << "Neplatny op" << endl;
        break;
    }

    return 0;
}
