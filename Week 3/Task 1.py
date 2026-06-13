import numpy as np
def main():
    arr = np.random.randint(1, 10, size=5)  # Example: create a random array of 5 elements
    print("Original array:", arr)
    print("Sum of elements:", np.sum(arr))
    print("Mean of elements:", np.mean(arr))
    print("Maximum element:", np.max(arr))
main()