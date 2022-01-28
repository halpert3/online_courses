# Demonstrate the usage of namdtuple objects

import collections as c


def main():
    # TODO: create a Point namedtuple
    Point = c.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1, p2)
    print(p1.x, p2.y)


    # TODO: use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1)
    print(p1[0] == p1.x) # True


if __name__ == "__main__":
    main()
