import telepot
import sys
import time
from telepot.loop import MessageLoop
def getData(command):
    cmdMap={'/mem':'meminfo','/cpu':'stat','/partitions':'partitions'}
    try:
        mapped=cmdMap[command]
    except KeyError:
        if command=='/start':
            return '/mem for meminfo,/cpu for stat,/partitions for partitions'
        return 'command not supported'
    path='/proc/'+mapped
    file=open(path,'r')
    content=file.read()
    file.close()
    return content

def handle(msg):
    contentType, chatType, chatId = telepot.glance(msg)
    order=msg['text']
    print(chatId)
    print(order)
    bot.sendMessage(chatId,getData(order))

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop (bot,handle).run_as_thread()
print ('Listening ...')
while 1:
    time.sleep(10)

