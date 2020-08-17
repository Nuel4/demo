import threading


class A:
    lockForB = threading.RLock()

class B:

    def __init__(self):
        with A.lockForB:
            #do init stuff

    def othermethod(self):
        with A.lockForB:
            #do other stuff