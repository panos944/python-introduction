class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y


    def __repr__(self):
        return f"Point({self.__x}, {self.__y}"
    

def main():
    p1 = Point(10, 20)
    p2 = Point(2, 4)
    p3 = Point(10, 20)
    p4 = Point(100, 200)
    p5 = Point(33, 77)

    print(f"p1 == p2: {p1 == p2}")
    print(f"p2 == p3: {p2 == p3}")

    print("Hash Values")
    print(f"Hash(p1): {hash(p1)}")
    print(f"Hash(p2): {hash(p2)}")
    print(f"Hash(p3): {hash(p3)}")
    print(f"Hash(p4): {hash(p4)}")
    print(f"Hash(p5): {hash(p5)}")

    point_dict = {
        p1: "Point 1",
        p1: "Point 2",
        p1: "Point 3"
    }

    for key, value in point_dict.items():
        print(f"{key} : {value}")


if __name__ == "__main__":
    main()