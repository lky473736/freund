from multiprocessing import Process, Queue
import os
import time

state = "daramji"

def tokenize() :
    return state