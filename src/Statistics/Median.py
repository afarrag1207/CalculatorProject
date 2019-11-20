def median(pool):
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return int(copy[int((size-1) / 2)])
    else:
        return (int(copy[int((size) / 2)-1]) + int(copy[int(size / 2)])) / 2
