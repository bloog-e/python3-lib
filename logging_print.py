from bases.colors import *
from bases.sheel_app import *
from datetime import datetime
def Bot(name,color,*text):
    print(color+datetime.strftime(datetime.now(),'%m/%d/%Y, %H:%M:%S')+' <'+name+'> :',end='')
    for i in text:
        print(color+str(i),end=' ')
    print(reset)
def criticalError(*text):
    print(fgBrightRed+datetime.strftime(datetime.now(),'%m/%d/%Y, %H:%M:%S')+' [Critial] :',end='')
    for i in text:
        print(fgBrightRed+str(i),end=' ')
    print(reset)
def Error(*text):
    print(fgRed+datetime.strftime(datetime.now(),'%m/%d/%Y, %H:%M:%S')+' [Error] :',end='')
    for i in text:
        print(fgRed+str(i),end=' ')
    print(reset)
def Warn(*text):
    print(fgBrightYellow+datetime.strftime(datetime.now(),'%m/%d/%Y, %H:%M:%S')+' [Warning] :',end='')
    for i in text:
        print(fgBrightYellow+str(i),end=' ')
    print(reset)
def Info(*text):
    print(fgBrightGreen+datetime.strftime(datetime.now(),'%m/%d/%Y, %H:%M:%S')+' [Info] :',end='')
    for i in text:
        print(fgBrightGreen+str(i),end=' ')
    print(reset)
def Debug(*text):
    print(fgBrightBlue+datetime.strftime(datetime.now(),'%m/%d/%Y, %H:%M:%S')+' [Debug] :',end='')
    for i in text:
        print(fgBrightBlue+str(i),end=' ')
    print(reset)
def test():
    criticalError('criticalError test!')
    Error('Error test!')
    Warn('Warn test!')
    Info('Info test!')
    Debug('Debug test!')
    
if __name__ == '__main__':
    criticalError('criticalError test!')
    Error('Error test!')
    Warn('Warn test!')
    Info('Info test!')
    Debug('Debug test!')
else:
    Info('Importing logging module is a Succses !\n')