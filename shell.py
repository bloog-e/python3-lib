import sys,os
import time
def sleep(sec):
    t1=time.time()
    t2=0
    while (t2-t1) < sec:
        t2=time.time()
def clear():
    os.system('clear')
def input(text=None,file=sys.stdin):
    if not text is None:print(text, end='')
    text = file.readline().replace('\n','')
    file.flush()
    return text
def print(*args,file=sys.stdout,end='\n'):
    for text in args:
        file.write(str(text)+' ')
    file.write(end)
    file.flush()