# with python methods

arr = [3,1,2]
n = len(arr)
currentList = []
def subseqPrinting(index, currentList, arr, n):
    if index >= n:                # base condition
        print(currentList)
        return 
    
    currentList.append(arr[index])
    subseqPrinting(index+1, currentList, arr, n)
    currentList.remove(arr[index])
    subseqPrinting(index+1, currentList, arr, n)

subseqPrinting(0, currentList, arr, n)

# with list appending
print()
print("with list appending")
arr = [3,1,2]
n = len(arr)
currentList = []
def subseqPrinting(index, currentList, arr, n):
    if index >= n:                # base condition
        print(currentList)
        return 
    
    subseqPrinting(index+1, currentList + [arr[index]], arr, n)
    subseqPrinting(index+1, currentList, arr, n)

subseqPrinting(0, currentList, arr, n)