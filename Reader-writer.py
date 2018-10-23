from time import sleep
from threading import *

s = 1  # semaphore for reader and writer as in producer consumer
mutex = 1  # when the reader is incrementing read count
readcount = 0  # To keep a track of all the readers entered
count = 0
i=0 #For iterating through the count for reader1
k=0 #For iterating through the count for reader2


def wait(para):
    global s
    global mutex
    global readcount
    global count
    while s <= 0:
        print("Blocked!!")
        sleep(0.5)
    s = s - 1
    print(para + " is locked!")


def signal(para):
    global s
    global mutex
    global readcount
    global count
    s = s + 1
    print(para + " is released!")


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
        	print("Number of reader in critical section:"+str(readcount))
        	for j in range(i, count): #Critical section
        	    print("Reader 1 reading block" + str(j))
        	    i=i+1
        	    sleep(2)

        	mwait()
        	readcount = readcount - 1
        	if readcount == 0:
        		signal("writer")  # Releasing the writer
        	msignal()
        	sleep(3)

class reader2(Thread):
    def run(self):
        global s
        global mutex
        global readcount
        global count
        global k
        while k<count:
        	print("\nReader2 trying to Read!")
        	# sleep(1)
        	mwait()  # stopping other readers until readcount is being altered
        	readcount = readcount + 1
        	if readcount == 1:
        	    wait("writer")  # locking the writer
        	msignal()
        	print("Number of reader in critical section:"+str(readcount))
        	for j in range(k, count):
        	    print("Reader 2 reading block" + str(j))
        	    k=k+1
        	    sleep(2)

        	mwait()
        	readcount = readcount - 1
        	if readcount == 0:
        		signal("writer")  # Releasing the writer
        	msignal()
        	sleep(3)

        





if __name__ == "__main__":
	w = writer().start()
	sleep(1)
	r1 = reader1().start()
	sleep(1)
	r2=reader2().start()











