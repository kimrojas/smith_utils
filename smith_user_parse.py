# Author: Kurt Irvin Rojas
# https://github.com/kimrojas/smith_utils
"""
Reads the user settings in $HOME/.smith_utils
Settings are available in the "user" variable.
Simply export
Usage:
    from smith_user_parse import user
"""
import os
import sys
sys.dont_write_bytecode = True
import configparser


cache_file = os.path.join(os.environ["HOME"],
                          ".smith_utils",
                          "settings.txt")
config = configparser.ConfigParser()
config.read(cache_file)
user = dict(config['SETTINGS'])

