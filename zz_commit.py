import os
import time
import sys

# 空文件夹占位文件的处理
rootDir = os.getcwd()
log = open(rootDir + '/zz_temp.log', 'r', encoding='UTF-8')
oldlines = log.readlines()
log.close()

log = open(rootDir + '/zz_main.log', 'w', encoding='UTF-8')
log.writelines(oldlines)
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

for root, dirs, files in os.walk(rootDir):
    for file in files:
        if file == 'gitkeep':
            if len(dirs) != 0:
                os.remove(root + '/gitkeep')
                logfile('路径' + root + '/gitkeep 删除占位文件')
            if len(dirs) == 0 and len(files) > 1:
                os.remove(root + '/gitkeep')
                logfile('路径' + root + '/gitkeep 删除占位文件')
    
for root, dirs, files in os.walk(rootDir):
    result = '.git' in root
    if len(dirs) == 0 and len(files) == 0 and not result:
        gitkeep = open(root + '/gitkeep', 'w', encoding='UTF-8')
        gitkeep.close()
        logfile('路径' + root + '/gitkeep 添加占位文件')

logfile("")
logfile("")

# git操作处理
result = os.popen("git add .")
batchlogfile(result)
result = os.popen("git status")
batchlogfile(result)
result = os.popen("git commit -m '" + time.strftime("%Y%m%d-%H%M") + "'")
batchlogfile(result)
result = os.popen("git push -u origin master")
batchlogfile(result)
result = os.popen("git subtree push --prefix=themes/next next master")
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
