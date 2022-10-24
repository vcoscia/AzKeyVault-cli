
from clint.textui import colored
from pyfiglet import Figlet
import sys 
import time 
import itertools
import threading

from tabulate import tabulate

def printAsTable(data):
  print(tabulate(data,headers='keys',tablefmt='pretty'))
     
def animate():
    global AUTH 
    global ERROR 
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if AUTH or ERROR:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

def welcome(text):
    result = Figlet()
    return colored.cyan(result.renderText(text))


def log(msg):
  print(msg)

def error(msg):
  print(f"\033[31m {msg} \033[0m")