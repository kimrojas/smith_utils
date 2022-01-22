#!/usr/bin/env python3
# Author: Kurt Irvin Rojas
# https://github.com/kimrojas/smith_utils
import itertools
import sys
import time
import threading

# lst = ['* . . . .', '. * . . .', '. . * . .', '. . . * .','. . . . *',
# '. . . * .', '. . * . .', '. * . . .','* . . . .']

lst = ['-', '/', '|', '\\']
class Spinner(object):
    spinner_cycle = itertools.cycle(lst)

    def __init__(self):
        self.stop_running = threading.Event()
        self.spin_thread = threading.Thread(target=self.init_spin)

    def start(self):
        self.spin_thread.start()

    def stop(self):
        self.stop_running.set()
        self.spin_thread.join()

    def init_spin(self):
        while not self.stop_running.is_set():
            sys.stdout.write(next(self.spinner_cycle))
            sys.stdout.flush()
            time.sleep(0.05)
            sys.stdout.write('\b')

def work_flow(fn, init_str="STARTING WORK", fin_str="WORK COMPLETE", verbose=True):
    if verbose: print("Starting work")
    spinner = Spinner()
    spinner.start()
    fn()
    spinner.stop()
    if verbose: print("Work complete")

def work_fn():
    time.sleep(5)


if __name__ == '__main__':
    work_flow(work_fn)