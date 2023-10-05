# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 06:11:36 2023

@author: Yousra
"""

import threading 
lock=threading.lock()
def worker():
    lock.aquire()
    print('worker : ', threading.current_thread().name)
    lock.release()

t1=threading.Thread(target=worker)
t2=threading.Thread(target=worker)
t3=threading.Thread(target=worker)

t1.start()
t2.start()
t3.start()


t3.join()

import threading 
def print_nums():
    for i in range(1,11):
        print(i)
        
t1=threading.Thread(target=print_nums)
t1.run()

t2=threading.Thread(target=print_nums)

t1.start()
t2.start()

import threading 
def print_nums(num):
    for i in range(1,num+1):
        print(i)
        
t1=threading.Thread(target=print_nums, args=(5,))
t2=threading.Thread(target=print_nums, args=(10,))

t1.start()
t1.join()
t2.start()
t2.join()
print('Done')