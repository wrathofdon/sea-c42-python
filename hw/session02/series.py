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
            if (i > 1):
                string.append(string[i - 1] + string[i - 2])
        print(string[(len(string))])


fibonacci(3)
