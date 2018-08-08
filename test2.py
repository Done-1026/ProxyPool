class A():

    def __init__(self):
        self.f()
    
    def a(m,n):
        def b(x):
            def c(self):
                nm = m + 1
                j = 3
                i = 4
                x(self,i,j)
                print(nm)
                print(n)
            return c
        return b

    @a(1,2)
    def f(self,i,j):
        print(i)
        print(j)

a = A()

