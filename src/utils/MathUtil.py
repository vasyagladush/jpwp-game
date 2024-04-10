def constrain_int(num: int, min: int, max: int) -> int:
    if num < min:
        return min
    elif num > max:
        return max
    else:
        return num