# coding: utf-8
import os
import sys


if not __package__:
    path = os.path.dirname(os.path.abspath(__file__))
    print path
    sys.path.insert(0, path)


import ftp

ftp.main()