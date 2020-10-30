from datetime import datetime
from os import path, mkdir

num = 1
day = 0
noPrint = False
logIntoFile = True


def getName():
    global num, day
    timeNow = datetime.now()
    day = timeNow.day
    _path = 'logs/log-' + str(timeNow.year) + '-' + str(timeNow.month) + '-' + str(timeNow.day) + '-' + str(num) + '.txt'
    if path.exists(_path):
        num += 1
        _path = getName()
    return _path


def log(*info):
    timeNow = datetime.now()
    data = ''
    for i in info:
        data += str(i) + ' | '
    data = data[:-2] + '>>'
    if day != timeNow.day:
        getName()
    if not noPrint:
        print('\n[' + str(timeNow) + ']<<  ' + str(data))
    if logIntoFile:
        with open(fileName, 'a') as logFile:
            logFile.write('\n[' + str(timeNow) + ']<<  ' + str(data))


if not path.exists('logs'):
    mkdir('logs', 0o755)
fileName = getName()
