def c(x):
    def a(f):
        def b(n):
            f(n)
            print(x-1)
        return b
    return a

@c(100)
def f(n):
    print(n+1)


f(10)
