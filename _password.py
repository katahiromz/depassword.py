#!/usr/bin/env python3

import _config as config

def depassword(de):
    for entry in config.depassword_list:
        real_pass = entry['real_pass']
        fake_pass = entry['fake_pass']
        filename = entry['filename']
        with open(filename, "rb") as fin:
            contents = fin.read().decode()
        if de:
            new_contents = contents.replace(real_pass, fake_pass)
        else:
            new_contents = contents.replace(fake_pass, real_pass)
        if contents == new_contents:
            print("WARNING: Not converted.")
            return
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            tf.write(new_contents.encode())
        import shutil
        shutil.move(tf.name, filename)

def parse_cmdline():
    import sys
    de = True
    sys.argv.pop(0)
    for arg in sys.argv:
        if arg == "--help":
            print("Usage: ./depassword.py")
            print("       ./enpassword.py")
            print("")
            print("NOTE: Please edit _config.py before using this program.")
            sys.exit()
        elif arg == "--version":
            print("depassword.py version 0.5 by katahiromz")
            sys.exit()
        elif arg == "--encode":
            de = False
        elif arg == "--decode":
            de = True
        else:
            print("ERROR: Invalid argument - '" + arg + "'")
            sys.exit(-1)
    depassword(de)

parse_cmdline()
