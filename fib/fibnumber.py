def fibnumber(n):
    # xn = xn−1 + xn−2
    # xn is term number "n"
    # xn−1 is the previous term (n−1)
    # xn−2 is the term before that (n−2)
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

'''
if __name__ == '__main__':
    fibnumber()
'''

# 1,2,3,4,5
# 1,3,5,7,9