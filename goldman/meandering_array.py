def meanderingArray(unsortedArray):
    # sort array in ascending order
    ascendingSort = sorted(unsortedArray)
    # create empty list to sort items in meandering order
    meanderedArray = []

    # Giving that the array is not empty or with only one element,
    while len(ascendingSort) > 1:
        # take the biggest and smallest from the ascendingSort list and add the to the meandering list
        meanderedArray += [ascendingSort[-1], ascendingSort[0]]
        # remove the biggest and smallest from the ascending sort list to allow for new biggest and new smallest
        ascendingSort = ascendingSort[1:-1]

    # add whatever is left of ascending sort list to the meanderedArray (i.e. empty or 1 item)
    meanderedArray += ascendingSort

    return meanderedArray
