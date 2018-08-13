from threading import Thread

class MyThread(Thread):

    def __init__(self,func,name=''):
        super().__init__()
        self.func = func
        #self.args = args
        self.name = name

    def run(self):
        return self.func()

    
    
class CheckThread(Thread):

    def __init__(self,func,args,name=''):
        super().__init__()
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        return self.func(self.args)
