def fibonacci(length):
    if (type(length) != int or length < 0):
        print("Positive intergers only")
        return False
    elif (length == 0):
        return 0
    elif (length == 1):
        return 1
    else:
        string = [0, 1]
        for i in range(length):
            i += 1
            if (i > 1):
                string.append(string[i - 1] + string[i - 2])
        return string[(length)]


def lucas(length):
    if (type(length) != int or length < 0):
        print("Positive intergers only")
        return False
    elif (length == 0):
        return 2
    elif (length == 1):
        return 1
    else:
        string = [2, 1]
        for i in range(length):
            i += 1
            if (i > 1):
                string.append(string[i - 1] + string[i - 2])
        return string[(length)]


lucas(1)
lucas(2)
lucas(3)
lucas(4)
lucas(5)
