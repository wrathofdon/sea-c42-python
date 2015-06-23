def fibonacci(length):
    if (type(length) != int or length < 0):
        print("Positive intergers only")
        return False
        """This is error checking"""
    elif (length == 0):
        return 0
    elif (length == 1):
        return 1
        """Addition is only necessary if the parameter is 2 or more"""
    else:
        string = [0, 1]
        """The sequence is represented as a list"""
        for i in range(length):
            if (i > 0):
                string.append(string[i] + string[i - 1])
                """if addition is necessary, it only counts if the string is
                more than 2.  At which point, you add the previous numbers on
                list and append the new sum."""
        return string[(length)]
        """Once range is completeled, we return the last number on list"""


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
            if (i > 0):
                string.append(string[i] + string[i - 1])
        return string[(length)]


def sum_series(length, x=0, y=1):
    """Default starting numbers are 0 & 1 unless otherwise specified"""
    if (type(length) != int or length < 0):
        print("Positive intergers only")
        return False
    elif (length == 0):
        return x
    elif (length == 1):
        return y
    else:
        string = [x, y]
        for i in range(length):
            if (i > 0):
                string.append(string[i] + string[i - 1])
        return string[(length)]


sum_series(10)
sum_series(10, 2, 1)
sum_series(10, 4, 53)
sum_series(10, 27, 4)
"""This was just a test"""
