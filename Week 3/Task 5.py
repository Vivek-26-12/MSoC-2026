import numpy as np
def main():
    traffic = np.random.randint(0,600,size=(5,3))
    print("Traffic data:")
    print(traffic)
    avg_traffic = np.mean(traffic)

    print("Average traffic:", avg_traffic)

    result = []
    for i in range(len(traffic)):
        if np.mean(traffic[i]) > avg_traffic:
            result.append(i)
    print("Days with above average traffic:", result)
main()