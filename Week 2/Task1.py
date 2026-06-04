def FindUnique(list):
    uniqueList = []
    for i in list:
        if i not in uniqueList: # checking if the element is not already in the uniqueList
            uniqueList.append(i)
    return uniqueList
def main():
    list = list(map(int,input("Enter numbers separated by space: ").split())) # taking input of numbers and converting them into a list of integers
    uniqueList = FindUnique(list) # finding unique numbers using the FindUnique function
    print("Unique numbers: ", uniqueList)

main()