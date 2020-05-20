import argparse
import glob
from os import rename
import sys
import uuid


print(sys.argv[1])
parser = argparse.ArgumentParser()
parser.add_argument('extension', type=str, help='extension to match agains, \'.jph\'')
args = parser.parse_args()
print("Extension to match: ", args.extension)
files = glob.glob('*.' + args.extension)
print("Will rename following files:")
for filename in files:
    print(filename)
try:
    if str.lower(input("y/n? ")) == 'y':
        for filename in files:
            rename(filename, str(uuid.uuid4()) + '.' + args.extension)
    else:
        print("ok, nevermind")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
