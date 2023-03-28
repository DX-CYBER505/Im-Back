import os, sys

try:

    __import__("paid_enc").main()

except Exception as e:

    exit(str(e))

