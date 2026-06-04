import numpy as np

def main():
    n, m = map(int, input("Enter rows and columns (e.g., 3 4): ").split())
    matrix = []
    for i in range(m):
        row = np.random.randint(1,100, n)
        matrix.append(row)
    print("Generated Matrix :")
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()
    print("Transposed Matrix :")
    for i in range(n):
        for j in range(m):
            print(matrix[j][i], end=" ")
        print()
main()