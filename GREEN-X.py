import os, sys

try:

    __import__("Paid_enc").main()

except Exception as e:

    exit(str(e))
