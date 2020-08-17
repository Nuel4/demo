from threading import *
from time import sleep
class hello(Thread):
    def run(self):
        for i in range(10):
            print('hello')
            sleep(1)


class hi(Thread):
    def run(self):
        for j in range(10):
            print('hi')
            sleep(1)

h1 =hello()
h2 =hi()
#h1.run() # will complet printing first
#h2.run()  # can only start after h1 has finied
print(" ............................")
h1.start() #print first
sleep(0.2) # h1 will wait for 0.2
h2.start() # print one and sleep for 0.2 seconds
h1.join() # main thread will allow h1 to complete execution before it jpins
h2.join() # main thread will allow h1 to complete execution before it jpins
print('all complete')  # main thread to execute this