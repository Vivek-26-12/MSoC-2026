import numpy as np
def main():
    arr2d = np.random.randint(1, 10, size=(3, 3))  # Example: create a random 2D array of shape (3, 3)
    print("Original 2D array:")
    print(arr2d)
    sum = 0
    idx = -1
    for i in range(len(arr2d)):
        temp_sum = 0
        for j in range(len(arr2d[i])):
            temp_sum += arr2d[i][j]
        if temp_sum > sum:
            sum = temp_sum
            idx = i
    print(f"Row with the largest sum: {idx}")
    print(f"Largest sum: {sum}")
main()