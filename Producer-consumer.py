from time import sleep
from threading import *

s=1
count=0

def wait(para1):
	global s
	global count
	# print("value of global inside wait:"+str(s))
	while s<=0:
		# print("Blocked state")
		sleep(3)
	s=s-1
	print(para1+" locked")

def signal(para2):
	global s
	global count
	# print("value of global inside signal:"+str(s))
	s=s+1
	print(para2+" released")

class P(Thread):
	def run(self):
		global s
		global count
		print("Producer started")
		for i in range(0,5):
			# print("Consumer blocked")
			wait("Consumer")
			# for i in range(0,5):
			print("Producer producing "+str(i))
			count+=1
			signal("Consumer")
			# print("Consumer released")
			sleep(2)

class C(Thread):
	def run(self):
		global s
		global count
		print("Consumer started")
		sleep(2)
		i=0
		while i<count:
			# print("Producer blocked")
			wait("Producer")
			# for i in range(0,5):
			print("Consumer consuming "+str(i))
			i=i+1
			signal("Producer")
			# print("Producer released")
			sleep(3)
p=P().start()
c=C().start()

