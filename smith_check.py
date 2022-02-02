#!/usr/bin/env python3
# Author: Kurt Irvin Rojas
# https://github.com/kimrojas/smith_utils
import sys, os, subprocess
sys.dont_write_bytecode = True
from threading import Thread
import smith_spinner as ss
from time import sleep
from smith_user_parse import user 
from smith_output import blue, green, warning, fail, bold, underline


def check():
    print("** Establishing Connection  ... ", end="")
    spinner = ss.Spinner()
    spinner.start()
    tlocal = Thread(target=check_local)
    tglobal = Thread(target=check_global)
    tlocal.start()
    tglobal.start()

    while tlocal.is_alive() or tglobal.is_alive():
        sleep(0.1)

    tlocal.join()
    tglobal.join()
    spinner.stop()

    if rcode_local == 0:
        res = "UseLocal"
        print(underline(res))
        return res
    elif rcode_global == 0:
        res = "UseGlobal"
        print(underline(res))
        return res
    else:
        print(fail("ConnectionError"))
        print(fail("**If you are outside the university, run `smith_tunnel` in a separate terminal before running this code again"))
        sys.exit()


def check_local(n=1):
    bashCommand = f"ssh -o ConnectTimeout={n} {user['smith_username']}@{user['smith_ip']} 'exit'"
    process_local = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process_local.communicate()
    global rcode_local
    rcode_local = process_local.returncode
    sleep(0.5)

def check_global(n=1):
    bashCommand =f"ssh -o ConnectTimeout={n} {user['smith_username']}@localhost -p {user['smith_univ_port']} 'exit'"
    process_global = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process_global.communicate()
    global rcode_global
    rcode_global = process_global.returncode
    sleep(0.5)



