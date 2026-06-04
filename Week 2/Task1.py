def FindUnique(list):
    uniqueList = []
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList
def main():
    list = list(map(int,input("Enter numbers separated by space: ").split()))
    uniqueList = FindUnique(list)
    print("Unique numbers: ", uniqueList)

main()