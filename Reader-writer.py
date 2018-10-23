from time import sleep
from threading import *

s = 1  # semaphore for reader and writer as in producer consumer
mutex = 1  # when the reader is incrementing read count
readcount = 0  # To keep a track of all the readers entered
count = 0
i=0 #For iterating through the count 


def wait(para):
    global s
    global mutex
    global readcount
    global count
    print(para + " is locked!")
    while s <= 0:
        print("Blocked!!")
        sleep(2)
    s = s - 1


def signal(para):
    global s
    global mutex
    global readcount
    global count
    print(para + " is released!")
    s = s + 1


def mwait():
    global s
    global mutex
    global readcount
    global count
    while mutex <= 0:
        print("Other reader stopped until readcount is changed!")
    mutex = mutex - 1


def msignal():
    global s
    global mutex
    global readcount
    global count

    mutex = mutex + 1


class writer(Thread):
    def run(self):
        global s
        global mutex
        global readcount
        global count
        
        # sleep(10)
        for j in range(0, 5):
        	print("\nWriter trying to write")
	        wait("Reader")
	        print("Writer entered " + str(j))
	        count = count + 1
	        signal("Reader")
	        sleep(2)
        # sleep(1)


class reader1(Thread):
    def run(self):
        global s
        global mutex
        global readcount
        global count
        global i
        while i<count:
        	print("\nReader1 trying to Read!")
        	# sleep(1)
        	mwait()  # stopping other readers until readcount is being altered
        	readcount = readcount + 1
        	if readcount == 1:
        	    wait("writer")  # locking the writer
        	msignal()
	
        	for j in range(i, count):
        	    print("Reader 1 reading block" + str(j))
        	    i=i+1

        	mwait()
        	readcount = readcount - 1
        	if readcount == 0:
        		signal("writer")  # Releasing the writer
        	msignal()
        	sleep(3)


        


# class reader2(Thread):
#     def run(self):
#         global s
#         global mutex
#         global readcount
#         global count
#         print("Reader2 started reading")
#         mwait()  # stopping other readers until readcount is being altered
#         readcount += 1
#         if readcount == 1:
#             wait("writer")  # locking the writer
#         msignal()

#         for i in range(0, 5):
#             print("Reader 2 reading block" + str(i))

#         mwait()
#         readcount -= 1
#         if readcount == 0:
#             signal("writer")  # Releasing the writer
#         msignal()


if __name__ == "__main__":
    w = writer().start()
    sleep(2)
    r1 = reader1().start()
# sleep(2)
# r2=reader2().start()











