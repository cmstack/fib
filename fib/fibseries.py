def fibseries(n):
    # xn = xn−1 + xn−2
    # xn is term number "n"
    # xn−1 is the previous term (n−1)
    # xn−2 is the term before that (n−2)
    first = 0
    second = 1
    count = 0
    while count < n+1:
        print(first)
        first, second = second, first+second
        count += 1

if __name__ == '__main__':
    fibseries(20)