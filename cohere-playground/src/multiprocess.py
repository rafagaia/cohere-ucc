import sys
import gc
import time
import threading
import multiprocessing
# from subprocess import Popen, PIPE




def check_daemonic_threads():
    for t in threading.enumerate():
        if t.daemon and t.is_alive():
            t.join()

def join_active_children():
    for p in multiprocessing.active_children():
        p.join()

def gc_collect_exit(s):
    gc.collect()
    sys.exit(s)

def sleeep(t):
    time.sleep(t)


# def speed_up(t):
    # for p in multiprocessing.active_children():
    #     p.sleep(t) #TODO: possible?
# @TODO: does the concept of "sleeping negative time" make sense?
#   that is, process requesting negative sleep may command any or all of their
#       child process to sleep that same amount of time (or more), in +time.
#           as a result, parent process will have a "speed-up" as child process(es) will not
#               be disputing for CPU and memory.
    