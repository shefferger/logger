from datetime import datetime
from os import path, mkdir

num = 1
day = 0
noPrint = False


def getName():
    global num, day
    timeNow = datetime.now()
    day = timeNow.day
    _path = 'logs/log-' + str(timeNow.day) + '-' + str(timeNow.month) + '-' + str(timeNow.year) + '-' + str(num) + '.txt'
    if path.exists(_path):
        num += 1
        _path = getName()
    return _path


def log(info):
    timeNow = datetime.now()
    if day != timeNow.day:
        getName()
    if not noPrint:
        print('\n[' + str(timeNow) + ']\t' + str(info))
    with open(fileName, 'a') as logFile:
        logFile.write('\n[' + str(timeNow) + ']\t' + str(info))


if not path.exists('logs'):
    mkdir('logs', 0o755)
fileName = getName()
