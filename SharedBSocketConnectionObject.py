import weakref
import gc


class Foo:
    sock=None
    def __init__(self):
        pass
    def setSock(self,sock):
        self.sock=sock
    def getSocket(self):
        return self.sock




if __name__=="__main__":

    x= Foo()
    r = weakref.ref(x)
    gc.collect()
    assert r() is x
    print(r)
    print(x)
    print(id(x))

    print(id(r))
    print("\n")

    while True:
        pass


