def slices(series, length):
    # Input Validation
    if (series == "") or (length <= 0) or (length > len(series)):
        raise ValueError("Invalid input parameters. Input series must be non-empty and length>0 but less than length of the input series")
    index = 0
    seriesArr = []
    while(index+length <= len(series)):
        seriesArr.append(series[index:index+length])
        index += 1
    return seriesArr



