import numpy as np
def main():
    arr = np.random.randint(1, 10, size=5)  # Example: create a random array of 5 elements
    print("Original array:", arr)
    EvenArr = arr[arr % 2 == 0]  # Filter even numbers from the array
    print("Even numbers in the array:", EvenArr)  # Print even numbers from the array
main()