def product(*num):
    if num==():
        raise ('typerror')
    else:
        y=1
        for n in num:
            y=y*n
        return y
print(product(5,6,7,8))