import os, sys
os.system("git pull")
try:
    __import__("tool").anas()
except Exception as e:
    exit(str(e))