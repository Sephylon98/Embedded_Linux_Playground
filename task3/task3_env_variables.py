#Write a python program to access environment variables.

import os

for key,value in os.environ.items():
    print("{}:{}".format(key,value))