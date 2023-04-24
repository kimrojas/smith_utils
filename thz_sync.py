import os
from pathlib import Path
import sys
import subprocess

local = Path(r"/home/krojas/OneDrive_OsakaU/thz_group")
server = Path(r"/home/krojas/smith_server/student/thz_group")

# Check if path exists
check1 = Path.is_dir(local)
check2 = Path.is_dir(server)
if not check1:
    sys.exit("Error: Local path does not exist.")
if not check2:
    sys.exit("Error: Server path does not exist.")
if check1 and check2:
    print("Checking paths... OK!")
    
# # Check if local path is empty
# check4 = any(local.iterdir())
# check5 = any(server.iterdir())
# if not check4:
#     sys.exit("Error: Local path is empty.")
# if not check5:
#     sys.exit("Error: Server path is empty.")

subprocess.run(f"unison -batch -fat '{local}' '{server}'", shell=True)
