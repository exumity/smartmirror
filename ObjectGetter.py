import ctypes


class Object(object):
    def getObjectWithId(self,_id):
        print("geter ici :\n"+str(_id))

        o = ctypes.cast(int(_id), ctypes.py_object).value

        print(o)
        print("------------->\n")
        if o:
            return o
        else:
            return None

