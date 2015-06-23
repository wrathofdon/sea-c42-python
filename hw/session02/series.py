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
        print(string[(length)])


fibonacci(1)
fibonacci(2)
fibonacci(3)
fibonacci(4)
fibonacci(5)
