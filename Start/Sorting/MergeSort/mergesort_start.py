# Example file for Programming Foundations: Algorithms by Joe Marini
# Implement a merge sort with recursion


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # TODO: recursively break down the arrays


        # TODO: now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # TODO: while both arrays have content


        # TODO: if the left array still has values, add them


        # TODO: if the right array still has values, add them



# test the merge sort with data
print(items)
mergesort(items)
print(items)
