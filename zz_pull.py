import os
import time
import sys

# 空文件夹占位文件的处理
rootDir = os.getcwd()
log = open(rootDir + '/zz_temp.log', 'r', encoding='UTF-8')
oldlines = log.readlines()
log.close()

log = open(rootDir + '/zz_temp.log', 'w', encoding='UTF-8')


def logfile(content):    
    print(content + "\r", file=log)    


def batchlogfile(result):
    info = result._stream.readlines()
    result.close()
    for line in info:  
        logfile(line)


output = sys.stdout

sys.stdout = log

logfile("============================begin============================")
logfile("=====================" + time.strftime("%Y-%m-%d %H:%M:%S") + "=====================")
logfile("=============================================================")

# git操作处理
result = os.popen("git pull")
batchlogfile(result)
result = os.popen("git fetch next master")
batchlogfile(result)
result = os.popen("git subtree pull --prefix=themes/next next master --squash")
batchlogfile(result)
logfile("=============================================================")
logfile("=====================" + time.strftime("%Y-%m-%d %H:%M:%S") + "=====================")
logfile("=============================end=============================")
logfile("")
logfile("")
logfile("")

log.writelines(oldlines)
sys.stdout = output
log.close()
