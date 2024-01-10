#include <iostream>

using namespace std;

struct Matrix               // strukture matice
{
    int** matrix;
    int rows;
    int cols;
};

void print2DMatrix(Matrix* matrix)
{
    for (int i = 0; i < matrix -> rows; i++)              // fce pro vypsani matice
    {
        for (int j = 0; j < matrix -> cols; j++)
            cout << matrix -> matrix[i][j] << "\t";
        cout << endl;
    }
    cout << endl;
}

int** init2DArray(int rows, int cols)       // inicializace 2D pole
{
    int** matrix = new int* [rows];
    for (int i = 0; i < rows; i++)
    {
        matrix[i] = new int[cols];
    }
    return matrix;
}

Matrix* initMatrix(int rows, int cols)      // konstruktor matice
{
    Matrix*  m = new Matrix;
    m -> cols = cols;
    m -> rows = rows;
    m -> matrix = init2DArray(rows, cols);
    return m;
}

void sumMatrix(Matrix* matrix1, Matrix* matrix2, Matrix* matrix3, int rows, int cols)
{           // scitani matic
    
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            matrix3 -> matrix[i][j] = matrix1 -> matrix[i][j] + matrix2 -> matrix[i][j];
        }
    }
}

void subMatrix(Matrix* matrix1, Matrix* matrix2, Matrix* matrix3, int rows, int cols)
{          // odcitani matic
    
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            matrix3 -> matrix[i][j] = matrix1 -> matrix[i][j] - matrix2 -> matrix[i][j];
        }
    }
}

void multiplyMatrix(Matrix* matrix1, Matrix* matrix2, Matrix* matrix3, int rows1, int cols1, int cols2)
{
    for (int i = 0; i < rows1; i++)
    {
        for (int j = 0; j < cols2; j++)
        {
            matrix3->matrix[i][j] = 0;
            for (int k = 0; k < cols1; k++)
            {
                matrix3->matrix[i][j] += matrix1->matrix[i][k] * matrix2->matrix[k][j];
            }
        }
    }
}


int main()
{
    int rows, cols, cols2;

    cout << "Rows: ";
    cin >> rows;

    cout << "Columns: ";
    cin >> cols;

    Matrix* matrix1 = initMatrix(rows, cols);

    for (int i = 0; i < rows; i++)
    {                                   // naplneni matice random cisly 0 - 9
        for (int j = 0; j < cols; j++)
        {
            matrix1 -> matrix[i][j] = rand() % 9;
        }
    }

    print2DMatrix(matrix1);

    ////////////////////// znovu pro matici 2 //////////////////////

    cout << "Rows: ";
    cin >> rows;

    cout << "Cols: ";
    cin >> cols2;

    Matrix* matrix2 = initMatrix(rows, cols);

    for (int i = 0; i < rows; i++)
    {                                   // naplneni matice random cisly 0 - 9
        for (int j = 0; j < cols; j++)
        {
            matrix2 -> matrix[i][j] = rand() % 9;
        }
    }

    print2DMatrix(matrix2);

    ///////////////// matice 3 vysledkova //////////////
    
    Matrix* matrix3 = initMatrix(rows, cols);

    sumMatrix(matrix1, matrix2, matrix3, rows, cols);

    print2DMatrix(matrix3);

    subMatrix(matrix1, matrix2, matrix3, rows, cols);

    print2DMatrix(matrix3);

    multiplyMatrix(matrix1, matrix2, matrix3, rows, cols, cols2);

    print2DMatrix(matrix3);

    return 0;
}
