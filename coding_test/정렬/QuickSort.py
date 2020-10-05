def QuickSortAsc(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    tail  = lst[1:]

    l_side = [item for item in tail if item <= pivot]
    r_side = [item for item in tail if item > pivot]

    return QuickSort(l_side) + [pivot] + QuickSort(r_side)


def QuickSortDesc(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    tail  = lst[1:]

    l_side = [item for item in tail if item > pivot]
    r_side = [item for item in tail if item <= pivot]

    return QuickSort(l_side) + [pivot] + QuickSort(r_side)