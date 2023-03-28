import os, sys

try:

    __import__("paid").main()
            


except Exception as e:

    exit(str(e))

