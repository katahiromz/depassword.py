#!/usr/bin/env python3

import subprocess, sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

cmdline = [sys.executable, "_password.py", "--decode"]
cmdline.extend(sys.argv[1:])
subprocess.run(cmdline)
