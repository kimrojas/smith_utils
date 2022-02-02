class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m' 
    WARNING = '\033[93m'  ## yellow
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def green(a):
    return bcolors.OKGREEN + a + bcolors.ENDC

def blue(a):
    return bcolors.OKBLUE + a + bcolors.ENDC

def cyan(a):
    return bcolors.OKCYAN + a + bcolors.ENDC

def warning(a): # yellow
    return bcolors.WARNING + a + bcolors.ENDC

def fail(a): # red
    return bcolors.FAIL + a + bcolors.ENDC

def bold(a): 
    return bcolors.BOLD + a + bcolors.ENDC

def underline(a):
    return bcolors.UNDERLINE + a + bcolors.ENDC

def header(a):
    return bcolors.HEADER + a + bcolors.ENDC

# print(warning("WARNING"))
# print(fail("FAIL"))
# print(underline("UNDERLINE"))
# print(header("HEADER"))
# print(underline("UNDERLINE"))

# print(cyan("WARNING"))
# print(blue("WARNING"))