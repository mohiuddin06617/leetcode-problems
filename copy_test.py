import copy

if __name__ == '__main__':
    a = ["a", "b", "c"]
    b = a
    c = a.copy()
    d = copy.deepcopy(a)

    print(a, b, c, d)
    a.append("abc")
    print(a, b, c, d)