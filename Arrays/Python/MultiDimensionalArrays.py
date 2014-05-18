#!/usr/bin/python

def InitializeArray(bounds):
    NumDimensions = len(bounds) / 2
    LowerBound = [0 for x in range(NumDimensions)]
    SliceSize = [0 for x in range(NumDimensions)]

    slice_size = 1
    for i in range(NumDimensions-1, -1, -1):
        SliceSize[i] = slice_size

        LowerBound[i] = bounds[2 * i]
        upper_bound = bounds[2 * i + 1]
        bound_size = upper_bound - LowerBound[i] + 1
        slice_size *= bound_size

    Values = [0 for x in range(slice_size)]
    return (Values, LowerBound, SliceSize)

def MapIndicesToIndex(indices, LowerBound, SliceSize):
    index = 0
    for i in range(len(indices)):
        index += (indices[i] - LowerBound[i]) * SliceSize[i]

    return index

if __name__ == "__main__":
    array, bounds, sizes = InitializeArray([0,2,0,2])
    print "Before: " + str(array)
    val = 0
    for i in range(3):
        for j in range(3):
            array[MapIndicesToIndex([i,j],bounds, sizes)] = val
            val += 1
    print "After: " + str(array)
