import numpy as np
def main():
    arr2d = np.random.randint(60,100,size=(3,3))
    print("Original 2D array:")
    print(arr2d)
    result = []
    for i in range(len(arr2d)):
        if np.mean(arr2d[i]) > 75:
            result.append(i)
    print("Rows with averages greater than 75:", result)
main()