from tkinter import *
from time import sleep

def add(text, s, cronometro):
    cronometro[10] += 1
    if cronometro[10] == 10:
        cronometro[10] = 0
        cronometro[9] += 1
        if cronometro[9] == 10:
            cronometro[9] = 0
            cronometro[7] += 1 
            if cronometro[7] == 10:
                cronometro[7] = 0
                cronometro[6] += 1
                if cronometro[6] == 6:
                    cronometro[6] = 0
                    cronometro[4] += 1
                    if cronometro[4] == 10:
                        cronometro[4] = 0
                        cronometro[3] += 1
                        if cronometro[3] == 6:
                            cronometro[3] = 0
                            cronometro[1] += 1
                            if cronometro[1] == 4:
                                cronometro[1] = 0
                                cronometro[0] += 1
                                if cronometro[0] == 3:
                                    cronometro[0] = 0
    #if res == True:
    #    cronometro.clear()
    #    cronometro = [0, 0, ':', 0, 0, ':', 0, 0, ':', 0, 0, 0]

    text['text'] = cronometro
    s += (((cronometro[0] + cronometro[1]) + (cronometro[3] + cronometro[4])) + 
    ((cronometro[6] + cronometro[7]) + (cronometro[9] + cronometro[10])))
    return s
    return cronometro
