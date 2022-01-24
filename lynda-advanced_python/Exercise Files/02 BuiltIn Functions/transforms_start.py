
# use transform functions like sorted, filter, map


def filterFunc(x):
    if x % 2 == 0:
        return False
    else:
        return True


def filterFunc2(x):
    if x.islower():
        return True
    else:
        return False


def squareFunc(x):
    pass


def toGrade(x):
    if x >= 90:
        return "A"
    elif x > 80:
        return "B"
    elif x > 70:
        return "C"
    elif x > 65:
        return "D"
    return "F"


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove items from a list
    odds = list(filter(filterFunc, nums))
    print(odds)

    # TODO: use filter on non-numeric sequence
    lowers = list(filter(filterFunc2, chars))
    print(lowers)

    uppers = list(filter(lambda x: x.isupper(), chars))
    print(uppers)

    # TODO: use map to create a new sequence of values
    squares = list(map(lambda x: x ** 2, nums))
    print(squares)

    # trying it to make all uppers
    all_uppers = list(map(lambda x: x.upper(), chars))
    print(all_uppers)
    print(map(lambda x: x.upper(), chars))

    # TODO: use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(grades)
    print(letters)



if __name__ == "__main__":
    main()
