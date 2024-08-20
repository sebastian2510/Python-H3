def detect_ranges(l1):
    ranges = []
    l1.sort()
    start = l1[0]
    end = l1[0]
    for i in range(1, len(l1)):
        if l1[i] - l1[i - 1] == 1:
            end = l1[i]
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"({start},{end + 1})")
            start = l1[i]
            end = l1[i]
    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"({start},{end + 1})")
    return ranges

if __name__ == "__main__":
    print(detect_ranges([2,5,4,8,12,6,7,10,13]))