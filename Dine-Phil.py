from threading import *
from time import sleep
fork=[1]*5 #semaphore for each and every fork
def wait(index):
	global fork
	while fork[index]<=0:
		
		print("\nwaiting state")
		sleep(1)
	fork[index]=fork[index]-1

def signal(index):
	global fork
	fork[index]=fork[index]+1


class Philosopher1(Thread):
	def run(self):
		global fork
		for i in range(0,1):
			wait(0)
			print("\nFork 0 is Locked")
			sleep(2)
			wait(1)
			print("Fork 1 is Locked\n")
			sleep(2)
			print("Philosopher 1 is eating")
			sleep(1)
			signal(0)
			print("Fork 0 released")
			signal(1)
			print("Fork 1 released")
			sleep(1)

		

class Philosopher2(Thread):
	def run(self):
		global fork
		for i in range(0,1):
			wait(1)
			print("\nFork 1 is Locked")
			sleep(2)
			wait(2)
			print("Fork 2 is Locked\n")
			sleep(2)
			print("Philosopher 2 is eating")
			sleep(1)
			signal(1)
			print("Fork 1 released")
			signal(2)
			print("Fork 2 released")
			sleep(1)


class Philosopher3(Thread):
	def run(self):
		global fork
		for i in range(0,1):
			wait(2)
			print("\nFork 2 is Locked")
			sleep(2)
			wait(3)
			print("Fork 3 is Locked\n")
			sleep(2)
			print("Philosopher 3 is eating")
			sleep(1)
			signal(2)
			print("Fork 2 released")
			signal(3)
			print("Fork 3 released")
			sleep(1)

class Philosopher4(Thread):
	def run(self):
		global fork
		for i in range(0,1):
			wait(3)
			print("\nFork 3 is Locked")
			sleep(2)
			wait(4)
			print("Fork 4 is Locked\n")
			sleep(2)
			print("Philosopher 4 is eating")
			sleep(1)
			signal(3)
			print("Fork 3 released")
			signal(4)
			print("Fork 4 released")
			sleep(1)

class Philosopher5(Thread):
	def run(self):
		global fork
		for i in range(0,1):
			wait(0)
			print("\nFork 4 is Locked")
			sleep(2)
			wait(4)
			print("Fork 0 is Locked\n")
			sleep(2)
			print("Philosopher 5 is eating")
			sleep(2)
			signal(0)
			print("Fork 3 released")
			signal(4)
			print("Fork 0 released")
			sleep(1)

if __name__=="__main__":
	p1=Philosopher1().start()
	p2=Philosopher2().start()
	p3=Philosopher3().start()
	p4=Philosopher4().start()
	p5=Philosopher5().start()


