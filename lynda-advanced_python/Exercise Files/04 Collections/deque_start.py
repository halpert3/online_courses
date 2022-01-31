# deque objects are like double-ended queues

import collections
import string


def main():
    
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)
    # print(d)

    # TODO: deques support the len() function
    # print("count: ", len(d))


    # TODO: deques can be iterated over
    # for elem in d:
    #     print(elem.upper(), end=' ')


    # TODO: manipulate items from either end
    for elem in d:
        print(elem, end=' ')
    print('')
    d.rotate(13)
    for elem in d:
        print(elem, end=' ')



    # TODO: rotate the deque


if __name__ == "__main__":
    main()
