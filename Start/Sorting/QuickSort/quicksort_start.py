# Example file for Programming Foundations: Algorithms by Joe Marini
# Implement a quicksort


items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]


def quickSort(dataset, first, last):
    if first < last:
        # calulcate the split point
        pivotIdx = partition(dataset, first, last)

        # now sort the two partitions
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)


def partition(datavalues, first, last):
    # TODO: choose the first item as the pivot value
    
    # TODO: establish the upper and lower indexes

    # start searching for the crossing point
    done = False
    while not done:
        # TODO: advance the lower index

        # TODO: advance the upper index

        # TODO: if the two indexes cross, we have found the split point
        pass

    # TODO: when the split point is found, exchange the pivot value

    # TODO: return the split point index


# test the merge sort with data
print(items)
quickSort(items, 0, len(items)-1)
print(items)
