def move_zeros(array):
    import numbers

    nozeros = [value for value in array if value is not 0]

    count = len(array) - len(nozeros)

    for i in nozeros:
        if isinstance(i, numbers.Number):
            if str(i) == '0.0':
                nozeros.pop(nozeros.index(i))
                count += 1

    for i in range(0, count):
        nozeros.append(0)

    return nozeros

#    l = [i for i in arr if isinstance(i, bool) or i!=0]
#    return l+[0]*(len(arr)-len(l))
